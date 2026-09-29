---
name: voice-profile
description: Build a reusable voice profile for any person from their transcripts, recordings, posts, or writing samples, save it as voice-profile.md, then write new content in that voice. Use when someone says "learn my voice," "build a voice profile," "analyze how I talk," "here are my transcripts," "make this sound like me," "write this in my voice," "draft something I'd say," or asks for a newsletter, post, email, keynote, or book passage that will be published under a specific person's name.
---

# Voice Profile

This skill has two modes. **Build** reads a person's real words and distills them into a `voice-profile.md`. **Write** loads that profile and drafts in the voice. Build once, write many times, refresh the profile when new samples arrive.

The profile is only as good as its evidence. Every claim in it points back to something the person actually said or wrote.

## Mode 1: Build the profile

### Inputs

- **Samples.** Verbatim transcripts are the best source because they catch the unedited rhythm. Published writing is second best. Ghostwritten or heavily edited copy is weak evidence; tag it as such.
- **Volume.** Aim for 5,000+ words across at least three contexts (casual, business, storytelling). Under 2,000 words, build a provisional profile and say so at the top.
- **Speaker isolation.** In transcripts, keep only the subject's lines. Other speakers' words are not evidence.

### Method

Work through the dimensions in `reference/extraction-guide.md` in order. For each one, collect evidence first, then write the finding. The dimensions:

1. **Context that shapes the voice** — career arc, the places and eras they draw on, what they have seen firsthand. Only what the samples or the person supply.
2. **Rhythm and structure** — sentence length, restarts, fragments, how they land a point.
3. **Storytelling moves** — how an argument is carried (anecdote, data, history, named people), where the punchline sits.
4. **Values and worldview** — the positions they hold consistently. These are the "never break" rules.
5. **Verbal tics and signature phrases** — with an observed frequency, so the writer does not overdose.
6. **Humor register** — wry, dry, absurd, self-deprecating, none.
7. **Reference pool** — the pop culture, history, and domains they reach for.
8. **Tone by format** — how the voice shifts across newsletter, social post, email, talk, long-form.
9. **Anti-patterns and banned words** — what they never say, and phrasings they have explicitly rejected.
10. **Calibration lines** — 6 to 10 short verbatim lines that capture the voice at its most typical.

### Privacy pass (required before saving)

Samples often contain things that must not end up in a reusable file:

- Strip email addresses, phone numbers, street addresses, account numbers, and anything that looks like a credential.
- Remove private details about third parties (health, money, family matters). Keep a named person only if the subject names them publicly.
- Prefer paraphrase over quotation for anything personal. Calibration lines should be about ideas and style, not private life.
- Record the source type and date range, not the source file path or account it came from.

### Output

Fill `reference/voice-profile.template.md` and save it as `voice-profile.md`. Default location is the project root; if the user names a path, use theirs. See `reference/example-profile.md` for a filled-in profile of a fictional person.

End the build by telling the user: word count analyzed, confidence per dimension (high / medium / low), and the two or three things more samples would sharpen.

## Mode 2: Write in the voice

1. **Load the profile.** Look for `voice-profile.md` in the project root, then any path the user gave. If none exists, offer to build one; if the user declines, write in a neutral voice and say so.
2. **Identify format and purpose.** Pull the matching row from "Tone by format."
3. **Find the specific.** A piece in someone's voice needs at least one concrete anchor: a number, a named event, a real memory. If the brief has none, ask for one. Never invent a personal anecdote and attribute it to a real person.
4. **Draft with the documented rhythm.** Match sentence length, restarts, and landing beats. Do not over-polish; a voice that sounds like a press release has been lost.
5. **Values check.** Nothing in the draft may contradict the "never break" list.
6. **Tic check.** Use signature phrases at roughly their observed frequency. Two too many reads as parody.
7. **Read-aloud test.** Would this person say it mid-conversation? If not, rewrite the sentence that failed.
8. **Final prose pass.** Run the `ai-slop-killer` skill on the draft, then re-check that it did not sand off the voice's deliberate quirks. The profile's banned words win over any generic rule.

### Format notes

- Short formats (social, email) lean on one tic and one specific. Long formats (newsletter, talk, chapter) carry a story per major point.
- For fiction or book passages, the profile governs narration and the author's asides, not every character's dialogue.

## Maintaining the profile

- Append new calibration lines as samples arrive; retire ones that no longer sound current.
- If the person corrects a draft ("I'd never say that"), add it to Anti-patterns with the date.
- Keep the file under ~400 lines. Condense before appending.

## What this skill does not do

- It does not impersonate someone without their consent. Build profiles only for the user, or for someone who has agreed to it (a client, an executive the user ghostwrites for).
- It does not fabricate quotes, credentials, or experiences.
- It does not line-edit for grammar; pair it with a house style skill for that.

## Reference files

- `reference/extraction-guide.md` — how to mine each dimension, with evidence rules.
- `reference/voice-profile.template.md` — the file this skill writes.
- `reference/example-profile.md` — a short filled-in profile for a fictional person.
