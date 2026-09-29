# News digest — structure

Counts and labels below are the defaults from `editions.news_digest`. If the
config changes a count (for example `quick_hits: 3`), change the skeleton to
match. `{K}` is `voice.kicker_prefix`.

## Skeleton

```markdown
[Opening paragraph — 2–4 sentences naming the week's through-line]

**Key Takeaways:**

- [Takeaway 1 — works as a standalone social post]
- [Takeaway 2]
- [Takeaway 3]
- [Takeaway 4]
- [Takeaway 5]

[Optional: editions.news_digest.tagline]

---

#### **{K}THE BIG STORY**

### [One-line headline that works as a standalone quote](canonical-url)

[Paragraph 1 — what happened: the news, the numbers, the context]

[Paragraph 2 — the deeper story: revenue, adoption, competitive dynamics]

[Paragraph 3 — the implications: what happens next]

[Paragraph 4 — the business read: what it means for the reader]

---

**4 QUICK HITS**

### 1. [Headline](canonical-url)

[One paragraph — the news, then one closing sentence on what it means for the reader]

### 2. [Headline](canonical-url)

[One paragraph]

### 3. [Headline](canonical-url)

[One paragraph]

### 4. [Headline](canonical-url)

[One paragraph]

---

**3 TOOLS**

- [**Tool Name**](canonical-url) — [2–3 sentences: what it does, the business value]
- [**Tool Name**](canonical-url) — [2–3 sentences]
- [**Tool Name**](canonical-url) — [2–3 sentences]

---

**{K}EXTRA READ**

### [Article or podcast title](canonical-url)

[2–3 sentences on why it is worth the reader's time, tied to the week's theme]
```

## Section guide

- **Opening paragraph** — name the thread that ties the week's stories together.
  It becomes the subtitle in the metadata.
- **Key Takeaways** — one bullet per story. Each passes the screenshot test: it
  makes sense pulled out and posted on its own. Specific numbers; em dashes for
  punch if `voice.prefer_em_dashes`.
- **The Big Story** — the week's most important story. Linked, quotable H3
  headline. Three to four paragraphs, ending on the implication for the reader.
  It passes the "tell a friend" test: the reader can walk into a meeting and
  say something smart.
- **Quick Hits** — numbered. One paragraph each. Distinct vectors, not four
  angles on one theme. A good spread: capability, infrastructure,
  business/funding, and policy or culture. End each on the business framing.
- **Tools** — real discoveries, no repeats from the Quick Hits. Spread across
  categories: a major update to a popular app, an enterprise-grade tool, and an
  emerging tool at an accessible price.
- **Extra Read** — one long-form piece or podcast that adds depth the edition
  did not cover. Connect it to the week's theme.
