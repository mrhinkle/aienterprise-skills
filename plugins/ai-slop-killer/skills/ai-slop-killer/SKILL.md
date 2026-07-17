---
name: ai-slop-killer
description: The final anti-AI-slop editing pass for any drafted or revised prose — blog posts, newsletters, LinkedIn/social, emails, marketing and web copy, documentation, essays, fiction. Detects documented AI writing tells (negative parallelism "not X, it's Y," rhetorical Q&A, rule-of-three and anaphora pile-ups, em-dash and unicode overuse, corporate-AI vocabulary, wind-up intros and signposted conclusions, bold-first-bullet listicles, low-burstiness rhythm, hedging, vague attributions, participial "-ing" filler, grandiose stakes, invented concept labels), scores the passage, rewrites in place, and reports what it caught. Runs LAST, after any other writing or editing skill. Trigger on "clean this," "de-slop," "kill the AI slop," "copyedit this for AI tells," "does this sound like AI," "make this sound human," "humanize this," or automatically after any skill produces prose meant to be published.
---

# AI Slop Killer

The last skill to touch prose before it ships. Whatever drafted or revised it, this runs the passage through one job: make it read like a person wrote it on purpose, then prove what it removed. Works on any genre — business writing, marketing, docs, essays, fiction.

The pattern catalog is built from documented sources (Wikipedia's *Signs of AI writing*, the tropes.fyi directory, working editors' guides — see `reference/slop-catalog.md`), not one person's taste. It ships with sensible defaults and an optional per-user config for house rules.

## The loop: Detect → Score → Fix → Prove

1. **Read the passage cold**, start to finish, before touching anything. Slop clusters — you're looking for stacked tells, not one stray word.
2. **Detect.** Run every check in `reference/slop-catalog.md`. Match on the *pattern*, not exact wording. A single instance of most tells is human; the tell is the *repetition and clustering*.
3. **Score.** Compute the slop score using `reference/scoring.md`. If it's ≤5 per 500 words, say "clean" in one line and stop — don't manufacture edits.
4. **Fix in place.** Rewrite the tells. Preserve the author's meaning and voice. If a voice/style skill or a config is available (see below), honor it. Never flatten a correct term of art into vagueness.
5. **Prove.** Return the cleaned passage, then the before→after score and an itemized list of what was cut and why — plus anything left in on purpose.

## The non-negotiables

- **Kill negative parallelism** — "It's not X, it's Y," "not because X but because Y," "The question isn't X. The question is Y." The single most-cited AI tell. At most one earned instance per piece.
- **Cut structural scaffolding.** Wind-up intros ("In today's fast-paced world…"), signposted conclusions ("In conclusion," "At the end of the day"), false-suspense transitions ("Here's the kicker," "Here's the thing"), and rhetorical-question pivots ("The result? Devastating."). Delete and start at the real sentence — the true article usually starts in paragraph two.
- **Break the rhythm.** No stacked rule-of-three triplets, no anaphora (three sentences opening the same way), no page of same-length "rectangle" paragraphs. Vary sentence length hard (long, explanatory sentence → short punch). This is *burstiness*, the thing readers and detectors both notice.
- **Two weights of emphasis, used sparingly.** No paragraph that's mostly em-dashes (a human uses 2–3 per piece, not 20). No bold-first-bullet on every list item. Normalize curly/straight quotes and stray unicode arrows.
- **Plain words beat AI vocabulary.** Replace the documented offenders (delve, leverage, robust, seamless, tapestry, landscape, realm, testament, elevate, harness, streamline, foster, pivotal, myriad…) with a concrete noun or an active verb. The pub test: would you say this to a colleague over a beer?
- **Substance, not fake authority.** No vague attributions ("experts say," "studies show") without a named source. No grandiose stakes inflation. No invented concept labels ("the supervision paradox") used as if they're established terms. No fake first-person experience ("Picture this…").
- **Watch the humanizer over-correction.** Thesaurus salad ("paramountly significant") from de-detection tools is its own tell. If a word makes the sentence harder to say aloud, revert it.

## Don't over-correct

One em-dash, one triad, one rhetorical question, one metaphor per piece is human. Deliberate fragments, real lists of real steps, correct technical terms, and a genuine strong stance all stay. The failure mode cuts both ways: leaving obvious machine cadence, OR scrubbing prose until it's beige and voiceless. Aim for lived-in, not sanitized.

## Config (optional, for house rules)

If a file named `slop.config.md` exists in the working directory or alongside the content, load it. It can define:

- **`banned_words:`** extra words to hard-ban on top of the defaults (e.g., a brand's forbidden list).
- **`allowed_words:`** documented-tell words this author legitimately uses (removes false positives).
- **`voice:`** the name of a voice/style skill to preserve (e.g., a personal or brand voice skill), or a short voice note.
- **`citations:`** `required` | `preferred` | `off` — whether every factual claim needs an inline source.
- **`channel_defaults:`** per-channel tweaks (e.g., allow emoji in social, forbid in docs).

With no config, defaults apply: standard documented banlist, citations `preferred`, preserve whatever voice the text already has.

## Fiction mode

Say "fiction mode" or run this on manuscript prose. Adds the section-7 checks in the catalog: one negative-parallelism per *book* max, don't explain a metaphor after the scene already made it, don't beat one metaphor to death (the "dead metaphor" trope), prefer real checkable texture over invented brand names, and catch paste artifacts (duplicated/garbled sentences). Series-specific metaphor limits belong in `slop.config.md`.

## Output

```
Slop score: N → M  (per 500 words)

[cleaned passage]

Cut / fixed:
- [pattern] xN — [what you did]
...

Left on purpose:
- [thing] — [why]
```

If clean on first read: one line saying so, with the score. Stop.

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
