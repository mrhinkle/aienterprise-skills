# Social bundle (aie-social)

Two research-driven post generators. The point of both is **research quality**: they gather real facts and citable sources before writing, and never ship a factual claim they can't source. Both run **ai-slop-killer** as a mandatory final pass, so posts don't read as machine-written.

Both are brand- and person-neutral. Point them at a voice skill or a `voice.config.md` / `slop.config.md` to match your tone; otherwise they write in a clear, credible, human voice.

---

## aie-social-linkedin

Turns any topic — or a source document (article, transcript, draft) — into a high-quality LinkedIn post, or a short series.

**The loop: Research → Draft → Review → Deliver.**

1. **Research** — establish the one idea and angle, run web searches, fetch primary sources, and build a claim → URL source log. Unsourced claims get cut or labeled opinion.
2. **Draft** — hook first (the opening ~210 characters decide whether anyone expands the post), skimmable one-idea body, concrete takeaway, genuine engagement close. Keeps ~80% of the value in the post itself (LinkedIn suppresses reach for posts that push readers off-platform).
3. **Review** — score against the quality rubric; verify every claim maps to a source; run ai-slop-killer.
4. **Deliver** — the post, 2–3 alternative hooks to A/B, the first-comment link if any, and the sources log.

**Outputs:** ready-to-paste post + alternate hooks + sources + rubric score.
**Reference:** `research-checklist.md`, `hook-library.md`, `formatting-guide.md`, `quality-rubric.md`, `sources.md`.
**Trigger:** "write a LinkedIn post about X," "turn this into a LinkedIn post," "repurpose this for LinkedIn."

## aie-social-x

The same research-then-draft-then-review flow, tuned to X (Twitter): the single-post-vs-thread decision, a hook that stands alone in ~1.5 seconds, thread structure (sweet spot ~5–9 posts), character limits, links kept out of the main post, and minimal hashtags.

**Outputs:** the post or thread + alternate hooks + sources + rubric score.
**Reference:** `research-checklist.md`, `hook-library.md`, `formatting-guide.md`, `quality-rubric.md`, `sources.md`.
**Trigger:** "write an X post," "make a thread about X," "turn this into a thread."

---

## Why the research phase matters

Most AI-written social posts fail in one of two ways: they're generic (no real information) or they're confidently wrong (invented stats). These skills fix both by making research the first step and source-backing a hard rule. Fabricated stats and quotes are banned outright. The best-practice sources behind each skill's formatting rules are listed in its `reference/sources.md`, with the 2026 algorithm findings that shaped them.
