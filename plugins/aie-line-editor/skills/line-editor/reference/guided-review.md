# Guided line-edit review protocol

Use this protocol when the author wants to review a chapter one proposed change at a time.

## Interaction contract

- Show exactly one pending edit per response.
- Wait for the author's decision before changing the manuscript.
- Apply only accepted wording.
- Walk through the chapter in manuscript order so the author can hold the local scene in mind.
- Skip paragraphs that do not need a meaningful edit; do not manufacture choices to make the queue look substantial.
- Treat each card as one editorial decision. A card may contain several sentences only when they form one inseparable revision.

## Start automatically

For a request such as `Review line-edits for Chapter 1`:

1. Resolve the chapter from the current project or supplied text. Ask only if the target is ambiguous.
2. Read applicable project instructions, the chapter, and any supplied style sheet, voice samples, or continuity notes. Missing optional context does not block the review.
3. Run any available documented manuscript checks and record the original word count. For pasted text, record the count and note that file checks do not apply.
4. Scan the full chapter and form a conservative candidate queue.
5. State the chapter, word count, baseline status, and approximate candidate count in one compact sentence.
6. Present the first edit card in the same response.

Do not open with a menu or ask how aggressive the edit should be. Use the skill's conservative default unless the author specifies otherwise.

## Build the candidate queue

Include only changes with a defensible benefit:

- clear errors or ambiguities;
- unnecessary repetition or explanation;
- weak or abstract wording with a supported, more precise alternative;
- rhythm or paragraphing that impairs the intended effect;
- dialogue that loses character, subtext, or physical grounding;
- POV, tense, or narrative-distance slips;
- local consistency issues appropriate to line editing.

Exclude preference-only substitutions, broad rewrites, speculative details, and changes already handled by another specialist. Route true author questions to the end of the local passage or present them as a `Query` card when a decision is needed before proceeding.

Keep the queue in manuscript order. Recalculate later candidates when an accepted edit makes one obsolete. Describe the count as approximate until the final card.

## Use this edit card

```markdown
### Line edit 1 of about 14 — Clarity

**Location:** Paragraph beginning “The kitchen was empty…”

**Before**
> [Only the sentence or compact passage needed to judge the edit.]

**Proposed**
> [The complete replacement text.]

**Why:** [One or two plain-language sentences explaining the concrete benefit.]

**Effect:** [Meaning/voice/fact impact and, when useful, word-count change.]

Reply naturally: **Accept**, **Revise: …**, **Skip**, **Context**, **Why**, **Undo**, or **Pause**.
```

Use `Query` instead of an edit category when authorial intent is required. Do not recommend `Accept` on a genuine query.

## Interpret responses

### Accept

Treat `accept`, `yes`, `use it`, and equivalent clear approval as acceptance. If `next` or other wording could mean either skip or accept, resolve that ambiguity before modifying the text.

1. Check that the original passage still matches the pending card, then apply only the displayed replacement to the working manuscript. If it changed, reconcile the difference and present a fresh card before applying anything.
2. Verify the local patch and update the session ledger.
3. Confirm in a short clause such as `Accepted and applied.`
4. Present the next edit card in the same response.

Do not reprint the accepted card.

### Revise or comment

Treat specific feedback, alternative wording, or a concern as a request to revise the current proposal.

1. Respond to the substance of the comment.
2. Show a revised version of the same card.
3. Keep the manuscript unchanged.
4. Wait again; do not advance.

### Skip

Leave the source unchanged, mark the card skipped, and present the next card in the same response.

### Context

Show the minimum surrounding paragraph or dialogue exchange needed to judge the proposal, then repeat the same proposed replacement. Do not advance or modify the source.

### Why

Explain the editorial reasoning, including the tradeoff and why leaving the original is or is not reasonable. Keep the same card pending.

### Undo

Undo only the most recently accepted line edit when the reversal is safe and isolated. Confirm the reversal and return to that card. If later accepted edits depend on it, explain the dependency before changing anything.

### Pause or stop

Keep accepted edits in place. Return a short checkpoint:

```text
Paused Chapter 1 after edit 6: 4 accepted, 2 skipped, next is edit 7.
Resume with: “Resume the Chapter 1 line edits.”
```

Do not run completion validation on a paused session unless the author asks.

## Maintain session state

Track in the conversation:

- target file and original word count;
- current edit number and approximate remaining count;
- accepted edits with original and replacement text;
- skipped edits;
- unresolved queries;
- whether the last accepted edit can be undone safely.

Keep this ledger in the conversation; create a tracking file only if the author asks. On resume, inspect the current file before continuing. Verify that accepted edits are still present and that the target has not changed unexpectedly. If it changed, reconcile the diff before showing the next card.

If the prior ledger is unavailable, do not reconstruct acceptances from memory or assume approval; ask for the checkpoint or offer a fresh review of the current text. For pasted text with no file, maintain an accumulating working draft in the conversation and return the complete approved passage at the end.

## Complete the chapter

After the last candidate:

1. Reread the complete revised chapter.
2. Run the mechanical checks and `git diff --check` when applicable.
3. Run the final prose audit described in SKILL.md, using `ai-slop-killer` in audit-only mode if installed or checking directly otherwise. Add any new proposed wording to the guided queue one card at a time; never silently apply downstream changes.
4. Recheck continuity or technical meaning if accepted edits touched them.
5. Report accepted, reusable style decisions. Write them to a project style sheet only if that update is authorized; never modify the installed skill.
6. Return:
   - accepted, skipped, and queried counts;
   - original and final word counts;
   - the most consequential improvements;
   - unresolved author queries;
   - style-sheet additions;
   - validation results.

Do not commit, push, or merge unless the author explicitly requests that publication workflow.
