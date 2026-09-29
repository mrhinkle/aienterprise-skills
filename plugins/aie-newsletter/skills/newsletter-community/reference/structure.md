# Community newsletter — structure

Sections run in this order. Settings come from `editions.community` in the
config.

## 1. Hero and opening

- **Hero** — `hero_image` if set (your logo, not a generated image), followed by
  `mission_tagline` in italics if set.
- **Title (H1)** — short and declarative, Title Case. About 33 characters is a
  good target. Make the reader curious or offer clear value. Periods, not
  exclamation marks. Never a generic date-based title.
- **Subtitle** — one italic line in regular body text (not a heading) that
  teases the edition, e.g. `*The speakers are set, the workshops are full, and
  we need your help.*`
- **Opening** — no heading. It follows the subtitle directly and is the
  organizer's personal note: warm, conversational, direct. It should read like
  the first article, not a separate "personal note" box. Use italic plus bold
  italic for the key ask, e.g. _So we have a small ask:_ _**help us spread the
  word.**_

## 2. Promo callout (optional)

Only when `promo_block.enabled` is true.

- Heading: `## {promo_block.heading}` (an emoji is fine if `voice.emoji_policy`
  allows it).
- Options as a bulleted list, never a table. Format:
  `**Option Name — $Price — Date.** Description.`
- Close with a link: `[{promo_block.cta_label} →]({promo_block.cta_url})`.
- Verify every price and date against the live registration page.

## 3. Feature article

- The H2 is the article title alone. Never prefix it with "Feature Article:".
- 3–5 paragraphs, enthusiastic, with relevant links from `key_links`.
- When listing workshops or sessions, link the session name **and** the
  instructor or speaker separately.
- Close with a clear call to action link.

## 4. Secondary article

- The H2 is the article title alone.
- 2–3 paragraphs, shorter than the feature.
- A strong call to action.

## 5. Upcoming Events

- Heading: `## Upcoming Events`, with an events image if `images.skill` is set.
- Pull from every URL in `event_sources`, inside `event_window_days`.
- Bulleted list sorted by date, earliest first. Never a table.
- Spell out day and month names in full: "Wednesday, February 18," not
  "Wed, Feb 18."
- **Critical:** the event title links to the canonical event page for that
  specific event, never the group homepage.
- Format:
  `**Day, Month Date — Group —** **[Event Title](canonical-event-url)** — One-sentence description.`
- When a company or product name appears in a description, link it to its site.

## 6. Sign-off

`sign_off` from the config, in regular text (not italics). No team name or
signatures; the email platform handles that.
