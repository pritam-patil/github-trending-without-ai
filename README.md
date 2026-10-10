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
*Last updated: **2026-10-10 11:17 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 487,117 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,809 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 398,645 | Python | :books: Freely available programming books |
| 4 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 369,076 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 326,260 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 6 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 325,107 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 7 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 286,253 | Python | Curated list of project-based tutorials |
| 8 | — | [torvalds/linux](https://github.com/torvalds/linux) | 251,418 | C | Linux kernel source tree |
| 9 | — | [react/react](https://github.com/react/react) | 250,811 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,143 | Python | All Algorithms implemented in Python |
| 11 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 193,515 | TypeScript | Visual Studio Code |
| 12 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,063 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 13 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 187,650 | Go | A curated list of awesome Go frameworks, libraries and software |
| 14 | — | [flutter/flutter](https://github.com/flutter/flutter) | 179,273 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 15 | — | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,804 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 16 | — | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 151,748 | C | Display and control your Android device |
| 17 | — | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 150,292 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 18 | — | [vercel/next.js](https://github.com/vercel/next.js) | 143,101 | JavaScript | The React Framework |
| 19 | — | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 140,456 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 20 | — | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 139,293 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 21 | — | [golang/go](https://github.com/golang/go) | 139,172 | Go | The Go programming language |
| 22 | — | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 139,158 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 23 | — | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,593 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 24 | NEW | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 130,505 | Java | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 25 | ↓ 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,241 | Go | Production-Grade Container Scheduling and Management |
| 26 | ↓ 1 | [react/react-native](https://github.com/react/react-native) | 126,615 | C++ | A framework for building native applications using React |
| 27 | ↓ 1 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,373 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 28 | ↓ 1 | [electron/electron](https://github.com/electron/electron) | 123,259 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 29 | ↓ 1 | [nodejs/node](https://github.com/nodejs/node) | 122,265 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 30 | ↓ 1 | [rust-lang/rust](https://github.com/rust-lang/rust) | 119,631 | Rust | Empowering everyone to build reliable and efficient software. |
| 31 | ↓ 1 | [godotengine/godot](https://github.com/godotengine/godot) | 118,210 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 32 | ↓ 1 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 117,762 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 33 | ↓ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,195 | JavaScript | JavaScript 3D Library. |
| 34 | ↓ 1 | [immich-app/immich](https://github.com/immich-app/immich) | 115,909 | TypeScript | High performance self-hosted photo and video management solution. |
| 35 | ↓ 1 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 115,735 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 36 | ↓ 1 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,721 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 37 | ↓ 1 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,375 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 38 | ↓ 1 | [fatedier/frp](https://github.com/fatedier/frp) | 109,811 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 39 | ↓ 1 | [axios/axios](https://github.com/axios/axios) | 109,346 | JavaScript | Promise based HTTP client for the browser and node.js |
| 40 | ↓ 1 | [denoland/deno](https://github.com/denoland/deno) | 108,721 | Rust | A modern runtime for JavaScript and TypeScript. |
| 41 | ↓ 1 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 105,691 | Unknown | 科技爱好者周刊，每周五发布 |
| 42 | ↓ 1 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,122 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 43 | — | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,962 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 44 | ↓ 2 | [neovim/neovim](https://github.com/neovim/neovim) | 102,962 | Vim Script | Vim-fork focused on extensibility and usability |
| 45 | ↓ 1 | [angular/angular](https://github.com/angular/angular) | 101,024 | TypeScript | Deliver web apps with confidence 🚀 |
| 46 | ↓ 1 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,730 | TypeScript | An enterprise-class UI design language and React UI library |
| 47 | ↓ 1 | [mui/material-ui](https://github.com/mui/material-ui) | 99,157 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 48 | NEW | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 97,852 | TypeScript | A utility-first CSS framework for rapid UI development. |
| 49 | ↓ 2 | [microsoft/playwright](https://github.com/microsoft/playwright) | 97,411 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |
| 50 | ↓ 2 | [oven-sh/bun](https://github.com/oven-sh/bun) | 96,169 | Rust | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| 51 | ↓ 2 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 95,673 | TypeScript | JavaScript API for Chrome and Firefox |
| 52 | ↓ 2 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 95,294 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions. |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 58,190 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 2 | [chenglou/pretext](https://github.com/chenglou/pretext) | 50,730 | TypeScript | 2026-03-07 | Fast, accurate & comprehensive text measurement & layout |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 49,838 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 47,077 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 40,912 | C | 2026-07-01 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦 |
| 6 | [block/buzz](https://github.com/block/buzz) | 35,803 | Rust | 2026-03-06 | A hive mind communication platform |
| 7 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33,560 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 8 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 33,010 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 9 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 32,078 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 10 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 32,050 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 11 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | 31,968 | Rust | 2026-05-06 | An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable 一个CodexApp的增强工具，努力让Codex变得更好用更舒服 |
| 12 | [tobi/qmd](https://github.com/tobi/qmd) | 30,309 | TypeScript | 2025-12-08 | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
| 13 | [sipeed/picoclaw](https://github.com/sipeed/picoclaw) | 30,016 | Go | 2026-02-04 | Tiny, Fast, and Deployable anywhere — automate the mundane, unleash your creativity |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,809 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 369,076 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 193,515 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 140,456 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,593 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 115,909 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,024 | Deliver web apps with confidence 🚀 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,730 | An enterprise-class UI design language and React UI library |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 97,852 | A utility-first CSS framework for rapid UI development. |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 97,411 | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 250,811 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,101 | The React Framework |
| [nodejs/node](https://github.com/nodejs/node) | 122,265 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,195 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,346 | Promise based HTTP client for the browser and node.js |
| [mui/material-ui](https://github.com/mui/material-ui) | 99,157 | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 487,117 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 398,645 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 326,260 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 286,253 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,143 | All Algorithms implemented in Python |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,962 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 150,292 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,373 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 119,631 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,721 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,721 | A modern runtime for JavaScript and TypeScript. |
| [oven-sh/bun](https://github.com/oven-sh/bun) | 96,169 | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 187,650 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,172 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,241 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,375 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 109,811 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,615 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,259 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 118,210 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,122 | The new Windows Terminal and the original Windows console host, all in the same place! |
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
