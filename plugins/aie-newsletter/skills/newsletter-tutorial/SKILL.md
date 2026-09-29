---
name: newsletter-tutorial
description: >
  Produce a tactical-tutorial newsletter edition that teaches the reader one
  skill they can apply the same day: pick the skill, verify every step against
  the tool's current behavior, write a hook, takeaway, and numbered procedure,
  score it on a 100-point rubric, and stage it for human approval. Use when the
  user says "write the tutorial," "this week's lesson," "the how-to edition,"
  "Tuesday newsletter," "teach readers how to do X with AI," or names the
  tutorial edition from their newsletter config.
---

# Newsletter Tutorial

You produce the tutorial edition. Each one teaches **one** skill the reader can
apply the same day. It is a tactical how-to, not a news roundup and not a
strategic analysis. The reader wants to be better at something by the time they
finish reading.

## Step 0 — Load the config

Read the newsletter config (lookup order and fields in
`reference/newsletter.config.example.md`). Use `publication.*`, `voice.*`,
`banned_words`, `citations.*`, `staging.*`, and `editions.tutorial.*`. If no
config exists, use the defaults and ask only for the publication name. If
`voice.style_file` is set, read it now.

## Pipeline

Five steps. Never skip the review.

1. **Research** — pin down the skill; verify the steps work as written today.
2. **Draft** — write the edition in the structure in `reference/structure.md`.
3. **Review** — prose pass, then score `reference/review-rubric.md`; fix until
   it clears `review.pass_score` (default 90).
4. **Package** — metadata and, if configured, the featured image.
5. **Stage** — write to `staging.destination` at `staging.status_value`, then stop.

## Step 1 — Research

Pick one skill the reader can put to work today: a setting to fix, a workflow to
adopt, a feature to use well. Menus, settings, tiers, and limits change fast.
Run web searches against the vendor's current docs and verify the procedure
step by step instead of trusting training data.

Filter every candidate through three questions:

1. **Can the reader do it today?** A tutorial teaches a repeatable skill, not an
   idea to admire.
2. **Is there a real procedure?** Concrete, numbered steps the reader runs
   themselves.
3. **Is it distinct from the week's other editions?** If the publication also
   runs a tactic edition (one copy-paste move) or a deep dive (analysis), this
   one is the tutorial. Don't overlap.

## Step 2 — Draft

Follow `reference/structure.md`: kicker, how-to title, first-person hook, action
subhead, the takeaway, CTA with honest micro-copy, the "real shift" callout,
explanation, the numbered procedure, optional bonus, and a why-now close.

Stay inside `editions.tutorial.words` (default 1,000–1,500). Output clean
markdown for `publication.platform`.

The hook is first person and specific: a real problem the author hit. If you do
not have one from the user or the style file, ask for it in one line rather
than inventing an anecdote. Never fabricate a personal story.

## Step 3 — Review

1. Run the `ai-slop-killer` skill (or `voice.final_prose_pass_skill`). Then
   check `banned_words`, `banned_phrases`, and `spelling_rules`.
2. Re-verify the procedure and every claim with web searches.
3. Score with `reference/review-rubric.md`. Below the pass score: fix and
   re-score, up to `review.max_revision_rounds`, then stop and show what is open.

## Voice rules

- Follow `voice.style_file` and `voice.author_persona`; use `voice.voice_skill`
  if set. The best tutorial voice is the teacher who made the mistake first.
- Labels use `voice.kicker_prefix`: `{K}{edition name}`, `{K}The Takeaway:`,
  `{K}The real shift:`.
- Every factual claim, setting name, and product behavior carries a citation in
  `citations.style`, pointing at the vendor's docs or another primary source.

## Step 4 — Package

Produce every field in `metadata.fields` (title, subtitle, two subject lines,
preview text, SEO title and meta description within limits, kebab-case slug).
Draft one social post per `metadata.social_posts` entry, built from the
takeaway. If `images.skill` is set, generate the featured image with it.

## Step 5 — Stage, then stop

Per `staging.destination`:

- **file** — write `{staging.file_dir}/{publish-date}-{slug}.md` with metadata
  as YAML front matter and the edition as the body.
- **notion** / **cms** — only if that connector is available. Find or create the
  entry in `staging.notion_database` or `staging.cms_collection`, matching on
  `staging.match_on`. Set `edition_type_field`, `review_score_field`, the
  metadata, and `status_field` = `staging.status_value`. Full edition in the
  body. If the connector is missing, fall back to **file** and say so.

**Then stop.** A human approves. Mention `staging.publish_handoff` if set; never
send or schedule the email yourself.

## Reference

- `reference/structure.md` — the edition skeleton and section guide
- `reference/review-rubric.md` — the 100-point rubric and auto-fails
- `reference/newsletter.config.example.md` — every config field and default
