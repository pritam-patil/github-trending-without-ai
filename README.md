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
*Last updated: **2026-10-28 11:28 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 492,866 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458,085 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 400,360 | Python | :books: Freely available programming books |
| 4 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 370,601 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 331,258 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 6 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 330,812 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 7 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 288,273 | Python | Curated list of project-based tutorials |
| 8 | — | [torvalds/linux](https://github.com/torvalds/linux) | 253,712 | C | Linux kernel source tree |
| 9 | — | [react/react](https://github.com/react/react) | 251,770 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 203,219 | Python | A feature-rich command-line audio/video downloader |
| 11 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 194,373 | TypeScript | Visual Studio Code |
| 12 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 190,777 | Go | A curated list of awesome Go frameworks, libraries and software |
| 13 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,206 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 14 | — | [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,357 | Python | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| 15 | NEW | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 185,188 | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| 16 | ↓ 1 | [flutter/flutter](https://github.com/flutter/flutter) | 180,510 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 17 | ↓ 1 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 175,018 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 18 | ↓ 1 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 154,548 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 19 | ↓ 1 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 153,366 | C | Display and control your Android device |
| 20 | ↓ 1 | [vercel/next.js](https://github.com/vercel/next.js) | 143,175 | JavaScript | The React Framework |
| 21 | ↓ 1 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 142,600 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 22 | ↓ 1 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 140,190 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 23 | ↓ 1 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 140,119 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 24 | ↓ 1 | [golang/go](https://github.com/golang/go) | 139,482 | Go | The Go programming language |
| 25 | ↓ 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 134,710 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 26 | ↓ 1 | [krahets/hello-algo](https://github.com/krahets/hello-algo) | 131,592 | Java | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 |
| 27 | ↓ 1 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,356 | JavaScript | Coding articles to level up your development skills |
| 28 | ↓ 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,582 | Go | Production-Grade Container Scheduling and Management |
| 29 | ↓ 1 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 127,366 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 30 | ↓ 1 | [react/react-native](https://github.com/react/react-native) | 126,808 | C++ | A framework for building native applications using React |
| 31 | ↓ 1 | [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | 123,860 | Unknown | A collection of various awesome lists for hackers, pentesters and security researchers |
| 32 | ↓ 1 | [electron/electron](https://github.com/electron/electron) | 123,593 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 33 | ↓ 1 | [nodejs/node](https://github.com/nodejs/node) | 123,125 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 34 | ↓ 1 | [rust-lang/rust](https://github.com/rust-lang/rust) | 120,879 | Rust | Empowering everyone to build reliable and efficient software. |
| 35 | ↓ 1 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 119,325 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 36 | ↓ 1 | [godotengine/godot](https://github.com/godotengine/godot) | 119,192 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 37 | ↓ 1 | [immich-app/immich](https://github.com/immich-app/immich) | 117,470 | TypeScript | High performance self-hosted photo and video management solution. |
| 38 | ↓ 1 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 117,228 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 39 | ↓ 1 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 117,117 | JavaScript | JavaScript 3D Library. |
| 40 | — | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,261 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 41 | — | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,645 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 42 | — | [fatedier/frp](https://github.com/fatedier/frp) | 110,237 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 43 | — | [axios/axios](https://github.com/axios/axios) | 109,310 | JavaScript | Promise based HTTP client for the browser and node.js |
| 44 | — | [denoland/deno](https://github.com/denoland/deno) | 108,788 | Rust | A modern runtime for JavaScript and TypeScript. |
| 45 | — | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 107,116 | Unknown | 科技爱好者周刊，每周五发布 |
| 46 | — | [microsoft/terminal](https://github.com/microsoft/terminal) | 105,261 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 47 | — | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,232 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 48 | — | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 103,294 | Unknown | Programmer's guide about how to cook at home. |
| 49 | — | [neovim/neovim](https://github.com/neovim/neovim) | 103,227 | Vim Script | Vim-fork focused on extensibility and usability |
| 50 | — | [angular/angular](https://github.com/angular/angular) | 101,091 | TypeScript | Deliver web apps with confidence 🚀 |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## 🌱 New &amp; rising

Trending repositories **created in the past year** — the newcomers, without
the long-established giants.

<!-- FRESH:START -->
| # | Repository | ⭐ Stars | Language | Created | Description |
|--:|------------|--------:|----------|---------|-------------|
| 1 | [storytold/photocraft](https://github.com/storytold/photocraft) | 74,167 | Rust | 2026-09-30 | PhotoCraft: An open-source, photo editor written by scratch in pure Rust |
| 2 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 60,813 | JavaScript | 2026-06-22 | A spy satellite simulator in your browser, except the data is real. Live open source spatial intelligence on a photorealistic 3D globe. |
| 3 | [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) | 51,131 | Python | 2026-04-24 | 符合nature论文学术表达和科研绘图的Skill |
| 4 | [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5) | 49,151 | C++ | 2026-08-03 | Tool for automatic PS5 executables porting to Linux and Windows |
| 5 | [JustVugg/colibri](https://github.com/JustVugg/colibri) | 44,521 | C | 2026-07-01 | Run frontier MoE models on hardware you already own — pure C, zero deps, experts streamed from disk. Tiny engine, immense model. 🐦 |
| 6 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) | 36,547 | Python | 2026-04-05 | 你想蒸馏的下一个员工，何必是同事。蒸馏任何人的思维方式——心智模型、决策启发式、表达DNA。Distill how anyone thinks. |
| 7 | [block/buzz](https://github.com/block/buzz) | 36,527 | Rust | 2026-03-06 | A hive mind communication platform |
| 8 | [webadderallorg/Recordly](https://github.com/webadderallorg/Recordly) | 35,453 | TypeScript | 2026-03-12 | Create polished demo videos without editing skills. Mac/Windows/Linux |
| 9 | [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 34,518 | Python | 2026-09-18 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward pass, in 100+ langu… |
| 10 | [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33,854 | Rust | 2026-01-19 | Algorithm powering the For You feed on X |
| 11 | [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) | 32,637 | Rust | 2025-11-26 | Professional Antigravity Account Manager & Switcher. One-click seamless account switching for Antigravity Tools. Built with Tauri v2 + Reac… |
| 12 | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 30,974 | TypeScript | 2026-02-08 | No description provided. |
| 13 | [vorssaint/vorssaint-utils](https://github.com/vorssaint/vorssaint-utils) | 30,361 | Swift | 2026-06-12 | Free and open-source macOS menu bar toolkit. |
<!-- FRESH:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 492,866 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 400,360 | :books: Freely available programming books |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 330,812 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 288,273 | Curated list of project-based tutorials |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 203,219 | A feature-rich command-line audio/video downloader |
| [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes) | 186,357 | :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计 |
| [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 185,188 | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 104,232 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458,085 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 370,601 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 194,373 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 142,600 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 134,710 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [immich-app/immich](https://github.com/immich-app/immich) | 117,470 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,091 | Deliver web apps with confidence 🚀 |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 251,770 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 143,175 | The React Framework |
| [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,356 | Coding articles to level up your development skills |
| [nodejs/node](https://github.com/nodejs/node) | 123,125 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 117,117 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,310 | Promise based HTTP client for the browser and node.js |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 190,777 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 139,482 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 128,582 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,645 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 110,237 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 154,548 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 127,366 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 120,879 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 112,261 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,788 | A modern runtime for JavaScript and TypeScript. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,808 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,593 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 119,192 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 105,261 | The new Windows Terminal and the original Windows console host, all in the same place! |
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
