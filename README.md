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
*Last updated: **2026-09-11 16:49 UTC** — repos with >100 stars, active in the last 7 days, no AI keywords detected.*

| # | Repository | ⭐ Stars | Language | Description |
|--:|------------|--------:|----------|-------------|
| 1 | [public-apis/public-apis](https://github.com/public-apis/public-apis) | 478,920 | Python | A collective list of free APIs |
| 2 | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 455,312 | TypeScript | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| 3 | [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 396,528 | Python | :books: Freely available programming books |
| 4 | [nilbuild/developer-roadmap](https://github.com/nilbuild/developer-roadmap) | 366,898 | TypeScript | Interactive roadmaps, guides and other educational content to help developers grow in their careers. |
| 5 | [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | 318,529 | Unknown | A list of Free Software network services and web applications which can be hosted on your own servers |
| 6 | [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 282,967 | Python | Curated list of project-based tutorials |
| 7 | [react/react](https://github.com/react/react) | 250,039 | JavaScript | The library for web and native user interfaces. |
| 8 | [torvalds/linux](https://github.com/torvalds/linux) | 248,253 | C | Linux kernel source tree |
| 9 | [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,480 | Python | All Algorithms implemented in Python |
| 10 | [microsoft/vscode](https://github.com/microsoft/vscode) | 192,008 | TypeScript | Visual Studio Code |
| 11 | [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts) | 190,193 | Batchfile | Open-source Windows and Office activator featuring HWID, Ohook, TSforge, and Online KMS activation methods, along with advanced troubleshoo… |
| 12 | [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,670 | Shell | 🙃 A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 300+ optional plugins (r… |
| 13 | [avelino/awesome-go](https://github.com/avelino/awesome-go) | 183,813 | Go | A curated list of awesome Go frameworks, libraries and software |
| 14 | [flutter/flutter](https://github.com/flutter/flutter) | 178,894 | Dart | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| 15 | [github/gitignore](https://github.com/github/gitignore) | 175,713 | Unknown | A collection of useful .gitignore templates |
| 16 | [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,758 | MDX | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |
| 17 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 149,393 | C | Display and control your Android device |
| 18 | [clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev) | 143,827 | Rust | A modern GUI client based on Tauri, designed to run in Windows, macOS and Linux for tailored proxy experience |
| 19 | [vercel/next.js](https://github.com/vercel/next.js) | 142,236 | JavaScript | The React Framework |
| 20 | [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | 138,560 | C | Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows |
| 21 | [golang/go](https://github.com/golang/go) | 138,417 | Go | The Go programming language |
| 22 | [iptv-org/iptv](https://github.com/iptv-org/iptv) | 138,334 | TypeScript | Collection of publicly available IPTV channels from all over the world |
| 23 | [ripienaar/free-for-dev](https://github.com/ripienaar/free-for-dev) | 137,132 | HTML | A list of SaaS, PaaS and IaaS offerings that have free tiers of interest to devops and infradev |
| 24 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 131,612 | TypeScript | Virtual whiteboard for sketching hand-drawn like diagrams |
| 25 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,036 | JavaScript | Coding articles to level up your development skills |
| 26 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 127,334 | Go | Production-Grade Container Scheduling and Management |
| 27 | [react/react-native](https://github.com/react/react-native) | 126,556 | C++ | A framework for building native applications using React |
| 28 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 123,574 | TypeScript | A set of beautifully-designed, accessible components and a code distribution platform. Works with your favorite frameworks. Open Source. Op… |
| 29 | [rustdesk/rustdesk](https://github.com/rustdesk/rustdesk) | 123,187 | Rust | An open-source remote desktop application designed for self-hosting, as an alternative to TeamViewer. |
| 30 | [electron/electron](https://github.com/electron/electron) | 122,995 | C++ | :electron: Build cross-platform desktop apps with JavaScript, HTML, and CSS |
| 31 | [nodejs/node](https://github.com/nodejs/node) | 121,583 | JavaScript | Node.js JavaScript runtime ✨🐢🚀✨ |
| 32 | [rust-lang/rust](https://github.com/rust-lang/rust) | 118,389 | Rust | Empowering everyone to build reliable and efficient software. |
| 33 | [godotengine/godot](https://github.com/godotengine/godot) | 116,971 | C++ | Godot Engine – Multi-platform 2D and 3D game engine |
| 34 | [2dust/v2rayN](https://github.com/2dust/v2rayN) | 115,916 | C# | A GUI client for Windows, Linux and macOS, support Xray and sing-box and others |
| 35 | [mrdoob/three.js](https://github.com/mrdoob/three.js) | 115,410 | JavaScript | JavaScript 3D Library. |
| 36 | [immich-app/immich](https://github.com/immich-app/immich) | 113,842 | TypeScript | High performance self-hosted photo and video management solution. |
| 37 | [jaywcjlove/awesome-mac](https://github.com/jaywcjlove/awesome-mac) | 113,563 | Swift |  This project is dedicated to collecting high-quality macOS software and organizing them systematically by different categories for easy s… |
| 38 | [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 111,003 | Rust | Build smaller, faster, and more secure desktop and mobile applications with a web frontend. |
| 39 | [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 111,000 | Go | TypeScript is a superset of JavaScript that compiles to clean JavaScript output. |
| 40 | [fatedier/frp](https://github.com/fatedier/frp) | 109,345 | Go | A fast reverse proxy to help you expose a local server behind a NAT or firewall to the internet. |
| 41 | [axios/axios](https://github.com/axios/axios) | 109,222 | JavaScript | Promise based HTTP client for the browser and node.js |
| 42 | [denoland/deno](https://github.com/denoland/deno) | 108,402 | Rust | A modern runtime for JavaScript and TypeScript. |
| 43 | [microsoft/terminal](https://github.com/microsoft/terminal) | 104,874 | C++ | The new Windows Terminal and the original Windows console host, all in the same place! |
| 44 | [ruanyf/weekly](https://github.com/ruanyf/weekly) | 102,353 | Unknown | 科技爱好者周刊，每周五发布 |
| 45 | [neovim/neovim](https://github.com/neovim/neovim) | 102,270 | Vim Script | Vim-fork focused on extensibility and usability |
| 46 | [angular/angular](https://github.com/angular/angular) | 100,993 | TypeScript | Deliver web apps with confidence 🚀 |
| 47 | [ant-design/ant-design](https://github.com/ant-design/ant-design) | 99,480 | TypeScript | An enterprise-class UI design language and React UI library |
| 48 | [mui/material-ui](https://github.com/mui/material-ui) | 99,027 | JavaScript | Material UI: Comprehensive React component library that implements Google's Material Design. Free forever. |
| 49 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 97,500 | TypeScript | A utility-first CSS framework for rapid UI development. |
| 50 | [microsoft/playwright](https://github.com/microsoft/playwright) | 95,978 | TypeScript | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. |
| 51 | [oven-sh/bun](https://github.com/oven-sh/bun) | 95,943 | Rust | Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one |
| 52 | [puppeteer/puppeteer](https://github.com/puppeteer/puppeteer) | 95,574 | TypeScript | JavaScript API for Chrome and Firefox |
| 53 | [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | 95,071 | Shell | Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions. $nvm: 3ArcxqLtXMmBnWbbtfwQgVL3MNnDsggzgGDtXM… |
| 54 | [3b1b/manim](https://github.com/3b1b/manim) | 93,745 | Python | Animation engine for explanatory math videos |
<!-- TRENDING:END -->

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
