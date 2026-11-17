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
*Last updated: **2026-11-17 14:45 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | NEW | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 563,331 | Markdown | Master programming by recreating your favorite technologies from scratch. |
| 2 | ↓ 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 499,757 | Python | A collective list of free APIs |
| 3 | ↓ 1 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,245 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 4 | ↓ 1 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,752 | Python | :books: Freely available programming books |
| 5 | ↓ 1 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 372,214 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 6 | NEW | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 337,925 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 7 | ↓ 2 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 335,386 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 8 | ↓ 2 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,909 | Python | Curated list of project-based tutorials |
| 9 | ↓ 2 | [torvalds/linux](https://github.com/torvalds/linux) | 256,129 | C | Linux kernel source tree |
| 10 | ↓ 2 | [react/react](https://github.com/react/react) | 252,817 | JavaScript | The library for web and native user interfaces. |
| 11 | ↓ 2 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,192 | Python | All Algorithms implemented in Python |
| 12 | ↓ 2 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 208,605 | Python | A feature-rich command-line audio/video downloader |
| 13 | ↓ 2 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 199,857 | Batchfile | Open-source Windows and Office activator featuring HWID, Ohook, TSforge, and Online KMS activation methods, along with advanced troubleshoo… |
| 14 | ↓ 2 | [microsoft/vscode](https://github.com/microsoft/vscode) | 195,635 | TypeScript | Visual Studio Code |
| 15 | ↓ 2 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 194,408 | Go | A curated list of awesome Go frameworks, libraries and software |
| 16 | ↓ 2 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,732 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 17 | ↓ 2 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,537 | JavaScript | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| 18 | ↓ 2 | [flutter/flutter](https://github.com/flutter/flutter) | 181,383 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 19 | ↓ 2 | [github/gitignore](https://github.com/github/gitignore) | 176,376 | Unknown | A collection of useful .gitignore templates |
| 20 | ↓ 2 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175,074 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 21 | ↓ 2 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 158,967 | TypeScript | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 22 | ↓ 2 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 155,052 | C | Display and control your Android device |
| 23 | ↓ 2 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 144,219 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 24 | ↓ 2 | [vercel/next.js](https://github.com/vercel/next.js) | 143,680 | JavaScript | The React Framework |
| 25 | ↓ 2 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 143,029 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 26 | ↓ 2 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 141,098 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 27 | ↓ 2 | [golang/go](https://github.com/golang/go) | 140,110 | Go | The Go programming language |
| 28 | ↓ 2 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,853 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 29 | ↓ 2 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,389 | Python | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 30 | ↓ 2 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,853 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 31 | ↓ 2 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,541 | JavaScript | Coding articles to level up your development skills |
| 32 | ↓ 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,272 | Go | Production-Grade Container Scheduling and Management |
| 33 | ↓ 2 | [react/react-native](https://github.com/react/react-native) | 126,940 | C++ | A framework for building native applications using React |
| 34 | ↓ 2 | [electron/electron](https://github.com/electron/electron) | 123,947 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 35 | ↓ 2 | [nodejs/node](https://github.com/nodejs/node) | 123,840 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 36 | ↓ 2 | [rust-lang/rust](https://github.com/rust-lang/rust) | 122,235 | Rust | Empowering everyone to build reliable and efficient software. |
| 37 | ↓ 2 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 120,823 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 38 | ↓ 2 | [godotengine/godot](https://github.com/godotengine/godot) | 120,314 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 39 | ↓ 2 | [immich-app/immich](https://github.com/immich-app/immich) | 119,441 | TypeScript | High performance self-hosted photo and video management solution. |
| 40 | ↓ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,744 | JavaScript | JavaScript 3D Library. |
| 41 | ↓ 3 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 118,728 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 42 | ↓ 2 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 113,593 | Python | Hunt down social media accounts by username across social networks |
| 43 | ↓ 2 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 113,031 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 44 | ↓ 2 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,834 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 45 | ↓ 1 | [axios/axios](https://github.com/axios/axios) | 109,473 | JavaScript | Promise based HTTP client for the browser and node.js |
| 46 | NEW | [denoland/deno](https://github.com/denoland/deno) | 109,009 | Rust | A modern runtime for JavaScript and TypeScript. |
| 47 | ↓ 2 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 108,232 | Unknown | 科技爱好者周刊，每周五发布 |
| 48 | ↓ 2 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,410 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 49 | ↓ 2 | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,944 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 50 | ↓ 2 | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 104,061 | Unknown | Programmer's guide about how to cook at home. |
| 51 | ↓ 2 | [neovim/neovim](https://github.com/neovim/neovim) | 103,852 | Vim Script | Vim-fork focused on extensibility and usability |
| 52 | ↓ 2 | [angular/angular](https://github.com/angular/angular) | 101,551 | TypeScript | Deliver web apps with confidence 🚀 |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | 80,001 | Rust | 2026-09-30 | PhotoCraft: An open-source photo editor written from scratch in pure Rust |
| 2 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 76,285 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 3 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 54,737 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 4 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 53,911 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 51,687 | C | 2026-07-01 | A hierarchical inference engine for frontier MoE models: hot experts on the GPU (CUDA, Vulkan), warm ones in RAM, cold ones streamed from N… |
| 6 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 41,359 | Python | 2026-02-23 | No description provided. |
| 7 | [block/buzz](https://github.com/block/buzz) | 37,552 | Rust | 2026-03-06 | A hive mind communication platform |
| 8 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 36,982 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 9 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 35,631 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 10 | [storytold/craft-anything](https://github.com/storytold/craft-anything) | 35,408 | Rust | 2026-10-31 | Craft Anything: understand how any software works, and craft your own. |
| 11 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 35,055 | Swift | 2026-06-12 | Free and open-source macOS menu bar toolkit. |
| 12 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 34,271 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 13 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 33,233 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 14 | [floci-io/floci](https://github.com/floci-io/floci) | 31,870 | Java | 2026-02-18 | Light, fluffy, and always free - The AWS Local Emulator alternative |
| 15 | [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) | 31,284 | Python | 2026-06-18 | Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 499,757 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,752 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 335,386 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,909 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,192 | All Algorithms implemented in Python |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 208,605 | A feature-rich command-line audio/video downloader |
| [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,389 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 113,593 | Hunt down social media accounts by username across social networks |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,944 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,245 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 372,214 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 195,635 | Visual Studio Code |
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 158,967 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 144,219 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,853 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 119,441 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,551 | Deliver web apps with confidence 🚀 |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 252,817 | The library for web and native user interfaces. |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,537 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,680 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,541 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 123,840 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,744 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,473 | Promise based HTTP client for the browser and node.js |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,940 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,947 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 120,314 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,410 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 194,408 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 140,110 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,272 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,834 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,853 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 122,235 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 113,031 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 109,009 | A modern runtime for JavaScript and TypeScript. |
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
