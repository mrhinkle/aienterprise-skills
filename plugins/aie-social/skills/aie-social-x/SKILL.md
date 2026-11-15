---
name: aie-social-x
description: Produce a high-quality X (Twitter) post or thread on any topic for any brand or person. Researches the topic to gather facts and citable sources, decides single-post vs thread, drafts a scroll-stopping hook and one-idea-per-post body tuned to X's character limits and 2026 algorithm, backs every factual claim with a source, self-reviews against a quality rubric, and finishes with the ai-slop-killer pass. Outputs the post/thread plus 2-3 alternative hooks. Trigger on "write an X post," "make a thread," "draft a tweet," "turn this into a thread," "X thread about X," "post this on X," or "repurpose this for Twitter/X."
---

# X Post & Thread Builder

One job: turn a topic (or a source document) into an X post or thread that stops the scroll, gets read, and gets replies and reposts — grounded in real research. Same research-then-draft-then-review discipline as the LinkedIn skill, tuned to X: tight character budgets, one idea per post, and a hook that has ~1.5 seconds to work.

Read the reference files before writing:

- `reference/research-checklist.md` — research phase and source log.
- `reference/hook-library.md` — X hook patterns with fill-in templates.
- `reference/formatting-guide.md` — character limits, single-vs-thread decision, thread structure, 2026 algorithm rules.
- `reference/quality-rubric.md` — the pre-publish scorecard.

## The loop: Research → Decide format → Draft → Review → Deliver

### 1. Research (do not skip)

Follow `reference/research-checklist.md`:

- Nail the **one idea**. On X, one idea per post — and a thread is one idea developed across posts, not five ideas stapled together.
- Web-search for facts, numbers, examples, and counter-takes. Fetch primary sources; don't trust paraphrases.
- Build a **source log**: every factual claim → URL. If you can't source it, cut it or label it clearly as opinion. Never invent a stat, study, or quote.

If a source doc was provided, verify it and find the sharpest current angle rather than just trimming it to fit.

### 2. Decide single post vs thread

Use `reference/formatting-guide.md`. Quick rule:

- **Fits in one post (under 280 chars) with a complete point → post a single.** Threads have a drop-off cost per post.
- **3+ distinct supporting points, a step-by-step, a story, or a list → thread** (sweet spot 5-9 posts). Threads win on dwell time and replies but only if each post earns the next tap.

State the call and why before drafting.

### 3. Draft

- **Hook post is everything.** It must stand alone and earn engagement by itself — a bold claim, a surprising number, or a specific promise. Draft 3 hooks from `reference/hook-library.md`; lead with the strongest.
- **One idea per post.** Each body post is a complete thought — a tip, step, data point, or example — readable in isolation. Never cram.
- **Respect the 280-char limit per post** (see formatting guide for verified/Premium longer-post nuance; default to 280 so it's universal).
- **Close with a real CTA** on the last post: follow for more on the topic, or "repost if this helps someone." No engagement-farming ("like if you agree, RT if you disagree" is suppressed).
- **Links go in a reply, not the hook.** External links in the main post suppress reach. Put the link in the final post or a reply, and say it's there.
- **Cite in-line lightly** ("per a 2026 [Org] study") and keep the full source log for the human.

### 4. Review

- Score against `reference/quality-rubric.md`. Fix failures.
- **Every factual claim maps to a source.** Non-negotiable.
- **Final pass: run the `ai-slop-killer` skill** on the full post/thread text. Required — it strips AI tells and engagement-bait cadence and reports what it changed. Not done until it passes.

### 5. Deliver

Output in this order:

1. **The post or thread** — numbered (1/, 2/, …) if a thread, each post within the character budget, ready to paste.
2. **2-3 alternative hooks** for the opener.
3. **Link placement note** (which reply the link goes in), if any.
4. **Sources** — claim → URL log.
5. One line: rubric score, format decision, and ai-slop-killer confirmation.

## Voice / config (optional, don't hardcode a person)

Brand- and person-neutral by default. If the human names a voice skill, brand style guide, or a `voice.config.md` / `slop.config.md`, honor it (tone, banned words, emoji, hashtag policy, citation strictness). With nothing set: clear, punchy, credible; 0-1 hashtag max; emoji sparing.

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
