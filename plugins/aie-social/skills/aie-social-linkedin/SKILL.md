---
name: aie-social-linkedin
description: Produce a high-quality, research-backed LinkedIn post (or short series) on any topic for any brand or person. Runs a real research phase to gather facts and citable sources, drafts using proven LinkedIn structures (strong first-line hook, skimmable body, one clear idea, concrete takeaway), enforces that every factual claim is source-backed, self-reviews against a quality rubric, and finishes with the ai-slop-killer pass. Outputs the post plus 2-3 alternative hooks. Trigger on "write a LinkedIn post," "draft a LinkedIn post about X," "turn this into a LinkedIn post," "make a LinkedIn post," "LinkedIn post from this article," or "repurpose this for LinkedIn."
---

# LinkedIn Post Builder

One job: turn a topic (or a source document) into a LinkedIn post that people stop for, read to the end, and save — grounded in real research, not vibes. The differentiator is research quality: this skill gathers real facts and citable sources first, then writes, and never ships a factual claim it can't source.

Read the three reference files before writing. They hold the detail this file only points to:

- `reference/research-checklist.md` — how to run the research phase and log sources.
- `reference/hook-library.md` — proven hook patterns with fill-in templates.
- `reference/formatting-guide.md` — structure, length, formatting, and the 2026 algorithm rules.
- `reference/quality-rubric.md` — the pre-publish scorecard.

## The loop: Research → Draft → Review → Deliver

### 1. Research (do not skip — this is the point)

Follow `reference/research-checklist.md`. In short:

- Establish the **angle** and the **one idea** the post will make. One post = one argument.
- Run web searches to gather facts, numbers, examples, and counter-arguments. Fetch primary sources where you can (original study, company release, docs) rather than trusting a summary.
- Build a **source log**: every factual claim → a URL. Prefer primary sources and recent ones.
- If a claim can't be sourced, cut it or reframe it as clearly-labeled opinion.

If a source document was provided (an article, transcript, draft), still research to verify its claims and find the sharpest, most current angle — do not just compress the input.

### 2. Draft

- **Hook first (top ~210 characters).** The opening 1-2 lines decide whether anyone expands the post. Draft 3 hooks from `reference/hook-library.md`, lead with the strongest, keep the other two for the alternates.
- **Body: skimmable, one idea.** Short paragraphs, one to two sentences each, hard line breaks, white space. Deliver the value in the post itself — LinkedIn suppresses reach for posts that push readers off-platform, so this is "zero-click": ~80% of the value lives in the post.
- **Concrete takeaway.** End with one specific, usable thing the reader can act on.
- **Soft engagement close.** A genuine question or invitation to add experience — never "comment 'YES' below" or engagement-bait, which is now penalized.
- **Cite claims naturally.** In-post, weave the source into the sentence ("A 2026 [Org] study found…"). Put full URLs in a sources block for the human, and put any link the post references in the first comment, not the body.
- Follow every length and formatting rule in `reference/formatting-guide.md`. Target ~1,300-1,900 characters unless the format calls for otherwise.

### 3. Review

- Score the draft against `reference/quality-rubric.md`. Fix anything under bar before moving on.
- **Every factual claim maps to a source in the log.** If it doesn't, cut or soften it. This check is non-negotiable.
- **Final pass: run the `ai-slop-killer` skill on the post copy.** This is required — it strips AI tells (negative parallelism, rule-of-three pile-ups, em-dash overuse, corporate-AI vocabulary, engagement-bait cadence) and reports what it changed. The post is not done until it has passed ai-slop-killer.

### 4. Deliver

Output in this order:

1. **The post** — ready to paste, formatted with the intended line breaks.
2. **2-3 alternative hooks** — the other openers from step 2, so the human can A/B them.
3. **First-comment link** (if the post references a link).
4. **Sources** — the claim → URL log, so the human can verify.
5. One line: rubric score and confirmation that ai-slop-killer ran.

## Voice / config (optional, don't hardcode a person)

This skill is brand- and person-neutral by default. If the human names a voice skill, a brand style guide, or a `voice.config.md` / `slop.config.md` in the working directory, honor it (tone, banned words, whether emoji/hashtags are allowed, citation strictness). With nothing specified, write in a clear, credible, professional-but-human voice, use 0-3 topical hashtags at the very end, and keep emoji minimal or off.

## Series mode

If the topic is too big for one post, say so and propose a 2-4 post series: one idea per post, each standalone, sequenced from hook-worthy to deep. Research once, then draft each post through the same loop.
