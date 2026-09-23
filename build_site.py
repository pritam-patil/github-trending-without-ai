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

# GitHub linguist language colors (used for the dot beside each language).
LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a",
    "Go": "#00ADD8",
    "Rust": "#dea584",
    "C": "#555555",
    "C++": "#f34b7d",
    "C#": "#178600",
    "Java": "#b07219",
    "Shell": "#89e051",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Ruby": "#701516",
    "PHP": "#4F5D95",
    "Swift": "#F05138",
    "Kotlin": "#A97BFF",
    "Dart": "#00B4AB",
    "Vue": "#41b883",
    "Lua": "#000080",
    "Vim Script": "#199f4b",
    "Batchfile": "#C1F12E",
    "MDX": "#fcb32c",
    "Dockerfile": "#384d54",
    "Elixir": "#6e4a7e",
    "Haskell": "#5e5086",
    "Jupyter Notebook": "#DA5B0B",
    "Objective-C": "#438eff",
    "Scala": "#c22d40",
    "PowerShell": "#012456",
    "Makefile": "#427819",
    "Zig": "#ec915c",
}
DEFAULT_LANGUAGE_COLOR = "#8b949e"

# Octicon-style inline SVGs (fill follows the surrounding text color).
ICON_STAR = (
    '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
    '<path fill="currentColor" d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815'
    " 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1"
    "-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818"
    " 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0"
    " 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1"
    " .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53"
    "-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564"
    '-.41L8 2.694Z"></path></svg>'
)
ICON_REPO = (
    '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
    '<path fill="currentColor" d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0'
    " 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h"
    "-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Z"
    "m10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25"
    ".25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45"
    '-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path></svg>'
)
ICON_RSS = (
    '<svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">'
    '<path fill="currentColor" d="M2.002 2.725a.75.75 0 0 1 .797-.699C8.79'
    " 2.42 13.58 7.21 13.973 13.201a.75.75 0 0 1-1.497.098 10.502 10.502 0"
    " 0 0-9.776-9.776.747.747 0 0 1-.698-.798ZM2.84 7.05h-.002a7.002 7.002"
    " 0 0 1 6.113 6.111.75.75 0 0 1-1.49.178 5.503 5.503 0 0 0-4.8-4.8.75"
    '.75 0 0 1 .179-1.489ZM2 13a1 1 0 1 1 2 0 1 1 0 0 1-2 0Z"></path></svg>'
)
ICON_UP = (
    '<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true">'
    '<path fill="currentColor" d="M8 3.5 3.25 8.75h3v4h3.5v-4h3Z"></path></svg>'
)
ICON_DOWN = (
    '<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true">'
    '<path fill="currentColor" d="M8 12.5 3.25 7.25h3V3.5h3.5v3.75h3Z"></path></svg>'
)


def parse_generated_at(dataset: dict) -> datetime:
    return datetime.strptime(
        dataset["generated_at"], "%Y-%m-%dT%H:%M:%SZ"
    ).replace(tzinfo=timezone.utc)


def language_counts(dataset: dict) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for repo in dataset["repositories"]:
        if repo["language"] != "Unknown":
            counts[repo["language"]] = counts.get(repo["language"], 0) + 1
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))


def language_dot(language: str) -> str:
    color = LANGUAGE_COLORS.get(language, DEFAULT_LANGUAGE_COLOR)
    return (
        f'<span class="lang-dot" style="background: {color}"></span>'
        f"{esc(language)}"
    )


def render_change(repo: dict) -> str:
    """Rank movement since the previous update, as a colored indicator."""
    previous = repo["previous_rank"]
    if previous is None:
        return '<span class="change new">NEW</span>'
    delta = previous - repo["rank"]
    if delta > 0:
        return (
            f'<span class="change up">{ICON_UP} up {delta} since'
            " yesterday</span>"
        )
    if delta < 0:
        return (
            f'<span class="change down">{ICON_DOWN} down {-delta} since'
            " yesterday</span>"
        )
    return '<span class="change same">no change</span>'


def repo_title(repo: dict) -> str:
    owner, _, name = repo["full_name"].partition("/")
    return (
        f'<a class="repo-link" href="{esc(repo["url"])}">{esc(owner)} / '
        f"<strong>{esc(name)}</strong></a>"
    )


def render_rows(
    repos: list[dict],
    has_history: bool,
    date_prefix: str = "Active",
    date_field: str = "updated_at",
) -> str:
    rows = []
    for repo in repos:
        description = repo["description"] or "No description provided."
        change = render_change(repo) if has_history else ""
        date_value = repo.get(date_field) or ""
        rows.append(
            f'<article class="row" data-lang="{esc(repo["language"])}">'
            f'<div class="rank">{repo["rank"]}</div>'
            '<div class="row-main">'
            f'<h2 class="row-title"><span class="repo-icon">{ICON_REPO}'
            f"</span>{repo_title(repo)}</h2>"
            f'<p class="desc">{esc(description)}</p>'
            '<div class="meta">'
            f'<span class="meta-item">{language_dot(repo["language"])}</span>'
            f'<span class="meta-item">{ICON_STAR}{repo["stars"]:,}</span>'
            f'<span class="meta-item active-date">{esc(date_prefix)}'
            f" {esc(date_value)}</span>"
            "</div></div>"
            '<div class="row-side">'
            f'<a class="star-btn" href="{esc(repo["url"])}">{ICON_STAR}'
            f" Star</a>{change}</div>"
            "</article>"
        )
    return "\n".join(rows)


def render_language_view(dataset: dict, max_languages: int = 6,
                         max_repos: int = 10) -> str:
    by_language: dict[str, list[dict]] = {}
    for repo in dataset["repositories"]:
        if repo["language"] != "Unknown":
            by_language.setdefault(repo["language"], []).append(repo)
    languages = sorted(
        by_language, key=lambda lang: (-len(by_language[lang]), lang)
    )[:max_languages]

    sections = []
    for language in languages:
        rows = []
        for repo in by_language[language][:max_repos]:
            description = repo["description"] or "No description provided."
            rows.append(
                '<article class="row row-compact">'
                '<div class="row-main">'
                f'<h3 class="row-title">{repo_title(repo)}</h3>'
                f'<p class="desc">{esc(description)}</p>'
                '<div class="meta">'
                f'<span class="meta-item">{ICON_STAR}{repo["stars"]:,}</span>'
                "</div></div></article>"
            )
        sections.append(
            f'<section class="lang-section"><h2 class="lang-heading">'
            f"{language_dot(language)}</h2>\n" + "\n".join(rows) + "</section>"
        )
    return "\n".join(sections)


def render_index(dataset: dict) -> str:
    generated = parse_generated_at(dataset)
    date_long = generated.strftime("%B %-d, %Y")
    criteria = dataset["criteria"]
    repos = dataset["repositories"]
    fresh = dataset.get("fresh_repositories", [])
    has_history = any("previous_rank" in r for r in repos)
    # New projects are the default view; fall back to the full list on a
    # day when nothing created recently meets the criteria.
    default_fresh = bool(fresh)

    options = ['<option value="">Any</option>'] + [
        f'<option value="{esc(lang)}">{esc(lang)} ({count})</option>'
        for lang, count in language_counts(dataset)
    ]
    show_options = (
        f'<option value="new"{" selected" if default_fresh else ""}'
        f'{" disabled" if not fresh else ""}>New — past year'
        f" ({len(fresh)})</option>"
        f'<option value="all"{"" if default_fresh else " selected"}>'
        f"All projects ({len(repos)})</option>"
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
  --bg: #ffffff; --fg: #1f2328; --muted: #59636e; --border: #d0d7de;
  --accent: #0969da; --subtle: #f6f8fa; --btn-border: rgba(31,35,40,0.15);
  --up: #1a7f37; --down: #d1242f;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #0d1117; --fg: #e6edf3; --muted: #8b949e; --border: #30363d;
    --accent: #4493f8; --subtle: #161b22;
    --btn-border: rgba(240,246,252,0.1); --up: #3fb950; --down: #f85149;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans",
    Helvetica, Arial, sans-serif;
}}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
svg {{ vertical-align: text-bottom; }}
.site-header {{
  display: flex; align-items: center; justify-content: space-between;
  gap: 16px; padding: 16px 32px; border-bottom: 1px solid var(--border);
}}
.brand {{ display: flex; align-items: center; gap: 10px; font-size: 16px;
  font-weight: 600; }}
.brand svg {{ display: block; }}
.brand circle, .brand line {{ stroke: var(--fg); }}
.site-nav {{ display: flex; align-items: center; gap: 20px; }}
.nav-link {{ display: inline-flex; align-items: center; gap: 6px;
  color: var(--fg); }}
.nav-link svg {{ color: var(--muted); }}
.btn {{
  display: inline-flex; align-items: center; gap: 6px; padding: 5px 16px;
  font-size: 14px; font-weight: 500; color: var(--fg);
  background: var(--subtle); border: 1px solid var(--btn-border);
  border-radius: 6px;
}}
.btn:hover {{ text-decoration: none; }}
.hero {{
  display: flex; flex-direction: column; align-items: center; gap: 8px;
  padding: 40px 32px; border-bottom: 1px solid var(--border);
  text-align: center;
}}
.hero h1 {{ margin: 0; font-size: 32px; font-weight: 600; }}
.hero .tagline {{ margin: 0; font-size: 16px; color: var(--muted); }}
.hero .criteria {{ margin: 0; font-size: 12px; color: var(--muted); }}
.container {{ max-width: 1280px; margin: 0 auto;
  padding: 40px 32px 24px 32px; }}
.box {{ border: 1px solid var(--border); border-radius: 6px; }}
.toolbar {{
  display: flex; align-items: center; justify-content: space-between;
  flex-wrap: wrap; gap: 12px; padding: 16px; background: var(--subtle);
  border-bottom: 1px solid var(--border); border-radius: 6px 6px 0 0;
}}
.segmented {{ display: flex; align-items: center;
  border: 1px solid var(--btn-border); border-radius: 6px; }}
.segment {{ padding: 5px 16px; font-size: 14px; color: var(--fg);
  background: none; border: none; font-family: inherit; cursor: pointer; }}
.segment + .segment {{ border-left: 1px solid var(--btn-border); }}
.segment.active {{ font-weight: 600; color: #ffffff;
  background: var(--accent); border-radius: 5px 0 0 5px; }}
.segment.active:last-child {{ border-radius: 0 5px 5px 0; }}
.toolbar-filters {{ display: flex; align-items: center; gap: 24px;
  font-size: 14px; color: var(--muted); }}
.toolbar-filters label {{ display: inline-flex; align-items: center;
  gap: 6px; }}
.toolbar-filters select {{
  font: inherit; font-weight: 600; color: var(--fg); background: var(--subtle);
  border: none; cursor: pointer;
}}
.row {{ display: flex; align-items: flex-start; gap: 16px;
  padding: 16px 24px; }}
.row + .row, .row + .lang-section, .lang-section .row {{
  border-top: 1px solid var(--border); }}
.rank {{ width: 24px; padding-top: 3px; font-size: 14px;
  color: var(--muted); text-align: right; flex-shrink: 0;
  font-variant-numeric: tabular-nums; }}
.row-main {{ display: flex; flex-direction: column; gap: 6px;
  flex-grow: 1; min-width: 0; }}
.row-title {{ margin: 0; font-size: 20px; font-weight: 400;
  display: flex; align-items: center; gap: 8px; }}
.row-compact .row-title {{ font-size: 16px; }}
.repo-icon {{ color: var(--muted); display: inline-flex; }}
.repo-link strong {{ font-weight: 600; }}
.desc {{ margin: 0; color: var(--muted); max-width: 760px; }}
.meta {{ display: flex; align-items: center; flex-wrap: wrap; gap: 16px;
  font-size: 12px; color: var(--muted); }}
.meta-item {{ display: inline-flex; align-items: center; gap: 5px; }}
.lang-dot {{ width: 12px; height: 12px; border-radius: 50%;
  display: inline-block; }}
.row-side {{ display: flex; flex-direction: column;
  align-items: flex-end; gap: 8px; flex-shrink: 0; }}
.star-btn {{
  display: inline-flex; align-items: center; gap: 6px; padding: 3px 12px;
  font-size: 12px; font-weight: 500; color: var(--fg);
  background: var(--subtle); border: 1px solid var(--btn-border);
  border-radius: 6px;
}}
.star-btn svg {{ color: var(--muted); }}
.star-btn:hover {{ text-decoration: none; border-color: var(--muted); }}
.change {{ display: inline-flex; align-items: center; gap: 4px;
  font-size: 12px; }}
.change.up {{ color: var(--up); }}
.change.down {{ color: var(--down); }}
.change.new {{ color: var(--accent); font-weight: 600; }}
.change.same {{ color: var(--muted); }}
.lang-section {{ padding: 0; }}
.lang-heading {{ margin: 0; padding: 16px 24px 0 24px; font-size: 16px;
  display: flex; align-items: center; gap: 8px; }}
.box-footer {{
  display: flex; justify-content: center; gap: 16px; padding: 16px;
  border-top: 1px solid var(--border); background: var(--subtle);
  border-radius: 0 0 6px 6px; font-size: 14px;
}}
.site-footer {{
  display: flex; flex-direction: column; align-items: center; gap: 6px;
  padding: 24px 32px 40px 32px; font-size: 12px; color: var(--muted);
  text-align: center;
}}
.site-footer p {{ margin: 0; }}
[hidden] {{ display: none !important; }}
@media (max-width: 767px) {{
  .site-header {{ padding: 14px 16px; }}
  .site-nav .btn {{ display: none; }}
  .hero {{ padding: 20px 16px; align-items: flex-start; text-align: left; }}
  .hero h1 {{ font-size: 22px; }}
  .hero .tagline {{ font-size: 14px; }}
  .container {{ padding: 0; }}
  .box {{ border-left: none; border-right: none; border-radius: 0; }}
  .toolbar {{ border-radius: 0; }}
  .row {{ padding: 14px 16px; gap: 10px; }}
  .row-title {{ font-size: 16px; }}
  .repo-icon, .star-btn, .active-date {{ display: none; }}
  .row-side {{ padding-top: 2px; }}
  .change {{ white-space: nowrap; }}
}}
</style>
</head>
<body>
<header class="site-header">
<div class="brand">
<svg width="24" height="24" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="9" stroke-width="2"></circle><line x1="6" y1="18" x2="18" y2="6" stroke-width="2"></line></svg>
Trending, Minus the AI
</div>
<nav class="site-nav">
<a class="nav-link" href="feed.xml">{ICON_RSS} RSS</a>
<a class="btn" href="{REPO_URL}">{ICON_REPO} View source</a>
</nav>
</header>

<section class="hero">
<h1>Trending, minus the AI</h1>
<p class="tagline">See what the open-source community is building right now
— with AI-focused repositories filtered out by a transparent keyword
rule.</p>
<p class="criteria">Updated daily · {esc(date_long)} ·
{criteria["min_stars"]}+ stars · active within {criteria["days_back"]} days
· AI-focused repositories filtered using
<a href="{REPO_URL}#-how-the-filter-works">keyword matching</a></p>
</section>

<main class="container">
<div class="box">
<div class="toolbar">
<div class="segmented" id="tabs">
<button class="segment active" type="button" data-view="repos">Repositories</button>
<button class="segment" type="button" data-view="langs">By language</button>
</div>
<div class="toolbar-filters">
<label for="show-filter">Show:
<select id="show-filter">
{show_options}
</select></label>
<label for="lang-filter">Language:
<select id="lang-filter">
{"".join(options)}
</select></label>
</div>
</div>

<div id="view-fresh"{"" if default_fresh else " hidden"}>
{render_rows(fresh, False, date_prefix="Created", date_field="created_at")}
</div>

<div id="view-repos"{" hidden" if default_fresh else ""}>
{render_rows(repos, has_history)}
</div>

<div id="view-langs" hidden>
{render_language_view(dataset)}
</div>

<div class="box-footer">
<span>{len(fresh)} new · {len(repos)} total today</span>
<a href="data/trending.json">Data (JSON)</a>
</div>
</div>
</main>

<footer class="site-footer">
<p>A transparent keyword filter, not a judgment call — the keyword list is
one file, open to pull requests.</p>
<p>Open-source engine:
<a href="{REPO_URL}">pritam-patil/github-trending-without-ai</a>
· <a href="{REPO_URL}/blob/main/LICENSE">MIT</a></p>
</footer>

<script>
(function () {{
  var tabs = document.getElementById("tabs");
  var viewFresh = document.getElementById("view-fresh");
  var viewRepos = document.getElementById("view-repos");
  var viewLangs = document.getElementById("view-langs");
  var filter = document.getElementById("lang-filter");
  var show = document.getElementById("show-filter");
  var onLangsTab = false;

  function syncViews() {{
    var fresh = show.value === "new";
    viewLangs.hidden = !onLangsTab;
    viewFresh.hidden = onLangsTab || !fresh;
    viewRepos.hidden = onLangsTab || fresh;
    show.disabled = onLangsTab;
    filter.disabled = onLangsTab;
  }}

  tabs.addEventListener("click", function (e) {{
    var button = e.target.closest(".segment");
    if (!button) return;
    tabs.querySelectorAll(".segment").forEach(function (b) {{
      b.classList.toggle("active", b === button);
    }});
    onLangsTab = button.dataset.view === "langs";
    syncViews();
  }});

  show.addEventListener("change", syncViews);

  filter.addEventListener("change", function () {{
    var lang = filter.value;
    document.querySelectorAll(
      "#view-fresh .row, #view-repos .row"
    ).forEach(function (row) {{
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
