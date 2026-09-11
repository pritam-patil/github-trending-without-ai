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
README_FILE = "README.md"
JSON_FILE = "data/trending.json"
START_MARKER = "<!-- TRENDING:START -->"
END_MARKER = "<!-- TRENDING:END -->"

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


def fetch_repositories() -> list[dict]:
    """Fetch raw search results from the GitHub Search API."""
    time_threshold = (
        datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)
    ).strftime("%Y-%m-%d")

    url = "https://api.github.com/search/repositories"
    params = {
        "q": f"stars:>{MIN_STARS} pushed:>{time_threshold}",
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


def build_dataset(repos: list[dict], generated_at: str | None = None) -> dict:
    """Assemble the canonical schema-versioned dataset."""
    if generated_at is None:
        generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at,
        "criteria": {"min_stars": MIN_STARS, "days_back": DAYS_BACK},
        "filter": {"type": "keyword", "keywords": AI_KEYWORDS},
        "repositories": [
            {
                "rank": repo["rank"],
                "full_name": repo["full_name"],
                "url": repo["url"],
                "description": repo["description"],
                "stars": repo["stars"],
                "language": repo["language"],
                "updated_at": repo["updated_at"],
            }
            for repo in repos
        ],
    }


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


def render_table(dataset: dict) -> str:
    criteria = dataset["criteria"]
    date_str = datetime.strptime(
        dataset["generated_at"], "%Y-%m-%dT%H:%M:%SZ"
    ).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        f"*Last updated: **{date_str}** — repos with"
        f" >{criteria['min_stars']:,} stars, active in the last"
        f" {criteria['days_back']} days, no AI keywords detected.*",
        "",
        "| # | Repository | ⭐ Stars | Language | Description |",
        "|--:|------------|--------:|----------|-------------|",
    ]
    for repo in dataset["repositories"]:
        description = repo["description"] or "No description provided."
        lines.append(
            f"| {repo['rank']} | [{repo['full_name']}]({repo['url']}) "
            f"| {repo['stars']:,} | {repo['language']} "
            f"| {clean_cell(description)} |"
        )
    return "\n".join(lines)


def splice_markers(readme: str, replacement: str) -> str:
    """Replace the content between the trending markers, idempotently."""
    if START_MARKER not in readme or END_MARKER not in readme:
        raise SystemExit(
            f"Markers {START_MARKER} / {END_MARKER} not found in README"
        )
    head, rest = readme.split(START_MARKER, 1)
    _, tail = rest.split(END_MARKER, 1)
    return head + START_MARKER + "\n" + replacement + "\n" + END_MARKER + tail


def render_readme(dataset: dict, path: str = README_FILE) -> None:
    with open(path, encoding="utf-8") as f:
        readme = f.read()

    updated = splice_markers(readme, render_table(dataset))

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"Updated {path} with {len(dataset['repositories'])} repositories.")


def main() -> None:
    items = fetch_repositories()
    repos = rank_repositories(filter_repositories(normalize_repositories(items)))
    if not repos:
        print("No repositories found; leaving outputs untouched.")
        return
    dataset = build_dataset(repos)
    write_json(dataset)
    render_readme(dataset)


if __name__ == "__main__":
    main()
