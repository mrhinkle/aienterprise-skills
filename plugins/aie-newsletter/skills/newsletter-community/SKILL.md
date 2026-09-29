---
name: newsletter-community
description: >
  Produce a community or event newsletter edition: a hero and personal opening
  note, an optional ticket or offer callout, a feature article, a secondary
  article, and an upcoming-events roundup pulled from your Meetup, Luma, or
  Eventbrite groups with links to each canonical event page. Delivers SEO and
  email metadata separately and stages the edition for human approval. Use when
  the user says "write the community newsletter," "draft the event newsletter,"
  "round up upcoming meetups," "put together this month's community edition,"
  or names the community edition from their newsletter config.
---

# Newsletter Community

You produce the community newsletter: the edition a meetup group, user
community, or conference sends to its members. Its job is belonging and action:
every section moves the reader to show up, sign up, or share.

## Step 0 — Load the config

Read the newsletter config (lookup order and fields in
`reference/newsletter.config.example.md`). Use `publication.*`, `voice.*`,
`banned_words`, `citations.*`, `metadata.*`, `staging.*`, and
`editions.community.*`. If no config exists, use the defaults and ask only for
the publication name. If `voice.style_file` is set, read it now.

## Workflow

1. **Ask for the opening.** Ask the user for this edition's theme or opening
   message, plus the topics of the feature and secondary articles if they have
   them. This is the one question you always ask; the opening is the organizer's
   own note.
2. **Gather events.** For each URL in `editions.community.event_sources`, pull
   upcoming events inside `event_window_days` (default 45). Collect the
   **canonical event page URL** for each event, never the group homepage. If no
   sources are configured, ask for them or skip the section.
3. **Draft** every section in the order in `reference/structure.md`, using
   `reference/newsletter-template.md` as the skeleton.
4. **Images.** If `images.skill` is set, generate one image per article and one
   for events. Use `editions.community.hero_image` as the hero if set; don't
   generate a hero.
5. **Review.** Run the `ai-slop-killer` skill (or `voice.final_prose_pass_skill`),
   check `banned_words` and `spelling_rules`, verify every date, price, and link,
   then score `reference/review-rubric.md` to `review.pass_score`.
6. **Metadata, separately.** Slug, preview text, and meta description go to the
   user alongside the edition, never inside the newsletter body (see below).
7. **Stage, then stop** (see below).

## Section rules (summary)

Full rules are in `reference/structure.md`.

- **Title** — a short, declarative line (about 33 characters is a good target)
  that makes the reader curious or offers clear value. Title Case, periods not
  exclamation marks. Never a date-based title.
- **Subtitle** — an italic line that teases this edition's content, not a
  generic tagline.
- **Opening** — flows straight from the subtitle with no heading. It is the
  organizer's personal note: warm, conversational, first person plural. Use
  italic plus bold italic for the key ask.
- **Promo callout** — only if `promo_block.enabled`. Bulleted list, never a
  table.
- **Feature article** — the article title is the H2. Never prefix it with
  "Feature Article:". 3–5 paragraphs with relevant links. When listing sessions
  or workshops, link both the session name and the instructor.
- **Secondary article** — shorter (2–3 paragraphs), same heading rule, strong
  call to action.
- **Upcoming Events** — bulleted list sorted by date, earliest first. Month and
  day names spelled out in full. Event titles link to the canonical event page.
- **Sign-off** — `editions.community.sign_off` in regular text. No signatures;
  the email platform adds those.

## Voice rules

- Follow `voice.style_file` and `voice.author_persona`. Community voice: a
  knowledgeable friend. Enthusiastic without being salesy; "we" and "you."
- Tables are never used in the body; use bulleted lists.
- Every factual claim (dates, prices, speaker credentials, stats) is cited or
  links to the page that states it.

## Metadata (delivered separately)

Give the user, outside the newsletter body:

- **Slug** — short, keyword-focused, no dates, no "newsletter"
- **Preview text** — starts with `metadata.preview_text_prefix` if set
- **Meta description** — one or two sentences for search engines

If the user wants social posts, follow `reference/social-posts.md`.

## Stage, then stop

Per `staging.destination`:

- **file** — write `{staging.file_dir}/{publish-date}-{slug}.md` with metadata
  as YAML front matter and the edition as the body. Save images beside it.
- **notion** / **cms** — only if that connector is available. Find or create the
  entry in `staging.notion_database` or `staging.cms_collection`, matching on
  `staging.match_on`, set `status_field` = `staging.status_value`, full edition
  in the body. If the connector is missing, fall back to **file** and say so.

**Then stop.** A human approves. Never send or schedule the email yourself.

## Reference

- `reference/structure.md` — full section-by-section rules
- `reference/newsletter-template.md` — the markdown skeleton
- `reference/review-rubric.md` — the 100-point rubric and auto-fails
- `reference/social-posts.md` — LinkedIn and social post rules
- `reference/newsletter.config.example.md` — every config field and default
