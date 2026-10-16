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
*Last updated: **2026-10-16 10:01 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 489,271 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 457,147 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 399,173 | Python | :books: Freely available programming books |
| 4 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 369,517 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 327,802 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 6 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 327,107 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 7 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 286,854 | Python | Curated list of project-based tutorials |
| 8 | — | [torvalds/linux](https://github.com/torvalds/linux) | 252,106 | C | Linux kernel source tree |
| 9 | — | [react/react](https://github.com/react/react) | 251,152 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,306 | Python | All Algorithms implemented in Python |
| 11 | — | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 198,308 | Python | A feature-rich command-line audio/video downloader |
| 12 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 193,743 | TypeScript | Visual Studio Code |
| 13 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,043 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 14 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 188,676 | Go | A curated list of awesome Go frameworks, libraries and software |
| 15 | — | [flutter/flutter](https://github.com/flutter/flutter) | 180,234 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 16 | — | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,921 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 17 | — | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 152,289 | C | Display and control your Android device |
| 18 | — | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 151,773 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 19 | — | [vercel/next.js](https://github.com/vercel/next.js) | 143,035 | JavaScript | The React Framework |
| 20 | — | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 141,056 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 21 | — | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 139,631 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 22 | — | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 139,371 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 23 | — | [golang/go](https://github.com/golang/go) | 139,277 | Go | The Go programming language |
| 24 | — | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,962 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 25 | — | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 130,771 | Java | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 26 | — | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,313 | Go | Production-Grade Container Scheduling and Management |
| 27 | — | [react/react-native](https://github.com/react/react-native) | 126,690 | C++ | A framework for building native applications using React |
| 28 | — | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,982 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 29 | — | [electron/electron](https://github.com/electron/electron) | 123,353 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 30 | — | [nodejs/node](https://github.com/nodejs/node) | 122,382 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 31 | — | [rust-lang/rust](https://github.com/rust-lang/rust) | 120,407 | Rust | Empowering everyone to build reliable and efficient software. |
| 32 | — | [godotengine/godot](https://github.com/godotengine/godot) | 118,494 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 33 | — | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 118,349 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 34 | — | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,483 | JavaScript | JavaScript 3D Library. |
| 35 | — | [immich-app/immich](https://github.com/immich-app/immich) | 116,390 | TypeScript | High performance self-hosted photo and video management solution. |
| 36 | — | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 116,268 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 37 | — | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,941 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 38 | — | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,495 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 39 | — | [fatedier/frp](https://github.com/fatedier/frp) | 109,944 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 40 | — | [axios/axios](https://github.com/axios/axios) | 109,301 | JavaScript | Promise based HTTP client for the browser and node.js |
| 41 | — | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 106,275 | Unknown | 科技爱好者周刊，每周五发布 |
| 42 | — | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,178 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 43 | — | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 103,129 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 44 | — | [neovim/neovim](https://github.com/neovim/neovim) | 102,999 | Vim Script | Vim-fork focused on extensibility and usability |
| 45 | — | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 102,834 | Unknown | Programmer's guide about how to cook at home. |
| 46 | — | [angular/angular](https://github.com/angular/angular) | 101,062 | TypeScript | Deliver web apps with confidence 🚀 |
| 47 | — | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,787 | TypeScript | An enterprise-class UI design language and React UI library |
| 48 | — | [mui/material-ui](https://github.com/mui/material-ui) | 99,226 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 49 | — | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 97,881 | TypeScript | A utility-first CSS framework for rapid UI development. |
| 50 | — | [microsoft/playwright](https://github.com/microsoft/playwright) | 97,835 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 64,275 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 2 | [storytold/photocraft](https://github.com/storytold/photocraft) | 64,077 | Rust | 2026-09-30 | PhotoCraft: An open-source, photo editor written by scratch in pure Rust |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 57,058 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 4 | [chenglou/pretext](https://github.com/chenglou/pretext) | 50,806 | TypeScript | 2026-03-07 | Fast, accurate & comprehensive text measurement & layout |
| 5 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 48,640 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 6 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 46,584 | Markdown | 2026-03-16 | Skills for Designers and Engineers. |
| 7 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 42,284 | C | 2026-07-01 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦 |
| 8 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 39,187 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 9 | [block/buzz](https://github.com/block/buzz) | 36,036 | Rust | 2026-03-06 | A hive mind communication platform |
| 10 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 34,633 | Python | 2026-04-05 | 你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks. |
| 11 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 33,936 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 12 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33,651 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 13 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 33,107 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 14 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 32,281 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 15 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | 32,236 | Rust | 2026-05-06 | An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable 一个CodexApp的增强工具，努力让Codex变得更好用更舒服 |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 457,147 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 369,517 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 193,743 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 141,056 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,962 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 116,390 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,062 | Deliver web apps with confidence 🚀 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,787 | An enterprise-class UI design language and React UI library |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 97,881 | A utility-first CSS framework for rapid UI development. |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 97,835 | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 489,271 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 399,173 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 327,802 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 286,854 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,306 | All Algorithms implemented in Python |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 198,308 | A feature-rich command-line audio/video downloader |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 103,129 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 251,152 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,035 | The React Framework |
| [nodejs/node](https://github.com/nodejs/node) | 122,382 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,483 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,301 | Promise based HTTP client for the browser and node.js |
| [mui/material-ui](https://github.com/mui/material-ui) | 99,226 | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 188,676 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,277 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,313 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,495 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 109,944 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,690 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,353 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 118,494 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,178 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 151,773 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,982 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 120,407 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,941 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
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
