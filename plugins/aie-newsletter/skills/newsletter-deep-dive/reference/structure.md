# Deep dive — structure

`{K}` is `voice.kicker_prefix` (default `// `). `{Edition}` is
`editions.deep_dive.name`. Counts are the defaults from `editions.deep_dive`.

## Skeleton

```markdown
**{K}{Edition}**

# [Title]

*[Subtitle — one line that frames the analysis]*

## Executive Summary

[Thesis paragraph — the core tension or question, stated plainly]

**{K}[Finding 1 — a bolded sentence carrying the key data, cited to its source]**

**{K}[Finding 2]**

**{K}[Finding 3, and optionally a 4th]**

[Closing line — the strategic posture: what the leaders who get this right will
have done]

---

## {K}The Deep Dive

[Narrative hook — first person, 3–6 paragraphs. The author's way into the
topic, often a historical parallel they lived through. This is what pulls the
reader in.]

### [Organic question subhead — e.g., "What is the [X] problem, really?"]

[Analysis with evidence; every statistic cited]

### [Further organic subheads as the argument needs]

[If the topic is contested: a bull case and a bear case, each built in stages
and weighed against the evidence.]

### Common Missteps

**Misstep 1: [name].** [One paragraph.]

**Misstep 2: [name].** [One paragraph.]

**Misstep 3: [name].** [One paragraph.]

**Misstep 4: [name].** [One paragraph.]

## {K}Key Takeaways

**1. [Imperative action].** [Two sentences of rationale.]

**2. [Imperative action].** [Two sentences.]

**3. [Imperative action].** [Two sentences.]

**4. [Imperative action].** [Two sentences.]

[Closing — a concrete playbook: the specific line items or moves a leader takes
into the next planning or budget cycle. End on a sharp final thought.]
```

## Section guide

- **Executive Summary** — stands alone as a briefing. Thesis, then 3–4
  kicker-prefixed findings each carrying sourced data, then the posture line.
  Length: `editions.deep_dive.exec_summary_words` (default 220–320).
- **The narrative hook** — specific and first person. The author's own history
  earns its keep here. It should make a busy executive keep reading. Ask the
  user for the story if you don't have it.
- **The analysis** — organic question subheads, not a rigid template. Build one
  argument. Acknowledge the counterargument. No logical gaps.
- **Common Missteps** — exactly `missteps` (default 4), each named and numbered.
- **Key Takeaways** — exactly `key_takeaways` (default 4), imperative, each a
  decision the reader can act on.
- **The close** — a playbook, not a summary. Concrete enough to take into a
  budget meeting.
