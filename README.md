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
*Last updated: **2026-09-22 10:09 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Change | Repository | ⭐ Stars | Language | Description |
|--:|:------:|------------|--------:|----------|-------------|
| 1 | — | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 482,183 | Python | A collective list of free APIs |
| 2 | — | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 455,946 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | ↑ 2 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 367,873 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 4 | ↑ 2 | [vinta/awesome-python](https://github.com/vinta/awesome-python) | 322,234 | Python | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| 5 | ↑ 2 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 320,922 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 6 | ↑ 2 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 284,218 | Python | Curated list of project-based tutorials |
| 7 | ↑ 2 | [react/react](https://github.com/react/react) | 250,647 | JavaScript | The library for web and native user interfaces. |
| 8 | ↑ 2 | [torvalds/linux](https://github.com/torvalds/linux) | 249,765 | C | Linux kernel source tree |
| 9 | ↑ 2 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,854 | Python | All Algorithms implemented in Python |
| 10 | ↑ 3 | [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 192,817 | Python | A feature-rich command-line audio/video downloader |
| 11 | ↑ 1 | [microsoft/vscode](https://github.com/microsoft/vscode) | 192,782 | TypeScript | Visual Studio Code |
| 12 | ↑ 2 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,875 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 13 | ↑ 2 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 185,096 | Go | A curated list of awesome Go frameworks, libraries and software |
| 14 | ↑ 2 | [flutter/flutter](https://github.com/flutter/flutter) | 179,039 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 15 | ↑ 2 | [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 178,067 | Python | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| 16 | ↑ 2 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,889 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 17 | ↑ 2 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 150,177 | C | Display and control your Android device |
| 18 | ↑ 2 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 146,327 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 19 | ↑ 2 | [vercel/next.js](https://github.com/vercel/next.js) | 142,396 | JavaScript | The React Framework |
| 20 | ↑ 2 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 139,257 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 21 | ↑ 2 | [golang/go](https://github.com/golang/go) | 138,934 | Go | The Go programming language |
| 22 | ↑ 2 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 138,907 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 23 | ↑ 2 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 137,978 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 24 | ↑ 2 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 132,646 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 25 | ↑ 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 127,892 | Go | Production-Grade Container Scheduling and Management |
| 26 | ↑ 2 | [react/react-native](https://github.com/react/react-native) | 126,689 | C++ | A framework for building native applications using React |
| 27 | ↑ 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 124,368 | TypeScript | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| 28 | ↑ 2 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 124,239 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 29 | ↑ 2 | [electron/electron](https://github.com/electron/electron) | 123,192 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 30 | ↑ 2 | [nodejs/node](https://github.com/nodejs/node) | 122,033 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 31 | ↑ 2 | [rust-lang/rust](https://github.com/rust-lang/rust) | 119,033 | Rust | Empowering everyone to build reliable and efficient software. |
| 32 | ↑ 2 | [godotengine/godot](https://github.com/godotengine/godot) | 117,593 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 33 | ↑ 2 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 116,694 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 34 | ↑ 2 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 115,739 | JavaScript | JavaScript 3D Library. |
| 35 | ↑ 2 | [immich-app/immich](https://github.com/immich-app/immich) | 114,788 | TypeScript | High performance self-hosted photo and video management solution. |
| 36 | ↑ 2 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 114,328 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 37 | ↑ 2 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,255 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 38 | ↑ 2 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,158 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 39 | ↑ 2 | [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | 109,918 | Shell | Papers from the computer science community to read and discuss. |
| 40 | ↑ 3 | [axios/axios](https://github.com/axios/axios) | 109,210 | JavaScript | Promise based HTTP client for the browser and node.js |
| 41 | ↑ 3 | [denoland/deno](https://github.com/denoland/deno) | 108,476 | Rust | A modern runtime for JavaScript and TypeScript. |
| 42 | ↑ 3 | [microsoft/terminal](https://github.com/microsoft/terminal) | 104,963 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 43 | ↑ 3 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 104,392 | Unknown | 科技爱好者周刊，每周五发布 |
| 44 | ↑ 3 | [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,527 | Python | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
| 45 | ↑ 3 | [neovim/neovim](https://github.com/neovim/neovim) | 102,505 | Vim Script | Vim-fork focused on extensibility and usability |
| 46 | ↑ 3 | [Anduin2017/HowToCook](https://github.com/Anduin2017/HowToCook) | 102,314 | Unknown | Programmer's guide about how to cook at home. |
| 47 | ↑ 3 | [angular/angular](https://github.com/angular/angular) | 101,022 | TypeScript | Deliver web apps with confidence 🚀 |
| 48 | ↑ 3 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,581 | TypeScript | An enterprise-class UI design language and React UI library |
| 49 | ↑ 3 | [mui/material-ui](https://github.com/mui/material-ui) | 99,077 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 50 | ↑ 3 | [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,725 | JavaScript | 24 Lessons, 12 Weeks, Get Started as a Web Developer |
| 51 | ↑ 3 | [microsoft/playwright](https://github.com/microsoft/playwright) | 96,496 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |
| 52 | ↑ 3 | [oven-sh/bun](https://github.com/oven-sh/bun) | 96,003 | Rust | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| 53 | ↑ 3 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 95,608 | TypeScript | JavaScript API for Chrome and Firefox |
| 54 | NEW | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 95,158 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions. |

*Change = positions moved in this list since the previous update; NEW = not in the previous update.*
<!-- TRENDING:END -->

## Trending by language

<!-- BY_LANGUAGE:START -->
### TypeScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 455,946 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 367,873 | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 192,782 | Visual Studio Code |
| [iptv-org/iptv](https://github.com/iptv-org/iptv) | 139,257 | Collection of publicly available IPTV channels from all over the world |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 132,646 | Virtual whiteboard for sketching hand-drawn like diagrams |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 124,368 | Composable, accessible components with thoughtful defaults. Build your own component library with code you can customize, extend, and make… |
| [immich-app/immich](https://github.com/immich-app/immich) | 114,788 | High performance self-hosted photo and video management solution. |
| [angular/angular](https://github.com/angular/angular) | 101,022 | Deliver web apps with confidence 🚀 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,581 | An enterprise-class UI design language and React UI library |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 96,496 | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |

### JavaScript

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react](https://github.com/react/react) | 250,647 | The library for web and native user interfaces. |
| [vercel/next.js](https://github.com/vercel/next.js) | 142,396 | The React Framework |
| [nodejs/node](https://github.com/nodejs/node) | 122,033 | Node.js JavaScript runtime ✨🐢🚀✨ |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 115,739 | JavaScript 3D Library. |
| [axios/axios](https://github.com/axios/axios) | 109,210 | Promise based HTTP client for the browser and node.js |
| [mui/material-ui](https://github.com/mui/material-ui) | 99,077 | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| [microsoft/Web-Dev-For-Beginners](https://github.com/microsoft/Web-Dev-For-Beginners) | 96,725 | 24 Lessons, 12 Weeks, Get Started as a Web Developer |

### Python

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 482,183 | A collective list of free APIs |
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 322,234 | The definitive list that answers "I want to do X in Python, which tool should I use?" |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 284,218 | Curated list of project-based tutorials |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,854 | All Algorithms implemented in Python |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 192,817 | A feature-rich command-line audio/video downloader |
| [521xueweihan/HelloGitHub](https://github.com/521xueweihan/HelloGitHub) | 178,067 | :octocat: 分享 GitHub 上有趣、入门级的开源项目。Share interesting, entry-level open source projects on GitHub. |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 102,527 | FastAPI framework, high performance, easy to learn, fast to code, ready for production |

### Rust

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 146,327 | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 124,239 | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 119,033 | Empowering everyone to build reliable and efficient software. |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,255 | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| [denoland/deno](https://github.com/denoland/deno) | 108,476 | A modern runtime for JavaScript and TypeScript. |
| [oven-sh/bun](https://github.com/oven-sh/bun) | 96,003 | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |

### C++

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [react/react-native](https://github.com/react/react-native) | 126,689 | A framework for building native applications using React |
| [electron/electron](https://github.com/electron/electron) | 123,192 | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| [godotengine/godot](https://github.com/godotengine/godot) | 117,593 | Godot Engine – Multi-platform 2D and 3D game engine |
| [microsoft/terminal](https://github.com/microsoft/terminal) | 104,963 | The new Windows Terminal and the original Windows console host, all in the same place! |

### Go

| Repository | ⭐ Stars | Description |
|------------|--------:|-------------|
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 185,096 | A curated list of awesome Go frameworks, libraries and software |
| [golang/go](https://github.com/golang/go) | 138,934 | The Go programming language |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 127,892 | Production-Grade Container Scheduling and Management |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,158 | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
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
