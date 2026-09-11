# Launch kit (drafts — not published content)

> Internal working document. Nothing here is posted automatically; every
> post below is a draft for the maintainer to review, adapt, and publish
> by hand, in sequence.

## Ground rules

- **Never anti-AI.** The pitch is curiosity and discovery ("the rest of
  open source"), not exclusion. If a sentence would read as "AI is bad,"
  rewrite it.
- **Never overpromise.** Say "AI-focused repositories filtered out with a
  transparent keyword heuristic," not "AI-free."
- **The content is the marketing.** Lead with interesting repos found via
  the list, not with "I built a thing, please star."
- One channel at a time; adapt the angle to each community, no
  copy-paste cross-posting.

## Sequence

| Day | Channel | Goal |
|-----|---------|------|
| 1 | Hacker News | Discussion + first wave of stars |
| 2–3 | Reddit (r/opensource, r/programming, r/selfhosted) | Community-fit angles |
| 4–5 | Dev.to | Long-form write-up, evergreen search traffic |
| ongoing | Occasional posts | "Interesting finds this week" style |

Measure stars, forks, site visitors, and returning traffic (repo
Insights), not "posts made."

---

## Day 1 — Hacker News

**Title:**

> Show HN: GitHub Trending, minus the AI

**URL:** https://pritam-patil.github.io/github-trending-without-ai/

**First comment (post immediately after submitting):**

> I kept opening GitHub Trending to see what was new in open source and
> finding that most of the list was LLM wrappers, agent frameworks, and
> prompt toolkits. Useful when you're looking for AI — but I wanted a way
> to see what was trending across the rest of open source.
>
> So I built a small, transparent filter: a daily GitHub Action fetches
> repos with >100 stars pushed in the last 7 days, then sets aside
> anything whose name, description, or topics match a configurable
> keyword list ("ai", "llm", "agent", etc., matched on word boundaries so
> "email" and "maintain" survive).
>
> It's deliberately a reproducible keyword rule rather than a classifier,
> which means false positives and negatives happen — the keyword list is
> one Python list, and PRs against it are welcome. The data is also
> published as JSON, and there's an RSS daily digest.
>
> Repo: https://github.com/pritam-patil/github-trending-without-ai

*Reply prep:* the most likely pushback is "what counts as AI?" — answer
with the transparency section (it's a keyword rule, not a judgment call)
and invite PRs. Don't argue about whether AI projects belong on Trending.

---

## Day 2–3 — Reddit

**r/opensource — angle: rediscovery**

> Title: A daily "GitHub Trending" feed for open source that isn't AI
>
> Body: GitHub Trending is dominated by AI/LLM projects lately — which is
> fine, but it makes it harder to spot everything else. I made a daily
> auto-updated list (repo README + a small static site + RSS) of trending
> repos with AI-focused ones filtered out by a transparent keyword rule.
> Today's list surfaced [pick 3 concrete non-obvious repos from today's
> data]. Filter is one Python list; corrections welcome.

**r/programming — angle: the mechanism**

> Title: I built a filtered view of GitHub Trending with a 30-line
> keyword heuristic and a GitHub Action
>
> Body: focus on the engineering: Search API criteria, word-boundary
> matching (why "email" survives an "ai" keyword), canonical JSON with a
> versioned schema, README/site as two renderers of the same dataset,
> daily snapshots for rank movement. Link the repo.

**r/selfhosted — angle: findings, only if genuine**

> Title: [N] self-hosted projects trending on GitHub this week (from a
> non-AI trending feed I run)
>
> Body: lead with the actual self-hosted repos from the list (immich,
> rustdesk, frp-class finds). Mention the feed once at the end. Skip this
> post if a given week has no interesting self-hosted entries.

---

## Day 4–5 — Dev.to

**Title:** I built GitHub Trending, minus the AI

**Outline:**

1. The itch: wanting to see what else is trending (not an anti-AI rant —
   say so explicitly).
2. The rule: >100 stars, pushed within 7 days, keyword filter on
   name/description/topics; why a transparent heuristic beats a
   classifier for this job.
3. What went wrong: word boundaries ("email"/"maintain"), `gpt` vs
   `gpt4`, false positives — honest lessons.
4. The architecture: canonical JSON → README table, static site, RSS as
   renderers; daily snapshots → rank movement.
5. What I found: 3–5 genuinely interesting repos discovered through the
   list.
6. Invitation: the keyword list is one PR away.

---

## Ongoing

- Occasional "this week's finds" posts reusing the r/selfhosted format
  for other niches (CLI tools, databases, Rust).
- The website's daily page title ("N open-source projects trending on
  GitHub today — minus AI-focused repos") is the shareable unit — link
  the site, not just the repo.
