# House Style Config (example)

Copy this file to `house-style.md` in your project root and edit it. Every section is optional; delete what you do not use. The `house-style` skill reads headings and tables, so keep the structure. Anything in a section it does not recognize is applied as a plain instruction.

---

## Publication

- **Name:** Example Weekly
- **Audience:** business professionals and managers who use AI tools but do not build them
- **Content types:** newsletter, blog post, report, site copy

## Reader value test

Every piece must answer this question in one sentence:

> How does this help the reader do their job better this week?

`blocking: true`

## Tone

Clear, confident, and practical. Write like a knowledgeable colleague briefing a busy executive. Specific over abstract. No hype, no speculation presented as fact.

| Sounds like | Never sounds like |
|---|---|
| "Three of the five tools we tested failed on scanned PDFs." | "AI is transforming document workflows forever." |
| "Start with the invoices. They are the most repetitive." | "Organizations must embrace this new era." |
| "We don't know yet, and here is what would tell us." | "Experts agree this will change everything." |

## Banned words and phrases

Case-insensitive; inflections included. `blocking: true`

| Banned | Try instead |
|---|---|
| delve | look at, dig into, examine |
| realm | area, field |
| unleash | release, start, use |
| tapestry | mix, set |
| paradigm | model, approach |
| landscape | market, field, options |
| cornerstone | foundation, core |
| game-changer | name the specific change |
| revolutionary | name the specific change |
| unlock potential | say what becomes possible |
| excited to announce | just announce it |
| in today's fast-paced world | cut |

## Spelling and hyphenation

`blocking: true`

| Rule | Correct | Incorrect |
|---|---|---|
| "open source" is two words, never hyphenated, including as a modifier | open source software | the hyphenated form |
| "email" has no hyphen | email | e-mail |
| AI is not spelled out after first use | AI | A.I., artificial intelligence (repeated) |
| Use the serial comma | red, white, and blue | red, white and blue |

## Required terms

| Term | Rule |
|---|---|
| Example Weekly | Always italicized in body copy |
| Product names | Match the vendor's capitalization |

## Citations

- **Format:** inline numeric markers with Markdown reference-style links at the end of the piece.
- **Required for:** every statistic, direct quote, and non-obvious factual claim.
- **Freshness:** AI-related sources older than 18 months need a note or a newer source.
- **Stats need:** the year and the source organization in the sentence or the link text.

Example:

```markdown
One industry survey found that a majority of companies now use AI in at least one business function [1].

[1]: https://example.com/survey-2026
```

`blocking: true`

## Formatting

- Prose first. Bullets for lists of parallel items only, not for arguments.
- Alternate paragraphs with tables where comparison helps.
- **Bold** for key terms on first use; no more than one bold phrase per paragraph.
- H2 for sections, H3 for subsections; never skip a level.
- Paragraphs of five sentences or fewer.

## Taxonomy and cross-linking (optional)

Tag each piece with one section and link to at least two others.

| Section | What goes here |
|---|---|
| News | What happened and why it matters |
| How-to | One skill the reader can apply today |
| Analysis | One hard question, argued |
| Tools | Evaluations and comparisons |

`min_cross_links: 2`

## Visual brand (optional; styled output only)

| Token | Value |
|---|---|
| Primary accent | `#1F6FEB` |
| Secondary accent | `#F97316` |
| Background (dark) | `#0B1220` |
| Headline font | Inter, 700 |
| Body font | Inter, 400 |
| Code / labels | JetBrains Mono |

## Review checklist

1. Reader value question answered in one sentence.
2. No banned words or phrases.
3. Spelling and hyphenation rules followed.
4. Every stat and quote cited in the required format.
5. Tone matches the "sounds like" column.
6. Formatting rules followed.
7. Tagged and cross-linked (if taxonomy is used).
