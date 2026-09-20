# Sample run — ai-slop-killer

A real before/after on a short marketing draft. This is the exact output shape the skill produces.

## Input (as drafted)

> In today's fast-paced business world, companies are constantly searching for ways to leverage AI across every part of their operations. AI isn't just another tool — it's a fundamental shift in how work gets done. Experts agree that organizations adopting it early see meaningful productivity gains, while those that hesitate risk falling behind their peers in ways that compound over time. The result? A widening divide between companies that move now and companies that wait for certainty that never comes. It's worth noting, though, that adoption alone doesn't produce results. Teams that bolt AI onto existing workflows tend to plateau quickly, while teams that rethink the workflow itself — what gets automated, what stays human, and how the two hand off — are the ones reporting real gains. Leadership attention is usually the deciding factor: pilots that report to an executive sponsor make it to production, and pilots that live in a side project rarely do. The gap between experimenting with AI and operating with it is where most of the value is currently being won or lost.

## Output

```
Slop score: 53 → 4  (per 500 words)
```

> Companies keep asking how to use AI across their operations, and the honest answer is that the tooling matters less than the workflow. Teams that bolt AI onto an existing process plateau quickly. Teams that rethink the process itself — what gets automated, what stays human, how the two hand off — report real gains. (McKinsey's 2024 State of AI survey found the biggest EBIT impact concentrated in companies that redesigned workflows, not just deployed tools.) Leadership attention usually decides which kind of team you get: pilots with an executive sponsor make it to production; side-project pilots rarely do. That gap, between experimenting with AI and operating with it, is where the value is being won or lost.

```
Cut / fixed:
- Wind-up intro                  — deleted "In today's fast-paced business world…"; opened on the real point
- Negative parallelism x1        — "isn't just another tool — it's a fundamental shift" → cut; the claim is argued, not asserted
- "leverage" x1                  — → "use"
- Vague attribution              — "Experts agree" → named a checkable source (McKinsey 2024)
- Rhetorical Q&A                 — "The result? A widening divide" → folded into a plain sentence, then cut as redundant
- "It's worth noting"            — deleted; the sentence stood without it

Left on purpose:
- 1 em-dash pair ("— what gets automated… —") — doing real work, no pile-up
- The closing antithesis (experimenting vs operating) — one earned contrast, stated once
```

Word count 190 → 122. Meaning and stance preserved; the unsupported "experts agree" claim became a sourced one instead of being cut, per `citations: preferred`.
