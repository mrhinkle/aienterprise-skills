---
name: aie-video-webinar-publish
description: >
  BETA. Turn a recorded webinar into a publish-ready YouTube video — pull the
  recording off the webinar platform, strip the umms and ahs, cut the "can you hear
  me" cold open, build a thumbnail that still reads at 168px, write the title,
  description and chapters, and upload it private for review. Every stage verifies
  itself by re-measuring the output. Use this skill whenever someone says "edit the
  webinar recording," "publish last week's webinar," "take out the umms and ahs,"
  "remove filler words from this video," "cut the dead air at the start," "put this
  on YouTube," "make a thumbnail for the video," or hands over a recording of a
  slides-plus-webcam session and asks to ship it. Works for any recording of that
  shape regardless of platform. Configure per channel in `webinar.config.md`.
---

# Webinar → YouTube (BETA)

> **Beta.** The editing and verification stages are proven on real hour-long
> recordings. The upload stage assumes a Composio-connected YouTube account; if
> yours is wired differently, stop after step 7 and upload by hand — everything
> before that is platform-independent.

One job: take an hour of raw webinar and produce something worth someone's click,
without silently mangling the speech in the process.

The reason this is not a two-line ffmpeg script is that **every stage here has a
failure mode that produces a plausible-looking wrong result.** A cut list can look
perfect and land on the wrong words. A render can be exactly the right duration and
contain exactly the wrong audio. The only defence that worked was re-measuring the
output instead of trusting the plan, so that is built into each step.

Copy `reference/webinar.config.example.md` to `webinar.config.md` and fill in your
channel, brand and platform details before the first run.

Work in a per-webinar folder.

## Process

### 1. Get the recording

Webinar platforms rarely expose recordings through their API even when they have
one — `reference/platform-retrieval.md` covers where the file actually lives on the
common hosts, and the traps (expired replay links, download buttons that are not
in the API, config wizards that look like the right menu but aren't).

Whatever the source: get an MP4 on disk, and check its duration against the session
length the platform reports before going further.

### 2. Extract audio — the step that silently breaks everything

```bash
ffmpeg -y -i raw.mp4 -vn -af "aresample=async=1:first_pts=0" \
  -ac 1 -ar 16000 -c:a pcm_s16le audio_sync.wav
```

**`-af aresample=async=1` is not optional.** Recordings from live platforms carry
timestamp gaps where the stream hiccuped. Without the resampler ffmpeg *collapses*
those gaps: on one 58-minute recording the WAV came out 4 seconds shorter than the
MP4's audio track. Every transcript timestamp then drifted against the video, and
every cut landed on the wrong word.

This is the most expensive bug in the pipeline because it hides: comparing the
source transcript to the edited transcript still lines up perfectly, since both
sides share the drift. `build_edit.py` refuses to run unless these match:

```bash
ffprobe -v error -select_streams a -show_entries stream=duration -of csv=p=0 raw.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 audio_sync.wav
```

### 3. Transcribe with a verbatim ASR

Use an ASR that keeps disfluencies. **Whisper does not** — it is trained to tidy
speech, and on the same hour of audio it found 5 filler words where a verbatim
model found 294. An `initial_prompt` asking for verbatim output does not fix it.

ElevenLabs Scribe works and is what the scripts expect:

```bash
curl -s -X POST "https://api.elevenlabs.io/v1/speech-to-text" \
  -H "xi-api-key: $ELEVENLABS_API_KEY" \
  -F "model_id=scribe_v1" -F "timestamps_granularity=word" -F "diarize=true" \
  -F "file=@audio_sync.mp3" -o transcript.json
```

Send a 64 kbps mp3 made from the synced wav — same timebase, far less upload.

Scribe attaches punctuation to tokens (`"uh,"`, `"Um..."`), so strip non-word
characters before matching or your filler count comes back zero. That mistake reads
as "this speaker is remarkably clean," which is why it survives review.

### 4. Build the cut list

```bash
pip install numpy soundfile        # once; ffmpeg must be on PATH too
python3 scripts/build_edit.py --src raw.mp4 --audio audio_sync.wav \
  --transcript transcript.json [--cold-open cold_open.json]
```

**Do not cut on the transcript's word boundaries.** Word *onsets* are accurate;
word *ends* are not. Scribe reported an audibly ~280 ms "uh" as lasting 10 ms, so a
window built from `[start, end] + padding` clipped only the filler's tail and left
it plainly audible in the render.

So the transcript locates each filler and **the audio decides where it starts and
stops**: a filler is one burst of speech energy bounded by silence, and that burst
is what gets cut.

The script deliberately **skips** roughly a third of fillers — the ones whose energy
merges into a neighbouring word, where there is no silence to cut on. Removing those
clips real speech. **60–70% removal with zero words lost is the correct outcome;
100% is not.** A tool that claims all of them is either lying or cutting words.

Discourse markers (`like`, `you know`, `basically`) are counted and reported but
never cut — removing them changes sentences, not just noise.

Every cut lands in `cuts.csv` with a timestamp so a human can veto any of them.

### 5. Cold open

Webinars routinely open with several minutes of "can you hear me", waiting for a
guest to get logged in, and chat chatter. That is the worst possible opening on
YouTube. But **don't just lop off the first N minutes** — there is usually a good
line buried in there.

Read the opening transcript, pick the keepers, and write the removals into
`cold_open.json` as `[[start, end], ...]` in source seconds. A working pattern: the
greeting, the one-line guest introduction, the strongest hook the host says, the
handoff — then straight into the guest's first substantive sentence.

Watch for lines that stop making sense once the cut lands: an apology for a delay
that no longer exists, "as I mentioned earlier", a reference to a poll you removed.

The script prints the reconstructed opening. Read it before rendering.

### 6. Render

```bash
python3 scripts/render.py --src raw.mp4 --cuts cuts.json --out edited.mp4
```

Three constraints are baked in, each learned from a wrong render:

- **`select`/`aselect`, not `trim`+`concat`.** Hundreds of trim branches force
  ffmpeg to split the input that many ways and buffer most of the file.
- **ffmpeg's expression parser dies past ~100 `between()` terms** with "Cannot
  allocate memory" — 100 works, 140 does not. Keeps are rendered in batches of 80
  and joined with the concat demuxer.
- **Never `-ss` to seek to a batch.** Input seeking lands on the preceding keyframe
  without discarding the pre-roll, which shifts the filter's `t` by up to a GOP and
  puts every cut on the wrong word. Each pass decodes from 0 — around 100×
  realtime — and uses absolute timestamps.

### 7. Verify — non-negotiable

```bash
python3 scripts/verify_edit.py --before transcript.json --after edited.mp4
```

Re-transcribes the **rendered output** and diffs it against the source. Two numbers
decide it:

| Signal | Healthy | Means |
|---|---|---|
| fillers before → after | large drop | cuts are landing on fillers |
| non-filler word count | flat (±1%) | no speech was clipped |

Fillers barely moving **and** real words vanishing is the timebase-drift signature
from step 2. Then spot-check the actual audio at one mapped timestamp — a
transcript-to-transcript comparison cannot detect a timebase problem, because both
sides drift together.

### 8. Thumbnail

Judge it at **168px**, not at full size. The most common failure is a beautiful
1280×720 image that is an unreadable smudge in a results grid. Measure rather than
squint:

```bash
python3 - <<'PY'
from PIL import Image; import numpy as np
a = np.array(Image.open("thumb.jpg").convert("L")).astype(float)
print(f"mean luma {a.mean():.0f}/255, below-40 {(a<40).mean()*100:.0f}%")
PY
```

Rules of thumb that held up:

- **Over ~65% of pixels below luma 40 and the tile disappears** in a bright grid.
  Moody night scenes are exactly the trap.
- **A face needs to be recognisable at 168px** — roughly 80px+ of head height in the
  1280-wide master. A person composited at photorealistic scale inside a scene ends
  up ~7px tall and communicates nothing.
- ≤ 4 words per line, ≤ 3 lines, one highlight colour. State the payoff, not the
  topic. Don't repeat the video title — it already sits under the thumbnail.
- Faces come from real sources only: a frame of the footage, or a photo the person
  supplied. Never an AI-invented face of a real person.
- `scripts/liftsubject.swift` does background removal locally and free on macOS via
  Vision's foreground-instance mask — the same engine as Preview's Lift Subject. No
  image API needed.

If a real person's face is composited into a scene they were never in, get their
consent before publishing.

### 9. Metadata

- **Chapters from the slides, not from memory.** `scripts/ocr_slides.swift` reads
  slide titles off sampled frames (one per 10 s, collapse repeats) — real chapter
  names in a couple of minutes. Then map each source timestamp through the cut list;
  chapters must be in *edited* time.
- Unwrap any hard-wrapped markdown into real paragraphs before sending. YouTube does
  its own wrapping.
- Keep the title under ~70 characters so it survives truncation in search results.

### 10. Publish

`reference/publishing.md` has the staging chain for a Composio-connected account,
including the part that trips people up: the upload wants a file already in
Composio's storage, and a local path fails.

**Upload private.** The owner publishes. Then verify duration, custom thumbnail,
processing status and privacy through the API rather than assuming the upload did
what it said.

## Rules

- Report what you measured, not what you intended. "70% of fillers removed, no
  speech lost" is a claim you can defend; "removed all the umms" is not.
- Keep the raw download. Every re-cut re-renders from it.
- If a step's verification fails, fix the cause — do not loosen the check.

## What this skill does NOT do

- Short vertical clips from the recording
- Live-stream production
- Publishing public — that stays a human decision

## Reference

- `reference/webinar.config.example.md` — copy to `webinar.config.md` and fill in
- `reference/platform-retrieval.md` — getting the MP4 off the webinar host
- `reference/publishing.md` — the upload chain and its failure modes

## Self-improvement

This skill should get better every time it runs. Before finishing a run that taught
you something — a correction from the user, a failure mode you hit, a step that was
ambiguous, a rule you had to infer — fold it back in.

Prefer the strongest form the lesson supports:

1. **Enforce it in a script.** An assert or check that makes the mistake impossible
   is worth more than a paragraph asking nicely.
2. **State it as a rule here**, with the *why* — that is what lets the next run
   resolve an edge case the rule didn't anticipate.
3. **Put it in `reference/`** when it is detail that would bloat this file.

Change only what the lesson touches. Record the evidence and the rule, not the war
story. Don't add speculative rules for things that haven't actually gone wrong —
they cost context on every future run.
