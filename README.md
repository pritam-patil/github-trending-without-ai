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
table below.

## Trending non-AI repositories

<!-- TRENDING:START -->
*Last updated: **2026-09-19 09:39 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 481,516 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 455,757 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | — | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 397,187 | Python | :books: Freely available programming books |
| 4 | — | [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 370,710 | Python | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| 5 | — | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 367,663 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 6 | — | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 321,627 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 7 | — | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 320,256 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 8 | — | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 283,827 | Python | Curated list of project-based tutorials |
| 9 | — | [react/react](https://github.com/react/react) | 250,584 | JavaScript | The library for web and native user interfaces. |
| 10 | — | [torvalds/linux](https://github.com/torvalds/linux) | 249,477 | C | Linux kernel source tree |
| 11 | — | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,753 | Python | All Algorithms implemented in Python |
| 12 | — | [microsoft/vscode](https://github.com/microsoft/vscode) | 192,677 | TypeScript | Visual Studio Code |
| 13 | — | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 192,050 | Python | A feature-rich command-line audio/video downloader |
| 14 | — | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,799 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 15 | — | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 184,730 | Go | A curated list of awesome Go frameworks, libraries and software |
| 16 | — | [flutter/flutter](https://github.com/flutter/flutter) | 179,002 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 17 | — | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,850 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 18 | — | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 149,976 | C | Display and control your Android device |
| 19 | — | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 145,403 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 20 | — | [vercel/next.js](https://github.com/vercel/next.js) | 142,348 | JavaScript | The React Framework |
| 21 | — | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 138,991 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 22 | — | [golang/go](https://github.com/golang/go) | 138,882 | Go | The Go programming language |
| 23 | — | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 138,828 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 24 | — | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 137,763 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 25 | — | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 132,387 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 26 | — | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 127,819 | Go | Production-Grade Container Scheduling and Management |
| 27 | — | [react/react-native](https://github.com/react/react-native) | 126,650 | C++ | A framework for building native applications using React |
| 28 | — | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 124,166 | TypeScript | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| 29 | — | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 123,973 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 30 | — | [electron/electron](https://github.com/electron/electron) | 123,151 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 31 | — | [nodejs/node](https://github.com/nodejs/node) | 122,004 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 32 | — | [rust-lang/rust](https://github.com/rust-lang/rust) | 118,949 | Rust | Empowering everyone to build reliable and efficient software. |
| 33 | — | [godotengine/godot](https://github.com/godotengine/godot) | 117,448 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 34 | — | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 116,490 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 35 | — | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 115,648 | JavaScript | JavaScript 3D Library. |
| 36 | — | [immich-app/immich](https://github.com/immich-app/immich) | 114,576 | TypeScript | High performance self-hosted photo and video management solution. |
| 37 | — | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 114,145 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 38 | — | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,174 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 39 | — | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,108 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 40 | — | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 109,845 | Shell | Papers from the computer science community to read and discuss. |
| 41 | — | [fatedier/frp](https://github.com/fatedier/frp) | 109,510 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 42 | — | [axios/axios](https://github.com/axios/axios) | 109,209 | JavaScript | Promise based HTTP client for the browser and node.js |
| 43 | — | [denoland/deno](https://github.com/denoland/deno) | 108,468 | Rust | A modern runtime for JavaScript and TypeScript. |
| 44 | — | [microsoft/terminal](https://github.com/microsoft/terminal) | 104,935 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 45 | — | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 102,940 | Unknown | 科技爱好者周刊，每周五发布 |
| 46 | — | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,455 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 47 | — | [neovim/neovim](https://github.com/neovim/neovim) | 102,422 | Vim Script | Vim-fork focused on extensibility and usability |
| 48 | NEW | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 102,266 | Unknown | Programmer's guide about how to cook at home. |
| 49 | ↓ 1 | [angular/angular](https://github.com/angular/angular) | 101,012 | TypeScript | Deliver web apps with confidence 🚀 |
| 50 | ↓ 1 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,545 | TypeScript | An enterprise-class UI design language and React UI library |
| 51 | ↓ 1 | [mui/material-ui](https://github.com/mui/material-ui) | 99,060 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 52 | ↓ 1 | [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,705 | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| 53 | ↓ 1 | [microsoft/playwright](https://github.com/microsoft/playwright) | 96,341 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |
| 54 | ↓ 1 | [oven-sh/bun](https://github.com/oven-sh/bun) | 95,985 | Rust | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| 55 | ↓ 1 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 95,593 | TypeScript | JavaScript API for Chrome and Firefox |
| 56 | ↓ 1 | [iluwatar/java-design-patterns](https://github.com/iluwatar/java-design-patterns) | 94,706 | Java | Design patterns implemented in Java |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 455,757 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 367,663 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 192,677 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 138,991 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 132,387 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 124,166 | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| [immich-app/immich](https://github.com/immich-app/immich) | 114,576 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,012 | Deliver web apps with confidence 🚀 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,545 | An enterprise-class UI design language and React UI library |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 96,341 | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 481,516 | A collective list of free APIs |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 397,187 | :books: Freely available programming books |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | 370,710 | Learn how to design large-scale systems. Prep for the system design interview. Includes Anki flashcards. |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 321,627 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 283,827 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,753 | All Algorithms implemented in Python |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 192,050 | A feature-rich command-line audio/video downloader |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,455 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 250,584 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 142,348 | The React Framework |
| [nodejs/node](https://github.com/nodejs/node) | 122,004 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 115,648 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,209 | Promise based HTTP client for the browser and node.js |
| [mui/material-ui](https://github.com/mui/material-ui) | 99,060 | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,705 | 24 Lessons, 12 Weeks, Get Started as a Web Developer |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 145,403 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 123,973 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 118,949 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,174 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,468 | A modern runtime for JavaScript and TypeScript. |
| [oven-sh/bun](https://github.com/oven-sh/bun) | 95,985 | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 184,730 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 138,882 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 127,819 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,108 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| [fatedier/frp](https://github.com/fatedier/frp) | 109,510 | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,650 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,151 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 117,448 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 104,935 | The new Windows Terminal and the original Windows console host, all in the same place! |
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
