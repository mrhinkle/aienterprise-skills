---
name: newsletter-tactic
description: >
  Produce a short single-tactic newsletter edition that hands decision-makers
  one copy-paste artifact (a prompt, template, or config) they can use in under
  ten minutes: research the angle, draft under a hard word cap, score a
  100-point rubric, run an expert-panel critique, and stage it for human
  approval. Use when the user says "write the tactic," "this week's tactic,"
  "one-tactic edition," "Wednesday newsletter," "give readers a prompt they can
  copy," "run the expert panel," or names the tactic edition from their
  newsletter config.
---

# Newsletter Tactic

You produce the tactic edition. The reader is an executive or senior manager
who wants one concrete edge they can put to work today. This is not a news
roundup and not a tutorial. It is a single tactic, handed over as something the
reader can copy and use. **The artifact is the edition.**

## Step 0 — Load the config

Read the newsletter config (lookup order and fields in
`reference/newsletter.config.example.md`). Use `publication.*`, `voice.*`,
`banned_words`, `banned_phrases`, `citations.*`, `sources.*`, `staging.*`, and
`editions.tactic.*`. If no config exists, use the defaults and ask only for the
publication name. If `voice.style_file` is set, read it now.

## Pipeline

1. **Research** — find one tactic worth a leader's ten minutes.
2. **Draft** — the structure in `reference/structure.md`, under the word cap.
3. **Review** — prose pass, rubric, then the expert panel
   (`reference/review-rubric.md`, `reference/expert-panel.md`); fix until it
   clears `review.pass_score` (default 90).
4. **Package** — metadata and, if configured, the featured image.
5. **Stage** — write to `staging.destination` at `staging.status_value`, then stop.

## Step 1 — Research

Scan the last `sources.freshness_days` days (default 7) for one specific,
usable advantage: a new agent or feature, a prompt pattern, a workflow. Search
across the beat's product launches, productivity workflows, and prompt
patterns.

Filter every candidate:

1. **Usable today?** Can the reader paste something and get a result in under
   `editions.tactic.act_within_minutes` (default 10)?
2. **An advantage?** A concrete edge, not just awareness.
3. **Distinct from the week's other editions?** If the publication also runs a
   tutorial or a deep dive, this one is the tactic. Don't overlap.

Pick **one** angle. Prefer recency, then specificity, then measurable impact.

## Step 2 — Draft

Follow `reference/structure.md`: title, italic subtitle naming the deliverable,
one first-person intro paragraph, the artifact in a plain code block, a sample
output, "What changes," "Where else this works," and a short news-hook close.

Writing rules:

- The artifact must work when pasted with its `[BRACKETED]` fill-ins completed.
- Open on the reader's problem in the first sentence. No preamble; nothing from
  `banned_phrases`.
- Prompts and templates go in plain code blocks with no language tag (some
  email platforms render tagged blocks badly).
- Name tools by brand, not version number, in body copy. If a version is the
  news, put it in the linked source.
- Stay under `editions.tactic.words.max` (default 750). This is a hard cap. If it
  runs long, cut.

## Step 3 — Review

1. Run the `ai-slop-killer` skill (or `voice.final_prose_pass_skill`). Then
   check `banned_words`, `banned_phrases`, and `spelling_rules`.
2. Verify the news hook and every claim with web searches; test the artifact
   if you can.
3. Score `reference/review-rubric.md`.
4. Run the panel in `reference/expert-panel.md`. Apply every Must Fix and Should
   Fix; show Nice to Have items to the user.
5. Re-score. Below the pass score after `review.max_revision_rounds`, stop and
   show what is open.

## Voice rules

- Follow `voice.style_file` and `voice.author_persona`; use `voice.voice_skill`
  if set. Tactic voice is a coach: direct, energizing, no filler.
- Use `voice.kicker_prefix` lightly, mainly in bolded callouts. Don't force
  section labels onto a form this short.
- Every factual claim carries a citation in `citations.style`.

## Step 4 — Package

Produce every field in `metadata.fields` (title, subtitle, two subject lines,
preview text, SEO title and meta description within limits, kebab-case slug).
Draft one social post per `metadata.social_posts` entry, leading with the
artifact's payoff. If `images.skill` is set, generate the featured image.

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

- `reference/structure.md` — the edition skeleton
- `reference/review-rubric.md` — the 100-point rubric and auto-fails
- `reference/expert-panel.md` — the panel roles and how to sort their notes
- `reference/newsletter.config.example.md` — every config field and default
