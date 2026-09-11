# trending-non-ai

Fetches popular, recently-active GitHub repositories, filters out AI/LLM
projects by keyword, and writes the rest to a markdown report
(`trending_non_ai_repos.md`).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
```

## Usage

```bash
uv run trending.py
```

Authentication raises the GitHub API rate limit (unauthenticated search is
capped at 10 requests/minute). The script picks up credentials automatically,
in this order:

1. A `GITHUB_TOKEN` environment variable, if set
2. The [gh CLI](https://cli.github.com/)'s stored login (`gh auth token`),
   if `gh` is installed and you've run `gh auth login`

With neither, it still works on the anonymous rate limit.

## Configuration

Edit the constants at the top of `trending.py`:

- `MIN_STARS` — minimum stars to consider a repo popular (default 100)
- `DAYS_BACK` — how recently a repo must have been pushed to (default 7 days)
- `AI_KEYWORDS` — keywords (matched on word boundaries against name,
  description, and topics) that exclude a repo
