"""Render the canonical dataset into the static website and RSS feed.

Pure renderer: JSON in, HTML/XML out. It never calls GitHub, so the whole
site can be rebuilt offline from any historical dataset:

    uv run build_site.py --input tests/fixtures/trending.json
"""

import argparse
import html
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_INPUT = "data/trending.json"
DEFAULT_OUT_DIR = "docs"
SITE_URL = "https://pritam-patil.github.io/github-trending-without-ai"
REPO_URL = "https://github.com/pritam-patil/github-trending-without-ai"

esc = html.escape


def parse_generated_at(dataset: dict) -> datetime:
    return datetime.strptime(
        dataset["generated_at"], "%Y-%m-%dT%H:%M:%SZ"
    ).replace(tzinfo=timezone.utc)


def format_rank_change(repo: dict) -> str | None:
    """Positions moved in the primary ranking; None when no history exists."""
    if "previous_rank" not in repo:
        return None
    previous = repo["previous_rank"]
    if previous is None:
        return "NEW"
    delta = previous - repo["rank"]
    if delta > 0:
        return f"↑ {delta}"
    if delta < 0:
        return f"↓ {-delta}"
    return "—"


def language_counts(dataset: dict) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for repo in dataset["repositories"]:
        if repo["language"] != "Unknown":
            counts[repo["language"]] = counts.get(repo["language"], 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


def render_rows(dataset: dict, has_history: bool) -> str:
    rows = []
    for repo in dataset["repositories"]:
        description = repo["description"] or "No description provided."
        change = ""
        if has_history:
            label = format_rank_change(repo) or ""
            klass = (
                "new" if label == "NEW"
                else "up" if label.startswith("↑")
                else "down" if label.startswith("↓")
                else "same"
            )
            change = f'<td class="change {klass}">{esc(label)}</td>'
        rows.append(
            f'<tr data-lang="{esc(repo["language"])}">'
            f'<td class="rank">{repo["rank"]}</td>{change}'
            f'<td><a href="{esc(repo["url"])}">{esc(repo["full_name"])}</a>'
            f'<span class="desc">{esc(description)}</span></td>'
            f'<td class="stars">{repo["stars"]:,}</td>'
            f'<td class="lang">{esc(repo["language"])}</td>'
            "</tr>"
        )
    return "\n".join(rows)


def render_index(dataset: dict) -> str:
    generated = parse_generated_at(dataset)
    date_long = generated.strftime("%B %-d, %Y")
    criteria = dataset["criteria"]
    repos = dataset["repositories"]
    has_history = any("previous_rank" in r for r in repos)

    chips = "\n".join(
        f'<button class="chip" data-lang="{esc(lang)}">{esc(lang)}'
        f' <span>{count}</span></button>'
        for lang, count in language_counts(dataset)
    )
    change_head = '<th class="change">Change</th>' if has_history else ""
    change_note = (
        "<p class=\"note\">Change = positions moved in this list since the"
        " previous update; NEW = not in the previous update.</p>"
        if has_history
        else ""
    )

    title = (
        f"{len(repos)} open-source projects trending on GitHub today"
        " — minus AI-focused repos"
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="A non-AI view of GitHub Trending — discover open-source tools, libraries, languages, and projects trending right now.">
<link rel="alternate" type="application/rss+xml" title="GitHub Trending, Minus the AI" href="feed.xml">
<style>
:root {{
  color-scheme: light dark;
  --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --line: #d1d9e0;
  --accent: #0969da; --chip: #f6f8fa; --up: #1a7f37; --down: #cf222e;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #0d1117; --fg: #e6edf3; --muted: #8d96a0; --line: #30363d;
    --accent: #4493f8; --chip: #161b22; --up: #3fb950; --down: #f85149;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font: 15px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica,
    Arial, sans-serif;
}}
main {{ max-width: 900px; margin: 0 auto; padding: 2rem 1rem 4rem; }}
h1 {{ font-size: 1.6rem; margin: 0 0 .25rem; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
.updated {{ font-weight: 600; }}
.meta, .note {{ color: var(--muted); font-size: .85rem; }}
.chips {{ display: flex; flex-wrap: wrap; gap: .4rem; margin: 1.25rem 0; }}
.chip {{
  border: 1px solid var(--line); background: var(--chip); color: var(--fg);
  border-radius: 999px; padding: .25rem .75rem; font-size: .82rem;
  cursor: pointer;
}}
.chip span {{ color: var(--muted); }}
.chip.active {{ border-color: var(--accent); color: var(--accent); }}
.table-wrap {{ overflow-x: auto; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{
  padding: .5rem .6rem; border-bottom: 1px solid var(--line);
  text-align: left; vertical-align: top;
}}
th {{ font-size: .8rem; color: var(--muted); text-transform: uppercase; }}
.rank, .stars {{ text-align: right; font-variant-numeric: tabular-nums; }}
.change {{ text-align: center; white-space: nowrap; font-size: .82rem; }}
.change.up {{ color: var(--up); }}
.change.down {{ color: var(--down); }}
.change.new {{ color: var(--accent); font-weight: 600; }}
.desc {{ display: block; color: var(--muted); font-size: .85rem; }}
.lang {{ white-space: nowrap; }}
footer {{
  margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--line);
  color: var(--muted); font-size: .85rem;
}}
</style>
</head>
<body>
<main>
<h1>🚫🤖 GitHub Trending, Minus the AI</h1>
<p><span class="updated">Updated daily · {esc(date_long)}</span><br>
A non-AI view of GitHub Trending — discover open-source tools, libraries,
languages, and projects trending right now.</p>
<p class="meta">{criteria["min_stars"]}+ stars · active within
{criteria["days_back"]} days · AI-focused repositories filtered using
keyword matching · <a href="{REPO_URL}#-how-the-filter-works">methodology</a>
· <a href="feed.xml">RSS</a></p>

<div class="chips" hidden id="chips">
<button class="chip active" data-lang="">All languages</button>
{chips}
</div>

<h2>Trending today</h2>
<div class="table-wrap">
<table id="trending">
<thead><tr><th class="rank">#</th>{change_head}<th>Repository</th>
<th class="stars">⭐ Stars</th><th>Language</th></tr></thead>
<tbody>
{render_rows(dataset, has_history)}
</tbody>
</table>
</div>
{change_note}

<h2>How it works</h2>
<p>A daily GitHub Action queries the GitHub Search API for repositories
with more than {criteria["min_stars"]} stars that were pushed to in the
last {criteria["days_back"]} days, then sets aside any repo whose name,
description, or topics match a transparent, configurable list of AI
keywords — matched on word boundaries, so <code>email</code> and
<code>maintain</code> survive. It's a simple, reproducible rule, not a
judgment call.</p>

<footer>
<p>Open-source engine: <a href="{REPO_URL}">{esc("pritam-patil/github-trending-without-ai")}</a>
— spot a filter miss? <a href="{REPO_URL}/issues">Open an issue</a>.<br>
Data: <a href="data/trending.json">trending.json</a> · MIT licensed.</p>
</footer>
</main>
<script>
(function () {{
  var chips = document.getElementById("chips");
  chips.hidden = false;
  chips.addEventListener("click", function (e) {{
    var chip = e.target.closest(".chip");
    if (!chip) return;
    chips.querySelectorAll(".chip").forEach(function (c) {{
      c.classList.toggle("active", c === chip);
    }});
    var lang = chip.dataset.lang;
    document.querySelectorAll("#trending tbody tr").forEach(function (row) {{
      row.hidden = Boolean(lang) && row.dataset.lang !== lang;
    }});
  }});
}})();
</script>
</body>
</html>
"""


def render_feed(dataset: dict, top_n: int = 10) -> str:
    """RSS 2.0 daily digest: one item per daily edition, not per repo."""
    generated = parse_generated_at(dataset)
    date_long = generated.strftime("%B %-d, %Y")
    pub_date = generated.strftime("%a, %d %b %Y %H:%M:%S +0000")
    repos = dataset["repositories"]

    highlights = "".join(
        f"<li><a href=\"{esc(r['url'])}\">{esc(r['full_name'])}</a>"
        f" ({r['stars']:,} ⭐) — "
        f"{esc(r['description'] or 'No description provided.')}</li>"
        for r in repos[:top_n]
    )
    summary = esc(
        f"<p>Today's {len(repos)} trending open-source repositories,"
        f" with AI-focused projects filtered out. Highlights:</p>"
        f"<ol>{highlights}</ol>"
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
<title>GitHub Trending, Minus the AI</title>
<link>{SITE_URL}/</link>
<description>A non-AI view of GitHub Trending — a daily digest of open-source tools, libraries, languages, and projects trending right now.</description>
<language>en</language>
<lastBuildDate>{pub_date}</lastBuildDate>
<item>
<title>GitHub Trending, Minus the AI — {esc(date_long)}</title>
<link>{SITE_URL}/</link>
<guid isPermaLink="false">{SITE_URL}/#{generated.strftime("%Y-%m-%d")}</guid>
<pubDate>{pub_date}</pubDate>
<description>{summary}</description>
</item>
</channel>
</rss>
"""


def build(input_path: str, out_dir: str) -> None:
    with open(input_path, encoding="utf-8") as f:
        dataset = json.load(f)

    out = Path(out_dir)
    (out / "data").mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(render_index(dataset), encoding="utf-8")
    (out / "feed.xml").write_text(render_feed(dataset), encoding="utf-8")
    shutil.copyfile(input_path, out / "data" / "trending.json")
    print(
        f"Built site for {len(dataset['repositories'])} repositories"
        f" in {out_dir}/."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    args = parser.parse_args()
    build(args.input, args.out_dir)


if __name__ == "__main__":
    main()
