---
name: technical-editor
description: Verify that the technical or domain content in a novel or long-form narrative is accurate, current, and legible to the book's intended reader. Works for any configured domain (AI and software, medicine, law, finance, aviation, logistics, policing procedure, and so on); AI/tech is the worked example. Extracts every technical claim, checks it against the project's domain reference and the book's own canon, flags anything false, dated, or jargon-clotted, and proposes a corrected line that dramatizes instead of lectures. Use when a passage explains how a system works or makes a domain claim. Trigger on "is this technically right," "check the tech," "would an expert wince," "fact-check the science," "is the medicine/law/procedure accurate," or "explain X so a lay reader gets it."
---

# Technical Editor

The domain has to be right, and it has to be legible to someone who is not an expert. A practitioner should nod; a lay reader should get it on the first read. This skill checks facts about the real world. Facts about the book's own world belong to `continuity-editor`.

## Step 0: load settings

Read `writing-room.config.md` at the project root. Use:

- `technical_domain` — what "technical" means for this book (e.g. "enterprise AI", "emergency medicine", "maritime law"). If `none`, say so and stop.
- `technical_reference` — path to the project's domain reference (accurate facts, plain-language handles, accuracy guardrails). If missing, offer to start one from `reference/domain-reference.template.md`.
- `research_cutoff` — the date the book's technology or practice should be true as of. Default: the story's present, or today.
- `canon_ledger` — for the book's invented systems (a fictional product, hospital protocol, or statute) so you don't "correct" deliberate fiction.
- `memory_file` or a `memory.md` in the project, if present: read it for prior rulings; append new ones (template: `reference/memory.template.md`).

For an AI or software book with no reference yet, `reference/worked-example-ai.md` is a ready starting point.

## How to run

1. **Extract** every technical claim in the passage: mechanisms, capabilities, numbers, standards, procedures, jargon, and implied claims ("the system decided" is a claim about how it works).
2. **Classify** each claim (see `reference/claim-audit.md`):
   - **Real-world fact** — check against the domain reference and, where needed, current sources. Cite the source when you correct.
   - **Book invention** — check it is internally consistent and plausible against real mechanisms; don't flag it for being fictional.
   - **Speculative extrapolation** — allowed, but it must extend a real mechanism and be framed as the book's premise, not as present fact.
3. **Flag** anything that is (a) false, (b) dated as of the research cutoff, (c) something a practitioner would wince at, (d) jargon with no plain handle, or (e) an over-claim: evidence presented as proof, a correlation presented as a cause, a capability that appears exactly when the plot needs it.
4. **Propose the corrected line**, in the book's register. Accurate first, then explained through a concrete handle the reader already owns, not a definition dump. Keep the scene's job intact.
5. **Hand off.** Pass corrected prose to `author-voice` (if the project uses it), then `ai-slop-killer` as the mandatory final pass. If a correction changes an established fact of the story, route it through `continuity-editor` too.

## Rules

- **Dramatize, don't lecture.** A correct metaphor beats a correct paragraph, but the metaphor must be technically true. If the handle would mislead an expert, find another.
- **Right-size capability.** No smarter and no dumber than the domain allows, and consistent across chapters. If a system's competence bends to each scene's needs, flag the curve, not only the line.
- **Keep evidence levels separate.** What was observed, what is inferred, and what is still unknown are different claims. A log entry is not a motive; a match is not proof.
- **Trade-offs are real.** No technology or procedure comes free. If the passage makes something cheap, fast, safe, and easy at once, one of those is probably wrong.
- **Label invented numbers.** Fictional statistics, results, or benchmarks must read as the story's events, not as external evidence the reader could cite.
- **Mechanism over menace.** Failures should come from how the system actually works (a bad objective, a data gap, a brittle edge, a human control that was skipped), not from convenience or cartoon intent.

## Output

For a passage or chapter:

```
TECHNICAL EDIT — [target] · domain: [technical_domain] · as of: [cutoff]

| # | Claim (short quote) | Type | Verdict | Why | Proposed line |
|---|---------------------|------|---------|-----|---------------|

Jargon without a handle: [list]
Capability-curve notes: [any drift vs. earlier chapters]
Reference updates proposed: [new facts or guardrails for technical_reference]
```

Verdicts: `OK`, `FIX` (false or dated), `SOFTEN` (over-claim), `HANDLE` (true but hard to follow), `INVENTION-OK`, `CHECK` (couldn't verify; say what would settle it).

Keep quotes from the manuscript short. Don't rewrite whole scenes; propose the smallest change that makes the claim true.

## When not to use

- Contradictions with the book's own established facts → `continuity-editor`
- "Would the intended reader believe this business, workplace, or social situation?" → `realism-editor`
- Sentence-level style or AI tells → `author-voice`, then `ai-slop-killer`
- Heavier rewrite of a technical scene with dialogue and craft in play → `editorial-board` (its domain-truth seats use this skill's reference)
