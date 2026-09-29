---
name: author-voice
description: Write and revise a novel's prose so it matches the author's own codified voice, as defined in the project's voice-profile file (principles, rhythm, setting texture, character speech, hard rules, and touchstone lines). Builds the voice profile from sample chapters if none exists. Use for drafting or line revision where the output is the book's narration or dialogue, or to check that a passage sits on the page without a seam. Trigger on "make it sound like the book," "in my voice," "in the book's voice," "match the voice," "voice pass," "build a voice profile," or any prose attributed to the manuscript.
---

# Author Voice

Enforce **the author's** voice, not a generic "good prose" voice and not the model's. The voice is whatever the author's voice profile says it is; this skill applies it and keeps it honest.

Note: a book's narrative voice often differs from the author's other writing (newsletters, posts, essays). The profile describes the **book's** voice unless the author says otherwise.

## Inputs

- `writing-room.config.md` at the project root: `voice_profile` (path to the profile), `pov`, `tense`, `banned_words`, `house_rules`.
- The **voice profile** at `voice_profile`. Structure: `reference/voice-profile.template.md`.
- A nearby passage of the real manuscript, for rhythm.
- Optional: a project `memory.md` (config `memory_file`, or `reference/memory.template.md`).

## If there is no voice profile

Build one before revising anything:

1. Ask for two or three chapters (or 5,000+ words) the author considers most "them."
2. Extract, with quoted evidence for each: sentence-length pattern, diction level, how concrete vs. abstract, how setting shows up, how scenes end, how characters differ in speech, punctuation habits, what the prose never does.
3. Pull 5 to 8 touchstone lines verbatim.
4. Write the profile from the template, show it to the author, and save it at the config's `voice_profile` path only after they confirm. Never invent touchstone lines.

## How to use

1. Read the voice profile and a nearby passage of the manuscript.
2. Draft or revise so the passage could sit beside the profile's touchstone chapters without a seam.
3. Check against the profile's **hard rules** and the config's `banned_words` and `house_rules`.
4. Report what changed and why, in a few lines keyed to profile principles.
5. Hand off to `ai-slop-killer`. Always.

## What to check (the default lenses; the profile overrides)

- **Concrete over abstract.** Name the thing, the street, the brand, the body.
- **Setting is texture, not garnish.** Real anchors from the profile, used sparingly and accurately.
- **Argument through scene and cost**, not speeches, if the book carries an idea.
- **Restraint.** End scenes a beat early. Don't explain the image.
- **Dignity.** Characters from every walk of life are smart and whole; no condescension.
- **Dialogue does double duty,** and each character sounds like their entry in the profile.
- **Rhythm.** Match the profile's sentence-length pattern, fragment use, and punctuation habits.

## Guardrails

- The profile is the authority. If your instinct and the profile disagree, the profile wins; if the profile seems wrong, raise it with the author instead of drifting.
- Don't import the model's defaults (tidy triads, balanced antithesis, summary endings). `ai-slop-killer` catches most, but don't add them in the first place.
- Voice changes only; no plot, fact, or cast edits. Flag those for their owners.
- Inside the Writing Room this pass sits after `continuity-editor` and before `ai-slop-killer`.
