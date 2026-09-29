---
name: newsletter-deep-dive
description: >
  Produce a long-form strategic-analysis newsletter edition (default 2,500–4,000
  words) that unpacks one hard business question for senior decision-makers:
  gather at least five primary sources, write an executive summary, narrative
  hook, evidence-led analysis, common missteps, and key takeaways, score it on a
  100-point rubric, and stage it for human approval. Use when the user says
  "write the deep dive," "the long read," "strategic analysis," "Thursday
  edition," "stage the deep dive," "unpack this topic for executives," or names
  the deep-dive edition from their newsletter config.
---

# Newsletter Deep Dive

You produce the deep dive: the long read. Each one unpacks **one** complex
business problem and leaves the reader thinking differently about it. The
reader is an executive or senior strategist making real decisions. This is a
strategic analysis, not a tutorial: the reader should finish thinking
differently, not doing a task differently.

Quality bar: business-journal depth, clear explanatory prose, and a narrative
that keeps a busy reader going. Every claim sourced. Every recommendation
grounded in evidence.

## Step 0 — Load the config

Read the newsletter config (lookup order and fields in
`reference/newsletter.config.example.md`). Use `publication.*`, `voice.*`,
`banned_words`, `citations.*`, `staging.*`, and `editions.deep_dive.*`. If no
config exists, use the defaults and ask only for the publication name. If
`voice.style_file` is set, read it now.

## Pipeline

Review is not optional. Never stage an edition below the pass score.

1. **Research** — gather the evidence; confirm the topic carries the weight.
2. **Draft** — write the analysis in the structure in `reference/structure.md`.
3. **Review** — prose pass, then score `reference/review-rubric.md`; fix until
   it clears `review.pass_score` (default 90).
4. **Package** — metadata and, if configured, the featured image.
5. **Stage** — write to `staging.destination` at `staging.status_value`, then stop.

## Step 1 — Research

Use web search for data, studies, industry reports, and expert analysis. Never
trust training data for statistics, pricing, or product availability; verify
everything live.

Before committing, confirm the topic carries a deep dive. It must:

- unpack **one** complex problem,
- have dense evidence (real numbers, named sources),
- support a narrative,
- be timely, and
- matter to a decision-maker.

If it is thin on evidence or too broad, narrow it or pick another.

**Sourcing.** At least `citations.min_sources_deep_dive` (default 5) unique
external sources. Priority: peer-reviewed research, then analyst and industry
reports, then tier-1 media, then official company data, then expert commentary.

**Title.** Propose `editions.deep_dive.title_options` (default 3) titles and
let the user pick. Before finalizing, check recent editions at
`publication.url` so the new title doesn't repeat a recent structure or key
words.

## Step 2 — Draft

Follow `reference/structure.md`: kicker, title, subtitle, Executive Summary
(thesis, 3–4 sourced findings, posture line), the narrative hook, organic
question subheads for the analysis, Common Missteps, Key Takeaways, and a
playbook close.

Stay inside `editions.deep_dive.words` (default 2,500–4,000).

The hook is first person. If `editions.deep_dive.signature_hook` is set (for
example "a parallel from the author's career"), use it. Get the personal detail
from the user or the style file; never fabricate one.

When the topic is contested, run both sides honestly: a bull case and a bear
case, each scored against the actual evidence. Don't pick a side the evidence
doesn't support.

## Step 3 — Review

1. Run the `ai-slop-killer` skill (or `voice.final_prose_pass_skill`). Then
   check `banned_words`, `banned_phrases`, and `spelling_rules`.
2. Verify every statistic, source, and claim with web searches. Check links
   resolve.
3. Score `reference/review-rubric.md`. Below the pass score: fix and re-score,
   up to `review.max_revision_rounds`, then stop and show what is open.

## Voice rules

- Follow `voice.style_file` and `voice.author_persona`; use `voice.voice_skill`
  if set. Deep-dive voice: a trusted advisor briefing a board.
- Labels use `voice.kicker_prefix`: the edition kicker, the section openers,
  `Key Takeaways`, and each Executive Summary finding.
- Citations follow `citations.style` (default inline links, no references
  section). Every statistic carries one.
- Emojis follow `voice.emoji_policy` (default: subject and preview only, never
  in headings or body).
- Heading levels: `#` title, `##` major sections, `###` subsections. No `####`;
  use bold text for sub-items.

## Step 4 — Package

Produce every field in `metadata.fields` (title, subtitle, two subject lines,
preview text, SEO title and meta description within limits, kebab-case slug).
Draft one social post per `metadata.social_posts` entry, built from the
Executive Summary. If `images.skill` is set, generate the featured image.

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
