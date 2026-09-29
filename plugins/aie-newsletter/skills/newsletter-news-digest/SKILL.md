---
name: newsletter-news-digest
description: >
  Produce a weekly news-digest newsletter edition: research the past week's
  top stories on your beat from a wide set of sources, write a Big Story, quick
  hits, tools, and an extra read with every link pointing to a canonical source,
  score it on a 100-point rubric, and stage it for human approval. Use when the
  user says "write the news digest," "this week's digest," "Monday edition,"
  "round up this week's AI news," "research the week's news for the
  newsletter," or names the digest edition from their newsletter config.
---

# Newsletter News Digest

You produce the weekly news digest. The reader scans several newsletters before
work and needs to brief a colleague from the highlights. Every line earns its
place or gets cut.

## Step 0 — Load the config

Read the newsletter config (lookup order and every field are in
`reference/newsletter.config.example.md`). Use `publication.*`, `voice.*`,
`banned_words`, `citations.*`, `sources.*`, `staging.*`, and
`editions.news_digest.*`. If no config exists, use the example defaults and ask
only for the publication name. If `voice.style_file` is set, read it now.

## Pipeline

Five steps. Never skip the review.

1. **Research** — scan the week, pick the stories, find canonical links.
2. **Draft** — write the edition in the structure in `reference/structure.md`.
3. **Review** — prose pass, then score the rubric in `reference/review-rubric.md`;
   fix until it clears `review.pass_score` (default 90).
4. **Package** — metadata and, if configured, the featured image.
5. **Stage** — write to `staging.destination` at `staging.status_value`, then stop.

## Step 1 — Research

Find 8–12 candidate stories from the last `sources.freshness_days` days
(default 7), then choose the best fit for each section. Run many web searches
across the beat: model or product releases, funding, launches, policy,
infrastructure, controversies.

Also check:

- Major updates to apps in `sources.apps_readers_use`. A big update to a tool
  readers already use beats an obscure launch.
- Launch trackers and tool directories for new tools with a clear business use
  case. Skip demos and research toys.

**Freshness.** The Big Story and every Quick Hit fall inside the freshness
window. Tools and the Extra Read can be older.

**Source attribution — the most important editorial rule.** Research *from*
the places in `sources.scan_for_leads`, but every link in the edition points to
a canonical source: the company blog, the official announcement, the filing, or
a tier-1 outlet from `citations.tier_one_outlets`. Never link to anything in
`citations.never_link_to`. Readers cite these links in meetings.

## Step 2 — Draft

Follow `reference/structure.md` exactly: opening paragraph, Key Takeaways, the
Big Story, numbered Quick Hits, Tools, Extra Read. Counts and section labels come
from `editions.news_digest.counts` and `.labels`. Output clean markdown for
`publication.platform` — no HTML, no inline images.

Stay inside `editions.news_digest.words` (default 900–1,200).

## Step 3 — Review

1. Run the `ai-slop-killer` skill (or `voice.final_prose_pass_skill`) over the
   draft. Then check `banned_words`, `banned_phrases`, and `spelling_rules`.
2. Verify every factual claim with a web search against its primary source.
3. Score the draft with `reference/review-rubric.md`. Below the pass score: fix
   the flagged items and re-score, up to `review.max_revision_rounds`. If it
   still fails, stop and show the user what is open.

## Voice rules

- Follow `voice.style_file` and `voice.author_persona`. If `voice.voice_skill`
  is set, use it.
- Numbers build credibility. Active voice, present tense for current events.
  State trade-offs plainly.
- Section labels use `voice.kicker_prefix` (default `// `).
- Every factual claim carries a citation in `citations.style`. No exceptions.

## Step 4 — Package

Produce every field in `metadata.fields`: the title, the subtitle (the week's
through-line from the opening paragraph), two subject lines, preview text, SEO
title and meta description within the configured limits, and a kebab-case slug.
Draft one social post per entry in `metadata.social_posts`, each built from a
Key Takeaway. If `images.skill` is set, generate the featured image with it.

## Step 5 — Stage, then stop

Staging is the approval gate. Per `staging.destination`:

- **file** — write `{staging.file_dir}/{publish-date}-{slug}.md` with the
  metadata as YAML front matter and the edition as the body.
- **notion** / **cms** — only if that connector is available in the session.
  Find or create the entry in `staging.notion_database` or
  `staging.cms_collection`, matching on `staging.match_on` so you update rather
  than duplicate. Set `edition_type_field` to the edition name,
  `review_score_field`, the metadata, and `status_field` =
  `staging.status_value`. Put the full edition in the body. If the connector is
  missing, fall back to **file** and say so.

**Then stop.** A human reviews and approves. If `staging.publish_handoff` is set,
mention it as the next step; never send or schedule the email yourself.

## Reference

- `reference/structure.md` — the edition skeleton and section guide
- `reference/review-rubric.md` — the 100-point rubric, auto-fails, and traps
- `reference/newsletter.config.example.md` — every config field and default
