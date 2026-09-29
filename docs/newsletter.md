# Newsletter skills

The `aie-newsletter` plugin ships five skills that research, draft, review, and
stage newsletter editions. Each one covers a different edition format, and all
five read one shared config file for your house rules, so you can run a single
format or a full weekly schedule.

Every skill follows the same pipeline:

1. **Research** with live web searches. Nothing is trusted from training data.
2. **Draft** to a fixed section structure.
3. **Review**: an `ai-slop-killer` prose pass, a banned-word check, fact
   verification, and a 100-point rubric. Below the pass score (default 90), the
   skill fixes and re-scores.
4. **Package** the metadata: subject lines, preview text, SEO fields, slug, and
   social drafts.
5. **Stage** for human approval, then stop. No skill sends or schedules email.

Two rules hold in every skill and can't be turned off: **every factual claim is
cited**, and **a failing edition is never staged**.

## Setup

1. Install the plugin.
2. Copy `reference/newsletter.config.example.md` from any of the five skills
   (the copies are identical) to `newsletter.config.md` at your project root,
   or to `~/.claude/newsletter.config.md` to use it across projects.
3. Set at least `publication.name`. Everything else has a default.
4. Optional: point `voice.style_file` at your own style guide, and make sure the
   `ai-slop-killer` skill is installed for the final prose pass.

If no config exists, the skills run on defaults and ask only for the publication
name.

### Config at a glance

| Block | What it controls |
|---|---|
| `publication` | Name, URL, beat, audience, platform (Beehiiv, Substack, Ghost, Kit, Mailchimp, other), timezone |
| `voice` | Style-file path, optional voice skill, persona, kicker prefix, emoji policy, final prose-pass skill |
| `banned_words`, `banned_phrases`, `spelling_rules` | Your house list; any banned word is an auto-fail |
| `citations` | Citation style, primary-source rule, sources never to link, tier-one outlets, deep-dive source minimum |
| `sources` | Where to scan for leads, what counts as canonical, apps your readers use, freshness window |
| `images`, `metadata` | Optional image skill; metadata fields, limits, social channels |
| `review` | Pass score and revision rounds |
| `staging` | Destination: a markdown file, or your CMS/Notion database if connected; status field and value; optional publish handoff |
| `editions.*` | Per-format name, send day, word range, counts, and labels |

---

## newsletter-news-digest

**What it does.** Builds a weekly news roundup for your beat: an opening
through-line, five Key Takeaways, one Big Story, four Quick Hits, three Tools,
and one Extra Read. You can research from other newsletters and aggregators,
but every published link points to a canonical source. A concentration rule
stops a single company from taking over the edition.

**Use it.** "Write this week's news digest." "Round up the week's AI news for
the newsletter." "Monday edition."

**Inputs and outputs.**

- In: the config; optionally a theme or stories you want included.
- Out: a platform-ready markdown edition (default 900–1,200 words), a review
  score with any fixes applied, the metadata package, and social drafts, all
  staged at your review status.

**Configure.** `editions.news_digest` sets the counts, section labels, tagline,
word range, and concentration limit (default 40%). `sources.*` sets where to
look and what to cite. `citations.never_link_to` lists the sources you research
from but never link to.

---

## newsletter-tutorial

**What it does.** Teaches one skill the reader can use the same day. The
edition runs: kicker, "How to" title, a first-person hook, an action subhead, a
bolded Takeaway, a CTA with an honest cost line, a "real shift" reframe, a
numbered procedure checked against the tool's current docs, an optional bonus,
and a why-now close. It never invents a personal anecdote. It asks you for one.

**Use it.** "Write the tutorial on setting up project memory." "This week's
lesson." "Teach readers how to do X with AI."

**Inputs and outputs.**

- In: the config, a skill or topic (or let it pick one), and your real story
  for the hook.
- Out: a markdown edition (default 1,000–1,500 words) with a checked
  procedure, a review score, metadata, and social drafts, staged for approval.

**Configure.** `editions.tutorial` sets the name, day, and word range. Kicker
labels come from `voice.kicker_prefix`.

---

## newsletter-tactic

**What it does.** A short edition built around one copy-paste artifact (a
prompt, template, or config) a senior reader can use within ten minutes. It
includes a sample output, "What changes," "Where else this works," and a
news-hook close. After the rubric, an eight-seat expert panel critiques the
draft: platform operator, growth marketer, copy chief, morning-read editor,
conversion specialist, growth analyst, deliverability lead, and reader
advocate. Notes are sorted into Must Fix, Should Fix, and Nice to Have.

**Use it.** "Write this week's tactic." "Give readers a prompt they can copy for
meeting prep." "Run the expert panel on this draft."

**Inputs and outputs.**

- In: the config; optionally an angle or a tool that just shipped.
- Out: a markdown edition under the hard word cap (default 350–750), the
  panel's sorted notes with Must and Should Fix items applied, a review score,
  metadata, and social drafts, staged for approval.

**Configure.** `editions.tactic.words.max` is a hard cap. `act_within_minutes`
sets the "usable today" bar. `expert_panel` replaces the default seats with
your own roles or named public experts.

---

## newsletter-deep-dive

**What it does.** A long-form strategic analysis of one hard business question
for executives. It checks that the topic has enough evidence, gathers at least
five primary sources, and offers three title options. The edition runs: an
Executive Summary that stands alone, a first-person narrative hook, analysis
under question subheads (with bull and bear cases when the topic is contested),
four Common Missteps, four Key Takeaways, and a playbook close.

**Use it.** "Write the deep dive on agent governance costs." "The long read this
week." "Unpack this topic for executives."

**Inputs and outputs.**

- In: the config, a topic, your pick among the proposed titles, and your story
  for the hook.
- Out: a markdown edition (default 2,500–4,000 words; executive summary
  220–320) with inline citations, a review score, metadata, and social drafts,
  staged for approval.

**Configure.** `editions.deep_dive` sets the word ranges, missteps and takeaway
counts, number of title options, and `signature_hook` (your recurring way into a
topic). `citations.min_sources_deep_dive` sets the source floor.

---

## newsletter-community

**What it does.** A member newsletter for a meetup group, user community, or
conference. It runs: hero and mission line, the organizer's opening note, an
optional ticket or offer callout, a feature article, a secondary article, an
Upcoming Events roundup pulled from your event pages, and your sign-off. Each
event links to its own event page, never the group homepage. Slug, preview
text, and meta description come back separately, outside the body.

**Use it.** "Write this month's community newsletter." "Draft the event
newsletter and round up upcoming meetups."

**Inputs and outputs.**

- In: the config, your opening theme (it always asks), and optional article
  topics.
- Out: a markdown edition built from the bundled template, a sorted events
  list, separate SEO and email metadata, optional social posts, and images if an
  image skill is configured, staged for approval.

**Configure.** `editions.community` sets the mission tagline, hero image, promo
block (heading, CTA, items), event sources (Meetup, Luma, Eventbrite URLs),
event window, key links, sign-off, and reshare ask. Set
`metadata.preview_text_prefix` if you open preview text with emojis.
