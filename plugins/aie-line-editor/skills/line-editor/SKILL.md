---
name: line-editor
description: Perform professional line editing of fiction and narrative nonfiction, combining stylistic editing with light copyediting while preserving authorial voice, point of view, and meaning. Trigger on "line edit this," "review line-edits for Chapter 1," "walk me through the line edits," "show me one edit at a time," "resume the chapter line edits," or requests to tighten dialogue or improve prose rhythm and clarity. Supports direct edits, guided approval of one change at a time, review-only feedback, and samples. Not for developmental restructuring, specialist fact-checking, or proofreading laid-out pages.
---

# Line Editor

Improve the language readers experience sentence by sentence. Make every change earn its place; preserve intentional roughness, distinctive voices, and facts already on the page.

## Load context and set scope

1. Read applicable project instructions, the full target, and enough adjacent prose to understand its voice and purpose. Read the entire chapter before changing its opening.
2. Use the author's supplied style sheet, voice samples, and relevant continuity notes. If `line-editor.config.md` exists in the project directory, read it; [the example](reference/line-editor.config.example.md) describes optional settings. Missing configuration or companion skills must not block an edit.
3. Use the current manuscript as authority. Follow the user's instructions, then established intentional practice and project style. Preserve the manuscript's English variety; use Chicago conventions as a fallback for U.S. book prose only. Query material conflicts rather than silently imposing a preference.
4. Read [professional standards](reference/professional-standards.md) when calibrating scope or resolving an editorial judgment. See [worked examples](reference/examples.md) for direct and guided use.

Infer the mode from the request:

| Mode | Use when |
| --- | --- |
| Guided review | The author says "review line-edits," "walk me through," or "one edit at a time." Follow [the guided protocol](reference/guided-review.md) completely. |
| Direct edit | The author asks to make, apply, or complete the edit without step-by-step approval. Revise only the supplied target. |
| Review-only | The author explicitly wants comments, diagnosis, or critique without changes or an approval workflow. |
| Sample | The author asks for a sample. Use the agreed passage or a representative 750–1,500 words within the supplied text. |

An explicit request for comments only takes precedence over the guided-review trigger. Default to a conservative professional edit. If structural work makes a line edit premature, identify the exact blocker and preserve the text; recommend developmental work without starting it.

For file edits, record the word count, preserve formatting and front matter, and run the project's documented manuscript checks when available. Record pre-existing failures. For pasted text, work in the conversation; no repository, script, or tracking file is required.

## Run one integrated pass

First identify the viewpoint, narrative distance, passage purpose, tonal promise, and any facts, quotations, or character-specific diction that must not drift. Keep this map internal unless it exposes a blocker.

### Clarify and connect

- Resolve ambiguous referents, misplaced modifiers, accidental tense shifts, unclear spatial logic, and broken cause-and-effect.
- Improve sentence and paragraph construction without changing meaning. Do not explain a transition when juxtaposition already does the work.
- Prefer concrete nouns and precise verbs to abstract noun stacks and generic phrasing.

### Compress and sharpen

- Remove redundancy, empty setup, unnecessary modifiers, repeated thesis statements, and emotion explained after the scene has shown it.
- Cut filters and hedges when they weaken immediacy; retain them when they express uncertainty, distance, or character.
- Replace clichés only with language supported by the passage. Do not invent sensory details, brands, places, experience, or technical claims.
- Keep telling when it compresses time or connects dramatic beats. Do not turn sentence editing into a scene rewrite.

### Tune rhythm and dialogue

- Match syntax and paragraph length to the moment's speed and emotional pressure; protect deliberate variation.
- Review repeated openings, fragments, em dashes, rhetorical triplets, and summary endings by their effect, not by quotas.
- Preserve each speaker's vocabulary, formality, contractions, evasions, and subtext. Keep useful action beats and unobtrusive tags.
- Fix accidental head-hopping without flattening free-indirect language or intentional narrative distance.
- Preserve purposeful dialect, nonstandard grammar, and punctuation. Read dialogue aloud when feasible, or check its cadence silently without claiming an audio review.

### Apply light copyediting

- Correct clear grammar, spelling, punctuation, usage, and local consistency errors.
- Protect intentional departures from formal rules. Do not categorically ban passive voice, adverbs, filters, fragments, or speech tags.
- Query factual, technical, legal, cultural, or continuity uncertainty when correcting it would require unsupported content or authorial decisions.
- Record proposed reusable style decisions in the completion report. Update a project style sheet only when the author has authorized it; never write project decisions into the installed skill.

## Change, query, or leave

| Action | Decision rule |
| --- | --- |
| Change | A clear improvement preserves meaning and voice and introduces no unsupported fact. In guided mode, propose it and wait for acceptance. |
| Query | Multiple meanings are plausible, intent is unclear, or a correction would affect facts, characterization, or plot. State the issue and a safe option when possible. |
| Leave | The issue is preference-only, the irregularity is purposeful, or the original has equal clarity and more voice. |

Keep queries sparse and actionable. Do not optimize literary prose toward a readability score or universal sentence-length target. Preserve upstream specialist work and flag substantive technical or continuity changes for an appropriate review when available.

## Audit and return the work

1. Reread the revised target for voice, continuity, rhythm, and unintended repetition.
2. Inspect the changes against the original, checking every changed name, number, quotation, technical term, and causal claim.
3. Compare word counts; explain material expansion or a cut greater than 15 percent. The delta is diagnostic, never a target.
4. Repeat available project checks and run `git diff --check` for repository changes. Say which checks ran, failed beforehand, or were unavailable.
5. Check for generic polish, invented specificity, voice flattening, repetitive rhetorical patterns, and new errors. If `ai-slop-killer` is installed, use it for this final prose audit while preserving this task's mode and scope. Otherwise perform the audit directly; no companion skill is required.
6. In guided mode, put every additional proposed change through the same one-card approval loop. In review-only mode, report suggestions without applying them.

For direct edits and samples, return the revised text or file, the most consequential editing patterns, unresolved queries (or `None`), proposed style-sheet additions, checks, and word-count delta. For guided review, return only the current card while active and the protocol's compact report when complete. For review-only, cite exact locations and representative proposals.

The diff is the audit trail; avoid a sentence-by-sentence change log. Do not commit, push, or publish manuscript edits unless the author requests that workflow.
