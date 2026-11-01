# 🚫🤖 GitHub Trending, Minus the AI

[![Update trending list](https://github.com/pritam-patil/github-trending-without-ai/actions/workflows/update.yml/badge.svg)](https://github.com/pritam-patil/github-trending-without-ai/actions/workflows/update.yml)
[![License](https://img.shields.io/github/license/pritam-patil/github-trending-without-ai)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/pritam-patil/github-trending-without-ai)](https://github.com/pritam-patil/github-trending-without-ai/stargazers)

**A non-AI view of GitHub Trending.**

Discover **trending open-source repositories, developer tools, libraries,
frameworks, and programming languages** — with AI/LLM-focused repositories
filtered out by a transparent keyword rule, so you can find interesting
tools, languages, and libraries again.

> Daily updates · Open source · MIT
>
> 🌐 **Browse the list on the website:**
> [pritam-patil.github.io/github-trending-without-ai](https://pritam-patil.github.io/github-trending-without-ai/)
> · [RSS feed](https://pritam-patil.github.io/github-trending-without-ai/feed.xml)

## ⭐ What you'll find here

- 🔥 Trending open-source repositories, refreshed every day
- 🧰 Developer tools, libraries, and frameworks
- 🦀 Rust, Go, Python, TypeScript, C++, and more
- 🔍 A transparent, configurable keyword filter — AI-focused repos excluded
- 🤝 Community-tunable: the keyword list lives in one file, open to PRs

## Why?

GitHub Trending currently features a lot of AI- and LLM-focused projects.
That's useful when you're looking for AI — but open source is bigger than
any one topic, and sometimes you just want to see what's happening across
the rest of it.

This project is a daily discovery feed for those days.

## How it works

A daily GitHub Action queries the GitHub Search API for repositories with
**more than 100 stars** that were **pushed to in the last 7 days**, then sets
aside any repo whose name, description, or topics match AI keywords (`ai`,
`llm`, `gpt`, `agent`, `rag`, `langchain`, and friends — matched on word
boundaries, so `email` and `maintain` survive). What's left lands in the
table below. A second query with the same criteria plus a `created:` window
feeds the [New &amp; rising](#-new--rising) section.

## Trending non-AI repositories

<!-- TRENDING:START -->
*Last updated: **2026-11-01 11:56 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 493,979 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458,347 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 400,648 | Python | :books: Freely available programming books |
| 4 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 370,918 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 332,589 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 6 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 331,706 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 7 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 288,637 | Python | Curated list of project-based tutorials |
| 8 | — | [torvalds/linux](https://github.com/torvalds/linux) | 254,025 | C | Linux kernel source tree |
| 9 | — | [react/react](https://github.com/react/react) | 252,064 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 204,359 | Python | A feature-rich command-line audio/video downloader |
| 11 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 194,443 | TypeScript | Visual Studio Code |
| 12 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 191,449 | Go | A curated list of awesome Go frameworks, libraries and software |
| 13 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,281 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 14 | — | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,410 | JavaScript | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| 15 | — | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 186,097 | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| 16 | NEW | [getify/You-Dont-Know-JS](https://github.com/getify/You-Dont-Know-JS) | 184,841 | Unknown | A book series (2 published editions) on the JS language. |
| 17 | ↓ 1 | [flutter/flutter](https://github.com/flutter/flutter) | 180,892 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 18 | ↓ 1 | [github/gitignore](https://github.com/github/gitignore) | 176,128 | Unknown | A collection of useful .gitignore templates |
| 19 | ↓ 1 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,971 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 20 | ↓ 1 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 155,470 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 21 | ↓ 1 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 153,722 | C | Display and control your Android device |
| 22 | ↓ 1 | [vercel/next.js](https://github.com/vercel/next.js) | 143,466 | JavaScript | The React Framework |
| 23 | ↓ 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 142,963 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 24 | ↓ 1 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141,443 | Python | Command-line program to download videos from YouTube.com and other video sites |
| 25 | ↓ 1 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 141,231 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 26 | ↓ 1 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 140,376 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 27 | ↓ 1 | [golang/go](https://github.com/golang/go) | 139,715 | Go | The Go programming language |
| 28 | ↓ 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 134,964 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 29 | ↓ 1 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 131,843 | Swift | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 30 | ↓ 1 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,386 | JavaScript | Coding articles to level up your development skills |
| 31 | ↓ 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,811 | Go | Production-Grade Container Scheduling and Management |
| 32 | ↓ 1 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 127,770 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 33 | ↓ 1 | [react/react-native](https://github.com/react/react-native) | 126,846 | C++ | A framework for building native applications using React |
| 34 | ↓ 1 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 124,289 | Unknown | A collection of various awesome lists for hackers, pentesters and security researchers |
| 35 | ↓ 1 | [electron/electron](https://github.com/electron/electron) | 123,689 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 36 | ↓ 1 | [nodejs/node](https://github.com/nodejs/node) | 123,180 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 37 | ↓ 1 | [rust-lang/rust](https://github.com/rust-lang/rust) | 120,949 | Rust | Empowering everyone to build reliable and efficient software. |
| 38 | ↓ 1 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 119,691 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 39 | ↓ 1 | [godotengine/godot](https://github.com/godotengine/godot) | 119,379 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 40 | ↓ 1 | [immich-app/immich](https://github.com/immich-app/immich) | 117,857 | TypeScript | High performance self-hosted photo and video management solution. |
| 41 | ↓ 1 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 117,515 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 42 | ↓ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 117,338 | JavaScript | JavaScript 3D Library. |
| 43 | ↓ 1 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,396 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 44 | ↓ 1 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,710 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 45 | ↓ 1 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 111,096 | Shell | Papers from the computer science community to read and discuss. |
| 46 | ↓ 1 | [axios/axios](https://github.com/axios/axios) | 109,307 | JavaScript | Promise based HTTP client for the browser and node.js |
| 47 | ↓ 1 | [denoland/deno](https://github.com/denoland/deno) | 108,782 | Rust | A modern runtime for JavaScript and TypeScript. |
| 48 | ↓ 1 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 107,338 | Unknown | 科技爱好者周刊，每周五发布 |
| 49 | ↓ 1 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,302 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | 75,702 | Rust | 2026-09-30 | PhotoCraft: An open-source, photo editor written by scratch in pure Rust |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 61,929 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 3 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 52,588 | Markdown | 2026-03-16 | Skills for Designers and Engineers. |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 51,658 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 5 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 50,245 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 45,467 | C | 2026-07-01 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦 |
| 7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 40,963 | Python | 2026-02-23 | No description provided. |
| 8 | [block/buzz](https://github.com/block/buzz) | 36,651 | Rust | 2026-03-06 | A hive mind communication platform |
| 9 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 36,537 | TypeScript | 2026-02-08 | No description provided. |
| 10 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 34,788 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 11 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33,999 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 12 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 32,748 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 13 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 32,187 | Swift | 2026-06-12 | Free and open-source macOS menu bar toolkit. |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 252,064 | The library for web and native user interfaces. |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,410 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,466 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,386 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 123,180 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 117,338 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,307 | Promise based HTTP client for the browser and node.js |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 493,979 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 400,648 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 331,706 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 288,637 | Curated list of project-based tutorials |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 204,359 | A feature-rich command-line audio/video downloader |
| [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 186,097 | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141,443 | Command-line program to download videos from YouTube.com and other video sites |

### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458,347 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 370,918 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 194,443 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 142,963 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 134,964 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 117,857 | High performance self-hosted photo and video management solution. |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 155,470 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 127,770 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 120,949 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,396 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,782 | A modern runtime for JavaScript and TypeScript. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,846 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,689 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 119,379 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,302 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 191,449 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,715 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,811 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,710 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
<!-- BY_LANGUAGE:END -->

## 🔍 How the filter works

This project does not attempt to determine whether a repository "really is
AI." Instead, it uses transparent keyword matching against:

- repository name
- description
- topics

Keywords are matched on word boundaries (so `ai` never matches `email` or
`maintain`), and the full list is configurable in
[trending.py](trending.py).

This intentionally favors a **simple, reproducible rule** over subjective
classification. That means some AI repos will slip through and some non-AI
repos will be excluded by accident — [open an issue](../../issues) if you
spot either.

## Run it yourself

Requires [uv](https://docs.astral.sh/uv/):

```bash
uv sync
uv run trending.py
```

The script rewrites the table above in place. Authentication is optional but
raises the API rate limit — it uses `GITHUB_TOKEN` if set, otherwise falls
back to the [gh CLI](https://cli.github.com/)'s stored login (`gh auth
token`), otherwise runs anonymously.

Tune `MIN_STARS`, `DAYS_BACK`, and `AI_KEYWORDS` at the top of
[trending.py](trending.py).

To preview the website locally:

```bash
uv run build_site.py
python3 -m http.server 8712 --directory docs
```

then open <http://localhost:8712>. Pass
`--input tests/fixtures/trending.json` to render from the test fixture
without fetching live data.

## Contributing

- **Filter misses** (AI repo in the list) or **false positives** (non-AI repo
  wrongly excluded): open an issue or PR against `AI_KEYWORDS` in
  [trending.py](trending.py).
- Ideas for better trending signals (star velocity, `created:` windows,
  language sections) are welcome.

## License

[MIT](LICENSE)

---

**If you use GitHub Trending and want a non-AI view of open source, give
this repo a ⭐** — it helps other developers find it.

Spot a filter miss? [Open an issue](../../issues).
