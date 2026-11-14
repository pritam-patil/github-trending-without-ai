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
*Last updated: **2026-11-14 12:22 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | 562,443 | Markdown | Master programming by recreating your favorite technologies from scratch. |
| 2 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 498,911 | Python | A collective list of free APIs |
| 3 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,120 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 4 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,578 | Python | :books: Freely available programming books |
| 5 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 371,982 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 6 | ↑ 2 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 334,668 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 7 | ↑ 2 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,715 | Python | Curated list of project-based tutorials |
| 8 | ↑ 2 | [torvalds/linux](https://github.com/torvalds/linux) | 255,631 | C | Linux kernel source tree |
| 9 | ↑ 2 | [react/react](https://github.com/react/react) | 252,599 | JavaScript | The library for web and native user interfaces. |
| 10 | ↑ 2 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,101 | Python | All Algorithms implemented in Python |
| 11 | ↑ 2 | [ossu/computer-science](https://github.com/ossu/computer-science) | 211,075 | HTML | 🎓 Path to a free self-taught education in Computer Science! |
| 12 | ↑ 2 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 198,954 | Batchfile | Open-source Windows and Office activator featuring HWID, Ohook, TSforge, and Online KMS activation methods, along with advanced troubleshoo… |
| 13 | ↑ 2 | [microsoft/vscode](https://github.com/microsoft/vscode) | 195,368 | TypeScript | Visual Studio Code |
| 14 | ↑ 2 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 193,845 | Go | A curated list of awesome Go frameworks, libraries and software |
| 15 | ↑ 2 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,615 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 16 | ↑ 2 | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,507 | JavaScript | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| 17 | ↑ 2 | [flutter/flutter](https://github.com/flutter/flutter) | 181,264 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 18 | ↑ 2 | [github/gitignore](https://github.com/github/gitignore) | 176,331 | Unknown | A collection of useful .gitignore templates |
| 19 | ↑ 2 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175,058 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 20 | ↑ 2 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 158,356 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 21 | ↑ 2 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 154,787 | C | Display and control your Android device |
| 22 | ↑ 2 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 143,967 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 23 | ↑ 2 | [vercel/next.js](https://github.com/vercel/next.js) | 143,510 | JavaScript | The React Framework |
| 24 | ↑ 2 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 142,805 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 25 | ↑ 2 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 140,971 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 26 | ↑ 2 | [golang/go](https://github.com/golang/go) | 139,879 | Go | The Go programming language |
| 27 | ↑ 2 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,669 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 28 | ↑ 2 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,317 | Python | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 29 | ↑ 2 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,508 | JavaScript | Coding articles to level up your development skills |
| 30 | ↑ 2 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,417 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 31 | ↑ 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,056 | Go | Production-Grade Container Scheduling and Management |
| 32 | ↑ 2 | [react/react-native](https://github.com/react/react-native) | 126,919 | C++ | A framework for building native applications using React |
| 33 | ↑ 2 | [electron/electron](https://github.com/electron/electron) | 123,899 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 34 | ↑ 2 | [nodejs/node](https://github.com/nodejs/node) | 123,711 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 35 | ↑ 2 | [rust-lang/rust](https://github.com/rust-lang/rust) | 121,897 | Rust | Empowering everyone to build reliable and efficient software. |
| 36 | ↑ 2 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 120,596 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 37 | ↑ 2 | [godotengine/godot](https://github.com/godotengine/godot) | 120,123 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 38 | ↑ 2 | [immich-app/immich](https://github.com/immich-app/immich) | 119,145 | TypeScript | High performance self-hosted photo and video management solution. |
| 39 | ↑ 2 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 118,503 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 40 | ↑ 2 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,363 | JavaScript | JavaScript 3D Library. |
| 41 | ↑ 2 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,901 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 42 | ↑ 2 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,809 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 43 | ↑ 2 | [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 111,485 | Python | Hunt down social media accounts by username across social networks |
| 44 | ↑ 2 | [fatedier/frp](https://github.com/fatedier/frp) | 110,578 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 45 | ↑ 2 | [axios/axios](https://github.com/axios/axios) | 109,390 | JavaScript | Promise based HTTP client for the browser and node.js |
| 46 | ↑ 2 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 108,045 | Unknown | 科技爱好者周刊，每周五发布 |
| 47 | ↑ 2 | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,384 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 48 | ↑ 2 | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,703 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 49 | NEW | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 103,935 | Unknown | Programmer's guide about how to cook at home. |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | 79,300 | Rust | 2026-09-30 | PhotoCraft: An open-source photo editor written from scratch in pure Rust |
| 2 | [eternity4719/HowToLiveBetter](https://github.com/eternity4719/HowToLiveBetter) | 75,700 | HTML | 2026-09-07 | 高性价比人生指南: 长寿防病、急救、省钱理财、法律红线、失业与工伤、医保社保、恋爱婚育、怀孕育儿、创业与做平台合规、出国与技能。每条写明成本、收益、证据等级和原始出处，只引期刊论文与官方文件。 |
| 3 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 64,766 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 4 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 53,832 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 5 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 53,519 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 6 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 50,977 | C | 2026-07-01 | A hierarchical inference engine for frontier MoE models: hot experts on the GPU (CUDA, Vulkan), warm ones in RAM, cold ones streamed from N… |
| 7 | [anthropics/financial-services](https://github.com/anthropics/financial-services) | 41,286 | Python | 2026-02-23 | No description provided. |
| 8 | [block/buzz](https://github.com/block/buzz) | 37,420 | Rust | 2026-03-06 | A hive mind communication platform |
| 9 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 36,711 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 10 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 35,516 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 11 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 34,672 | Swift | 2026-06-12 | Free and open-source macOS menu bar toolkit. |
| 12 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 34,213 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 13 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 33,093 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 498,911 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,578 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 334,668 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,715 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 226,101 | All Algorithms implemented in Python |
| [krahets/hello-algo](https://github.com/krahets/hello-algo) | 132,317 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock) | 111,485 | Hunt down social media accounts by username across social networks |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,703 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 252,599 | The library for web and native user interfaces. |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,507 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,510 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,508 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 123,711 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 118,363 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,390 | Promise based HTTP client for the browser and node.js |

### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,120 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 371,982 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 195,368 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 143,967 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 135,669 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 119,145 | High performance self-hosted photo and video management solution. |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 193,845 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,879 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 129,056 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,809 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 110,578 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,919 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,899 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 120,123 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,384 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 158,356 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 129,417 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 121,897 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,901 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
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
