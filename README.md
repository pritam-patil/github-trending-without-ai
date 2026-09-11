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

Optionally set a GitHub token to raise the API rate limit (unauthenticated
search is capped at 10 requests/minute):

```bash
GITHUB_TOKEN=ghp_... uv run trending.py
```

## Configuration

Edit the constants at the top of `trending.py`:

- `MIN_STARS` — minimum stars to consider a repo popular (default 100)
- `DAYS_BACK` — how recently a repo must have been pushed to (default 7 days)
- `AI_KEYWORDS` — keywords (matched on word boundaries against name,
  description, and topics) that exclude a repo
