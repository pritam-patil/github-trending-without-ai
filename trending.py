"""Fetch popular, recently-active GitHub repos and filter out AI/LLM projects."""

import os
import re
import shutil
import subprocess
from datetime import datetime, timedelta, timezone

import requests

# 1. Configuration & Filtering Layout
MIN_STARS = 100  # Minimum stars to consider a repo popular
DAYS_BACK = 7  # Look at repos active in the last X days
OUTPUT_FILE = "trending_non_ai_repos.md"

# Keywords used to identify and exclude AI/LLM bloat.
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
]

AI_PATTERN = re.compile(
    r"\b(?:" + "|".join(re.escape(k) for k in AI_KEYWORDS) + r")\b",
    re.IGNORECASE,
)


def is_ai_repo(repo: dict) -> bool:
    """Check the repo's name, description, and topics for AI keywords."""
    haystack = " ".join(
        [
            repo["name"],
            repo["description"] or "",
            " ".join(repo.get("topics", [])),
        ]
    )
    return AI_PATTERN.search(haystack) is not None


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


def fetch_non_ai_repos() -> list[dict]:
    # Calculate the date boundary for active repositories
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

    items = response.json().get("items", [])

    filtered_repos = [
        {
            "name": repo["full_name"],
            "url": repo["html_url"],
            "description": repo["description"] or "No description provided.",
            "stars": repo["stargazers_count"],
            "language": repo["language"] or "Unknown",
            "updated_at": repo["pushed_at"][:10],
        }
        for repo in items
        if not is_ai_repo(repo)
    ]

    return filtered_repos


def generate_markdown(repos: list[dict]) -> None:
    if not repos:
        print("No repositories found matching the criteria.")
        return

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Non-AI GitHub Trending Repositories\n")
        f.write(f"*Generated on {date_str} (Looking back {DAYS_BACK} days)*\n\n")

        for idx, repo in enumerate(repos, start=1):
            f.write(f"### {idx}. [{repo['name']}]({repo['url']})\n")
            f.write(f"- **⭐ Stars:** {repo['stars']:,}\n")
            f.write(f"- **💻 Language:** {repo['language']}\n")
            f.write(f"- **📅 Last Active:** {repo['updated_at']}\n")
            f.write(f"- **📝 Description:** {repo['description']}\n\n")
            f.write("---\n\n")

    print(f"Successfully saved {len(repos)} repositories to {OUTPUT_FILE}")


if __name__ == "__main__":
    repositories = fetch_non_ai_repos()
    generate_markdown(repositories)
