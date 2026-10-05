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
*Last updated: **2026-10-05 12:27 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 486,167 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,771 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 398,506 | Python | :books: Freely available programming books |
| 4 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 368,908 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 325,295 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 6 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 324,010 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 7 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 285,879 | Python | Curated list of project-based tutorials |
| 8 | — | [torvalds/linux](https://github.com/torvalds/linux) | 251,146 | C | Linux kernel source tree |
| 9 | — | [react/react](https://github.com/react/react) | 250,901 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,241 | Python | All Algorithms implemented in Python |
| 11 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 193,525 | TypeScript | Visual Studio Code |
| 12 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,155 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 13 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 187,033 | Go | A curated list of awesome Go frameworks, libraries and software |
| 14 | ↑ 1 | [flutter/flutter](https://github.com/flutter/flutter) | 179,346 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 15 | ↑ 1 | [github/gitignore](https://github.com/github/gitignore) | 176,026 | Unknown | A collection of useful .gitignore templates |
| 16 | ↑ 1 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,989 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 17 | ↑ 1 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 151,039 | C | Display and control your Android device |
| 18 | ↑ 1 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 149,312 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 19 | ↑ 1 | [vercel/next.js](https://github.com/vercel/next.js) | 143,187 | JavaScript | The React Framework |
| 20 | ↑ 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 140,341 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 21 | ↑ 2 | [golang/go](https://github.com/golang/go) | 139,252 | Go | The Go programming language |
| 22 | — | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 139,233 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 23 | ↑ 1 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 139,203 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 24 | ↑ 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,532 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 25 | ↑ 1 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,317 | JavaScript | Coding articles to level up your development skills |
| 26 | ↑ 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,294 | Go | Production-Grade Container Scheduling and Management |
| 27 | ↑ 1 | [react/react-native](https://github.com/react/react-native) | 126,795 | C++ | A framework for building native applications using React |
| 28 | ↑ 1 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,164 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 29 | ↑ 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 125,133 | TypeScript | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| 30 | ↑ 1 | [electron/electron](https://github.com/electron/electron) | 123,389 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 31 | ↑ 1 | [nodejs/node](https://github.com/nodejs/node) | 122,350 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 32 | ↑ 1 | [rust-lang/rust](https://github.com/rust-lang/rust) | 119,570 | Rust | Empowering everyone to build reliable and efficient software. |
| 33 | ↑ 1 | [godotengine/godot](https://github.com/godotengine/godot) | 118,139 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 34 | ↑ 1 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 117,644 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 35 | ↑ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,242 | JavaScript | JavaScript 3D Library. |
| 36 | ↑ 1 | [immich-app/immich](https://github.com/immich-app/immich) | 115,606 | TypeScript | High performance self-hosted photo and video management solution. |
| 37 | ↑ 1 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 115,434 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 38 | ↑ 1 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,598 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 39 | ↑ 1 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,348 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 40 | ↑ 1 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 110,249 | Shell | Papers from the computer science community to read and discuss. |
| 41 | ↑ 1 | [axios/axios](https://github.com/axios/axios) | 109,287 | JavaScript | Promise based HTTP client for the browser and node.js |
| 42 | ↑ 1 | [denoland/deno](https://github.com/denoland/deno) | 108,643 | Rust | A modern runtime for JavaScript and TypeScript. |
| 43 | ↑ 1 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,081 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 44 | ↑ 2 | [neovim/neovim](https://github.com/neovim/neovim) | 102,827 | Vim Script | Vim-fork focused on extensibility and usability |
| 45 | — | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,819 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 46 | ↑ 1 | [angular/angular](https://github.com/angular/angular) | 101,021 | TypeScript | Deliver web apps with confidence 🚀 |
| 47 | ↑ 1 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,683 | TypeScript | An enterprise-class UI design language and React UI library |
| 48 | ↑ 1 | [mui/material-ui](https://github.com/mui/material-ui) | 99,130 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 49 | ↑ 1 | [microsoft/playwright](https://github.com/microsoft/playwright) | 97,113 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |
| 50 | ↑ 1 | [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,895 | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| 51 | ↑ 1 | [oven-sh/bun](https://github.com/oven-sh/bun) | 96,121 | Rust | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [chenglou/pretext](https://github.com/chenglou/pretext) | 50,693 | TypeScript | 2026-03-07 | Fast, accurate & comprehensive text measurement & layout |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 47,720 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 45,972 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 4 | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 43,516 | Markdown | 2026-03-16 | Skills for Designers and Engineers. |
| 5 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 42,401 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 39,667 | C | 2026-07-01 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦 |
| 7 | [block/buzz](https://github.com/block/buzz) | 35,564 | Rust | 2026-03-06 | A hive mind communication platform |
| 8 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33,506 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 9 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 32,494 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 10 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 31,951 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 11 | [BigPizzaV3/CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | 31,818 | Rust | 2026-05-06 | An enhanced tool for CodexApp, striving to make Codex better to use and more comfortable 一个CodexApp的增强工具，努力让Codex变得更好用更舒服 |
| 12 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 30,834 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 13 | [tobi/qmd](https://github.com/tobi/qmd) | 30,201 | TypeScript | 2025-12-08 | mini cli search engine for your docs, knowledge bases, meeting notes, whatever. Tracking current sota approaches while being all local |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,771 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 368,908 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 193,525 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 140,341 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 133,532 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 125,133 | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| [immich-app/immich](https://github.com/immich-app/immich) | 115,606 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,021 | Deliver web apps with confidence 🚀 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,683 | An enterprise-class UI design language and React UI library |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 97,113 | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 250,901 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,187 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,317 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 122,350 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,242 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,287 | Promise based HTTP client for the browser and node.js |
| [mui/material-ui](https://github.com/mui/material-ui) | 99,130 | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,895 | 24 Lessons, 12 Weeks, Get Started as a Web Developer |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 486,167 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 398,506 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 325,295 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 285,879 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,241 | All Algorithms implemented in Python |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,819 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 149,312 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 125,164 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 119,570 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,598 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,643 | A modern runtime for JavaScript and TypeScript. |
| [oven-sh/bun](https://github.com/oven-sh/bun) | 96,121 | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,795 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,389 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 118,139 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,081 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 187,033 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,252 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,294 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,348 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
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
