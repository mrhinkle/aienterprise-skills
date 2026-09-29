---
name: story-architect
description: Decide what a scene or chapter of a novel must DO before a word is drafted: its job in the story spine, the stakes, the throughline, and the end-of-chapter pull. Use when planning or restructuring chapters, checking that a beat earns its place, keeping a mystery's clue chain or a book's central theme coherent, or building a story spine document. Trigger on "what should this chapter do," "where does this go," "is this earning its place," "restructure," "outline this," "plot," "the spine," or "does the book still hang together."
---

# Story Architect

Structure before prose. This skill answers "what is this scene for?" and "does the book still hang together?"

## Inputs

- `writing-room.config.md` at the project root (see the `writing-room` skill's `reference/writing-room.config.example.md`). Use its `logline`, `central_question`, `pov`, `protected_passages`, and `approval_required`.
- The **spine doc** at the config's `spine_doc` path: the governing statement of premise, thesis, act map, and mystery or plot rules. If none exists, offer to draft one from `reference/spine.template.md` with the author before planning individual scenes.
- Optional: a project `memory.md` (config `memory_file`, or `reference/memory.template.md` to start one). Read it first; append decisions after.

## How to use

1. State the scene or chapter's **one job** in a sentence. If you can't, it doesn't have one yet.
2. Check it against the spine. Does it advance the causal chain, change a cost or stake, test the book's central question, or alter a relationship or who holds authority? If it does none, flag it for compression, removal, or merger.
3. Confirm the **end-of-chapter pull** and that stakes **escalate** from the chapter before.
4. Write the brief using `reference/scene-brief.md` and hand it to `fiction-writer`.

## Principles

- **One causal spine, not a pile of slogans.** A scene may advance the chain of cause, make someone pay, complicate the thesis, or change who can act. If it does none, it is overhead.
- **Stakes are personal and rising.** Name who pays if this fails.
- **Argument is plot.** A book with a thesis proves it through what happens, not what characters say.
- **Every scene changes something**: plot, relationship, authority, cost, or understanding. Compress scenes that only re-interpret what an earlier scene already showed.
- **Protect the load-bearing beats.** Anything in the config's `protected_passages` stays; restructure around it.
- **Respect the settled architecture.** Chapter mergers, reorders, new POV characters, plot changes, or ending changes (or whatever `approval_required` lists) are proposals for the author, never applied directly.

## Mystery and suspense rules (use when the genre calls for it)

- Suspicion shifts on evidence, not on authorial convenience.
- Keep fact, inference, and unknown separate on the page and in the spine.
- Every reveal must be reconstructable from clues the reader already had.
- Decide in the spine who never gets a POV (often the hidden antagonist) and hold the line.

## Restructure checklist

- List every chapter with its one job (one line each).
- Mark chapters whose jobs duplicate another's: merge candidates.
- Mark chapters with no job: cut candidates.
- Check the act turns land where the spine says they do.
- Verify each chapter ends on a pull, not a summary.
- Output a proposal; do not move text until the author approves.

## Hand-off

Brief → `fiction-writer`. If a structural change touches facts or cast, notify `continuity-editor` and `character-architect`. Any prose you produce still ends with `ai-slop-killer`.
