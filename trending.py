"""Fetch popular, recently-active GitHub repos, set aside AI/LLM-focused
projects, and publish the rest as canonical JSON plus a README table.

Pipeline: fetch -> normalize -> filter -> rank -> build_dataset
          -> write_json -> render_readme

data/trending.json is the canonical output; the README table (and, later,
the website) are renderers of that same dataset.
"""

import json
import os
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone

import requests

# 1. Configuration
SCHEMA_VERSION = 1  # Only additive changes within a version; breaking changes bump it.
MIN_STARS = 100  # Minimum stars to consider a repo popular
DAYS_BACK = 7  # Look at repos active in the last X days
FRESH_DAYS = 365  # A repo created within this window counts as "new"
MAX_FRESH_README_ROWS = 15  # Soft cap for the README's New & rising table
README_FILE = "README.md"
JSON_FILE = "data/trending.json"
HISTORY_DIR = "data/history"
START_MARKER = "<!-- TRENDING:START -->"
END_MARKER = "<!-- TRENDING:END -->"
LANG_START_MARKER = "<!-- BY_LANGUAGE:START -->"
LANG_END_MARKER = "<!-- BY_LANGUAGE:END -->"
FRESH_START_MARKER = "<!-- FRESH:START -->"
FRESH_END_MARKER = "<!-- FRESH:END -->"
MAX_LANGUAGES = 6  # Soft caps for the by-language README sections
MAX_REPOS_PER_LANGUAGE = 10

# Keywords used to identify AI/LLM-focused repositories for exclusion.
# Matched on word boundaries so "ai" doesn't match "maintain" or "email".
AI_KEYWORDS = [
    "ai",
    "llm",
    "llms",
    "gpt",
    "claude",
    "agent",
    "agents",
    "agentic",
    "copilot",
    "rag",
    "deepseek",
    "artificial intelligence",
    "large language model",
    "prompt engineering",
    "transformers",
    "langchain",
    "llama",
    "stable diffusion",
    "machine learning",
    "deep learning",
    "neural network",
    "neural networks",
    "ml",
    "chatgpt",
    "openai",
    "gemini",
    "diffusion",
    "text-to-image",
    "text-to-speech",
]

AI_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(k) for k in AI_KEYWORDS) + r")\b",
    re.IGNORECASE,
)


def get_gh_cli_token() -> str | None:
    """Get the GitHub token stored by the gh CLI, if gh is installed and logged in."""
    if shutil.which("gh") is None:
        return None
    result = subprocess.run(
        ["gh", "auth", "token"], capture_output=True, text=True
    )
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def fetch_repositories(created_within: int | None = None) -> list[dict]:
    """Fetch raw search results from the GitHub Search API. With
    `created_within`, restrict to repos created in the last N days."""
    now = datetime.now(timezone.utc)
    time_threshold = (now - timedelta(days=DAYS_BACK)).strftime("%Y-%m-%d")

    query = f"stars:>{MIN_STARS} pushed:>{time_threshold}"
    if created_within is not None:
        created_threshold = (
            now - timedelta(days=created_within)
        ).strftime("%Y-%m-%d")
        query += f" created:>{created_threshold}"

    url = "https://api.github.com/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
    }

    # Auth is optional but raises the rate limit. Uses GITHUB_TOKEN if set,
    # otherwise falls back to the gh CLI's stored login (`gh auth token`).
    headers = {"Accept": "application/vnd.github.v3+json"}
    token = os.getenv("GITHUB_TOKEN") or get_gh_cli_token()
    if token:
        headers["Authorization"] = f"token {token}"
    else:
        print("Warning: no auth found; using the low anonymous rate limit.")

    print(f"Fetching active repositories since {time_threshold}...")
    response = requests.get(url, params=params, headers=headers, timeout=30)

    if response.status_code != 200:
        print(f"Error fetching data from GitHub API: {response.status_code}")
        try:
            print(response.json().get("message", ""))
        except ValueError:
            print(response.text[:500])
        return []

    return response.json().get("items", [])


def normalize_repository(item: dict) -> dict:
    """Reduce a raw API item to the fields the dataset needs, tolerating
    missing or null optional fields."""
    return {
        "name": item.get("name") or "",
        "full_name": item.get("full_name") or "",
        "url": item.get("html_url") or "",
        "description": item.get("description") or "",
        "stars": item.get("stargazers_count") or 0,
        "language": item.get("language") or "Unknown",
        "updated_at": (item.get("pushed_at") or "")[:10],
        "created_at": (item.get("created_at") or "")[:10],
        "topics": item.get("topics") or [],
    }


def normalize_repositories(items: list[dict]) -> list[dict]:
    return [normalize_repository(item) for item in items]


def is_ai_repo(repo: dict) -> bool:
    """Check a normalized repo's name, description, and topics for AI keywords."""
    haystack = " ".join(
        [repo["name"], repo["description"], " ".join(repo["topics"])]
    )
    return AI_PATTERN.search(haystack) is not None


def filter_repositories(repos: list[dict]) -> list[dict]:
    return [repo for repo in repos if not is_ai_repo(repo)]


def rank_repositories(repos: list[dict]) -> list[dict]:
    """Sort by stars and assign `rank`: the position in the primary trending
    list after filtering and sorting (not a universal ranking)."""
    ranked = sorted(repos, key=lambda r: (-r["stars"], r["full_name"]))
    for idx, repo in enumerate(ranked, start=1):
        repo["rank"] = idx
    return ranked


def dataset_entry(repo: dict) -> dict:
    return {
        "rank": repo["rank"],
        "full_name": repo["full_name"],
        "url": repo["url"],
        "description": repo["description"],
        "stars": repo["stars"],
        "language": repo["language"],
        "updated_at": repo["updated_at"],
        "created_at": repo.get("created_at", ""),
    }


def build_dataset(
    repos: list[dict],
    generated_at: str | None = None,
    fresh: list[dict] | None = None,
) -> dict:
    """Assemble the canonical schema-versioned dataset. `fresh` is the
    separately fetched list of repos created within FRESH_DAYS."""
    if generated_at is None:
        generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,
        "criteria": {
            "min_stars": MIN_STARS,
            "days_back": DAYS_BACK,
            "fresh_days": FRESH_DAYS,
        },
        "filter": {"type": "keyword", "keywords": AI_KEYWORDS},
        "repositories": [dataset_entry(repo) for repo in repos],
        "fresh_repositories": [dataset_entry(repo) for repo in fresh or []],
    }


def rank_from_snapshot(snapshot: dict) -> dict:
    """Reconstruct ranks from a {full_name: stars} snapshot using the same
    sort rule as rank_repositories."""
    ordered = sorted(snapshot.items(), key=lambda kv: (-kv[1], kv[0]))
    return {full_name: idx for idx, (full_name, _) in enumerate(ordered, 1)}


def load_previous_ranks(today: str, directory: str = HISTORY_DIR) -> dict | None:
    """Load the most recent snapshot strictly before `today` (YYYY-MM-DD)
    and return {full_name: rank}, or None when no history exists yet."""
    if not os.path.isdir(directory):
        return None
    dates = sorted(
        f[:-5]
        for f in os.listdir(directory)
        if f.endswith(".json") and f[:-5] < today
    )
    if not dates:
        return None
    with open(f"{directory}/{dates[-1]}.json", encoding="utf-8") as f:
        return rank_from_snapshot(json.load(f))


def annotate_previous_ranks(dataset: dict, previous_ranks: dict | None) -> dict:
    """Add `previous_rank` (int, or None for repos absent from the previous
    observation) to each repo. A repo missing from a snapshot is unknown,
    not zero — with no previous snapshot at all, the field is omitted."""
    if previous_ranks is None:
        return dataset
    for repo in dataset["repositories"]:
        repo["previous_rank"] = previous_ranks.get(repo["full_name"])
    return dataset


def write_snapshot(dataset: dict, directory: str = HISTORY_DIR) -> None:
    """Record today's observed star counts for future comparisons."""
    os.makedirs(directory, exist_ok=True)
    date = dataset["generated_at"][:10]
    snapshot = {r["full_name"]: r["stars"] for r in dataset["repositories"]}
    path = f"{directory}/{date}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(f"Wrote snapshot of {len(snapshot)} repositories to {path}.")


def write_json(dataset: dict, path: str = JSON_FILE) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dataset, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {len(dataset['repositories'])} repositories to {path}.")


def clean_cell(text: str, max_len: int = 140) -> str:
    """Make a description safe for a markdown table cell."""
    text = " ".join(text.split()).replace("|", "\\|")
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip() + "…"
    return text


def format_rank_change(repo: dict) -> str:
    """Positions moved in the primary ranking since the previous snapshot
    (never stars): NEW / ↑ n / ↓ n / —."""
    previous = repo.get("previous_rank")
    if previous is None:
        return "NEW"
    delta = previous - repo["rank"]
    if delta > 0:
        return f"↑ {delta}"
    if delta < 0:
        return f"↓ {-delta}"
    return "—"


def render_table(dataset: dict) -> str:
    criteria = dataset["criteria"]
    date_str = datetime.strptime(
        dataset["generated_at"], "%Y-%m-%dT%H:%M:%SZ"
    ).strftime("%Y-%m-%d %H:%M UTC")
    # The Change column only appears once a previous snapshot exists.
    has_history = any(
        "previous_rank" in repo for repo in dataset["repositories"]
    )

    lines = [
        f"*Last updated: **{date_str}** — repos with"
        f" >{criteria['min_stars']:,} stars, active in the last"
        f" {criteria['days_back']} days, no AI keywords detected.*",
        "",
    ]
    if has_history:
        lines += [
            "| # | Change | Repository | ⭐ Stars | Language | Description |",
            "|--:|:------:|------------|--------:|----------|-------------|",
        ]
    else:
        lines += [
            "| # | Repository | ⭐ Stars | Language | Description |",
            "|--:|------------|--------:|----------|-------------|",
        ]
    for repo in dataset["repositories"]:
        description = repo["description"] or "No description provided."
        change = f" {format_rank_change(repo)} |" if has_history else ""
        lines.append(
            f"| {repo['rank']} |{change} [{repo['full_name']}]({repo['url']}) "
            f"| {repo['stars']:,} | {repo['language']} "
            f"| {clean_cell(description)} |"
        )
    if has_history:
        lines += [
            "",
            "*Change = positions moved in this list since the previous"
            " update; NEW = not in the previous update.*",
        ]
    return "\n".join(lines)


def render_language_sections(
    dataset: dict,
    max_languages: int = MAX_LANGUAGES,
    max_repos: int = MAX_REPOS_PER_LANGUAGE,
) -> str:
    """Group the primary list by language: up to `max_languages` sections of
    up to `max_repos` each. Repos without a detected language are skipped."""
    by_language: dict[str, list[dict]] = {}
    for repo in dataset["repositories"]:
        if repo["language"] == "Unknown":
            continue
        by_language.setdefault(repo["language"], []).append(repo)

    languages = sorted(
        by_language, key=lambda lang: (-len(by_language[lang]), lang)
    )[:max_languages]

    lines = []
    for language in languages:
        lines += [
            f"### {language}",
            "",
            "| Repository | ⭐ Stars | Description |",
            "|------------|--------:|-------------|",
        ]
        for repo in by_language[language][:max_repos]:
            description = repo["description"] or "No description provided."
            lines.append(
                f"| [{repo['full_name']}]({repo['url']}) "
                f"| {repo['stars']:,} | {clean_cell(description)} |"
            )
        lines.append("")
    return "\n".join(lines).rstrip()


def render_fresh_section(
    dataset: dict, max_rows: int = MAX_FRESH_README_ROWS
) -> str:
    """Markdown table of trending repos created within the fresh window."""
    fresh = dataset.get("fresh_repositories", [])[:max_rows]
    if not fresh:
        return (
            "*No repositories created in the last year met the criteria"
            " today.*"
        )
    lines = [
        "| # | Repository | ⭐ Stars | Language | Created | Description |",
        "|--:|------------|--------:|----------|---------|-------------|",
    ]
    for repo in fresh:
        description = repo["description"] or "No description provided."
        lines.append(
            f"| {repo['rank']} | [{repo['full_name']}]({repo['url']}) "
            f"| {repo['stars']:,} | {repo['language']} "
            f"| {repo.get('created_at', '') or '—'} "
            f"| {clean_cell(description)} |"
        )
    return "\n".join(lines)


def splice_markers(
    readme: str,
    replacement: str,
    start: str = START_MARKER,
    end: str = END_MARKER,
) -> str:
    """Replace the content between a marker pair, idempotently."""
    if start not in readme or end not in readme:
        raise SystemExit(f"Markers {start} / {end} not found in README")
    head, rest = readme.split(start, 1)
    _, tail = rest.split(end, 1)
    return head + start + "\n" + replacement + "\n" + end + tail


def render_readme(dataset: dict, path: str = README_FILE) -> None:
    with open(path, encoding="utf-8") as f:
        readme = f.read()

    updated = splice_markers(readme, render_table(dataset))
    updated = splice_markers(
        updated,
        render_fresh_section(dataset),
        start=FRESH_START_MARKER,
        end=FRESH_END_MARKER,
    )
    updated = splice_markers(
        updated,
        render_language_sections(dataset),
        start=LANG_START_MARKER,
        end=LANG_END_MARKER,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Updated {path} with {len(dataset['repositories'])} repositories.")


def main() -> None:
    items = fetch_repositories()
    repos = rank_repositories(filter_repositories(normalize_repositories(items)))
    if not repos:
        print("No repositories found; leaving outputs untouched.")
        return
    fresh_items = fetch_repositories(created_within=FRESH_DAYS)
    fresh = rank_repositories(
        filter_repositories(normalize_repositories(fresh_items))
    )
    dataset = build_dataset(repos, fresh=fresh)
    # Compare against yesterday before recording today's observation.
    previous_ranks = load_previous_ranks(dataset["generated_at"][:10])
    annotate_previous_ranks(dataset, previous_ranks)
    write_snapshot(dataset)
    write_json(dataset)
    render_readme(dataset)


if __name__ == "__main__":
    main()
