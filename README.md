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
*Last updated: **2026-11-12 13:54 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 562,033 | Markdown | Master programming by recreating your favorite technologies from scratch. |
| 2 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 498,424 | Python | A collective list of free APIs |
| 3 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,034 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 4 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,482 | Python | :books: Freely available programming books |
| 5 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 371,895 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 6 | — | [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 364,301 | Unknown | A complete computer science study plan to become a software engineer. |
| 7 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 336,337 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 8 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 334,226 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 9 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,598 | Python | Curated list of project-based tutorials |
| 10 | — | [torvalds/linux](https://github.com/torvalds/linux) | 255,472 | C | Linux kernel source tree |
| 11 | — | [react/react](https://github.com/react/react) | 252,536 | JavaScript | The library for web and native user interfaces. |
| 12 | NEW | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,045 | Python | All Algorithms implemented in Python |
| 13 | ↓ 1 | [ossu/computer-science](https://github.com/ossu/computer-science) | 211,043 | HTML | 🎓 Path to a free self-taught education in Computer Science! |
| 14 | ↓ 1 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 198,693 | Batchfile | Open-source Windows and Office activator featuring HWID, Ohook, TSforge, and Online KMS activation methods, along with advanced troubleshoo… |
| 15 | ↓ 1 | [microsoft/vscode](https://github.com/microsoft/vscode) | 195,323 | TypeScript | Visual Studio Code |
| 16 | ↓ 1 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 193,474 | Go | A curated list of awesome Go frameworks, libraries and software |
| 17 | ↓ 1 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,582 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 18 | ↓ 1 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,500 | JavaScript | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| 19 | ↓ 1 | [flutter/flutter](https://github.com/flutter/flutter) | 181,248 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 20 | ↓ 1 | [github/gitignore](https://github.com/github/gitignore) | 176,251 | Unknown | A collection of useful .gitignore templates |
| 21 | ↓ 1 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175,045 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 22 | ↓ 1 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 157,985 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 23 | ↓ 1 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 154,654 | C | Display and control your Android device |
| 24 | ↓ 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 143,856 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 25 | ↓ 1 | [vercel/next.js](https://github.com/vercel/next.js) | 143,486 | JavaScript | The React Framework |
| 26 | ↓ 1 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 142,681 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 27 | ↓ 1 | [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141,545 | Python | Command-line program to download videos from YouTube.com and other video sites |
| 28 | ↓ 1 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 140,911 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 29 | ↓ 1 | [golang/go](https://github.com/golang/go) | 139,864 | Go | The Go programming language |
| 30 | ↓ 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,556 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 31 | ↓ 1 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,261 | Python | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 32 | ↓ 1 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,490 | JavaScript | Coding articles to level up your development skills |
| 33 | — | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,168 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 34 | ↓ 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,021 | Go | Production-Grade Container Scheduling and Management |
| 35 | ↓ 1 | [react/react-native](https://github.com/react/react-native) | 126,906 | C++ | A framework for building native applications using React |
| 36 | ↓ 1 | [electron/electron](https://github.com/electron/electron) | 123,869 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 37 | ↓ 1 | [nodejs/node](https://github.com/nodejs/node) | 123,516 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 38 | ↓ 1 | [rust-lang/rust](https://github.com/rust-lang/rust) | 121,819 | Rust | Empowering everyone to build reliable and efficient software. |
| 39 | ↓ 1 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 120,470 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 40 | ↓ 1 | [godotengine/godot](https://github.com/godotengine/godot) | 120,022 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 41 | ↓ 1 | [immich-app/immich](https://github.com/immich-app/immich) | 118,977 | TypeScript | High performance self-hosted photo and video management solution. |
| 42 | ↓ 1 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 118,355 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 43 | ↓ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,226 | JavaScript | JavaScript 3D Library. |
| 44 | ↓ 1 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,831 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 45 | ↓ 1 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,790 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 46 | ↓ 1 | [fatedier/frp](https://github.com/fatedier/frp) | 110,557 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 47 | ↓ 1 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 110,452 | Python | Hunt down social media accounts by username across social networks |
| 48 | ↓ 1 | [axios/axios](https://github.com/axios/axios) | 109,395 | JavaScript | Promise based HTTP client for the browser and node.js |
| 49 | ↓ 1 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 107,967 | Unknown | 科技爱好者周刊，每周五发布 |
| 50 | ↓ 1 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,375 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | 78,890 | Rust | 2026-09-30 | PhotoCraft: An open-source photo editor written from scratch in pure Rust |
| 2 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 75,293 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 64,442 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 4 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 53,377 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 5 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 53,327 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 50,186 | C | 2026-07-01 | A hierarchical inference engine for frontier MoE models: hot experts on the GPU (CUDA, Vulkan), warm ones in RAM, cold ones streamed from N… |
| 7 | [block/buzz](https://github.com/block/buzz) | 37,062 | Rust | 2026-03-06 | A hive mind communication platform |
| 8 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 36,574 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 9 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 35,446 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 10 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 34,412 | Swift | 2026-06-12 | Free and open-source macOS menu bar toolkit. |
| 11 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 34,196 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 12 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 33,017 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 498,424 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,482 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 334,226 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,598 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,045 | All Algorithms implemented in Python |
| [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl) | 141,545 | Command-line program to download videos from YouTube.com and other video sites |
| [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,261 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 110,452 | Hunt down social media accounts by username across social networks |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 252,536 | The library for web and native user interfaces. |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,500 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,486 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,490 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 123,516 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,226 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,395 | Promise based HTTP client for the browser and node.js |

### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,034 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 371,895 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 195,323 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 143,856 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,556 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 118,977 | High performance self-hosted photo and video management solution. |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 193,474 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,864 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,021 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,790 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 110,557 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,906 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,869 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 120,022 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,375 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 157,985 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,168 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 121,819 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,831 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
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
