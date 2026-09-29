# Writing bundle

## ai-slop-killer

The final anti-AI-slop editing pass for any prose — blog posts, newsletters, social, email, marketing/web copy, docs, essays, fiction. It's the last thing to touch a draft before it ships.

### What it does

Runs a four-step loop: **Detect → Score → Fix → Prove.**

1. **Detect** — scans for documented AI tells: negative parallelism ("it's not X, it's Y"), rhetorical Q&A, rule-of-three and anaphora pile-ups, em-dash and unicode overuse, corporate-AI vocabulary, wind-up intros and signposted conclusions, bold-first-bullet listicles, low-burstiness rhythm, hedging, vague attributions, grandiose stakes, and more.
2. **Score** — a 0–100 slop score (lower is cleaner), so the improvement is visible.
3. **Fix** — rewrites the tells in place while preserving meaning and voice.
4. **Prove** — returns the cleaned text plus an itemized list of what changed and what was left in on purpose.

The catalog is built from documented sources — Wikipedia's *Signs of AI writing*, the tropes.fyi directory, and working editors' guides — not one person's taste.

### Use it

- "Does this sound like AI? Clean it up."
- "De-slop this newsletter draft."
- "Copyedit this and show me what you cut."

### Inputs / outputs

- **In:** any passage of prose (paste it, or point to a file).
- **Out:** the cleaned passage, a before→after score, and the change log.

### Configure

Drop a `slop.config.md` in your working directory to add house rules. Copy the annotated example from `plugins/ai-slop-killer/skills/ai-slop-killer/reference/slop.config.example.md`. You can set:

- `banned_words` — extra words to hard-ban.
- `allowed_words` — documented-tell words you legitimately use (kills false positives; every domain has a "robust").
- `voice` — a voice/style skill or a short note to preserve.
- `citations` — `required` | `preferred` | `off`.
- `channel_defaults` — per-channel emoji/format rules.

### Reference files

- `reference/slop-catalog.md` — the full field guide of tells, with fixes and sources.
- `reference/scoring.md` — how the slop score is computed.
- `reference/slop.config.example.md` — annotated config template.

### Notes

It won't over-correct: one em-dash, one triad, one rhetorical question, one metaphor per piece is human. The goal is prose that reads like a person wrote it on purpose — lived-in, not scrubbed flavorless. It has an optional **fiction mode** for manuscript prose.

## line-editor

Professional line editing for fiction and narrative nonfiction: clarity, coherence, rhythm, dialogue, and light copyediting while preserving voice, viewpoint, and meaning. Install its standalone bundle:

```text
/plugin install aie-line-editor@aienterprise-skills
```

### Use it

- "Line edit this chapter in place, preserving the narrator's voice."
- "Review line-edits for Chapter 1."
- "Walk me through the line edits one at a time."
- "Resume the Chapter 1 line edits."
- "Give me comments only; don't change the manuscript."
- "Line edit this 1,000-word sample."

Direct mode returns an edited passage or file and a compact report. Guided mode shows one card with before/proposed text, a reason, and its effect, then waits for **Accept**, **Revise**, **Skip**, **Context**, **Why**, **Undo**, or **Pause**. It applies only accepted wording; a later prose audit must also go through approval. For pasted text, the approved draft stays in the conversation.

### Configure and verify

Supply your own style sheet and voice samples, or copy the optional [line-editor.config.md example](../plugins/aie-line-editor/skills/line-editor/reference/line-editor.config.example.md) into your project. Defaults preserve the manuscript's language variety and established voice. Project facts and decisions stay in the project; the installed skill is not a manuscript ledger.

The final report includes unresolved queries, proposed style decisions, word-count change, and the checks actually run. Existing manuscript checks are used when available; pasted text does not require a repository or scripts. The skill includes a final check for generic polish and voice flattening. It can use `ai-slop-killer` in audit mode when installed, and works independently when it is not.

See [worked direct and guided examples](../plugins/aie-line-editor/skills/line-editor/reference/examples.md) and the [professional source basis](../plugins/aie-line-editor/skills/line-editor/reference/professional-standards.md). Developmental restructuring, specialist fact-checking, and proofreading laid-out pages remain separate tasks.
