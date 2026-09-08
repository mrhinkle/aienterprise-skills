# Video bundle (beta)

`aie-video-webinar-publish` — one skill, one job: take a raw webinar recording and
produce a YouTube video worth clicking, without silently mangling the speech.

> **Beta.** The editing and verification stages are proven on real hour-long
> recordings. The upload stage assumes a Composio-connected YouTube account. If
> yours is wired differently, stop after verification and upload by hand —
> everything before that is platform-independent.

## What it actually does

1. Pulls the MP4 off the webinar platform (the recording is rarely in the API).
2. Extracts audio **with timestamps preserved** — the step that quietly breaks
   everything if you skip it.
3. Transcribes with a verbatim ASR that keeps disfluencies.
4. Builds a cut list for the umms and ahs, using the transcript to *find* each
   filler and the audio waveform to decide where it starts and stops.
5. Cuts the "can you hear me" cold open, keeping the good lines buried in it.
6. Renders, in batches, with the ffmpeg constraints that actually hold.
7. **Verifies by re-transcribing the render** and diffing it against the source.
8. Builds a thumbnail judged at 168px, not at full size.
9. Generates chapters by OCR-ing the slides.
10. Uploads private for a human to publish.

## Setup

```bash
pip install numpy soundfile     # ffmpeg must also be on PATH
```

Copy `reference/webinar.config.example.md` to `webinar.config.md` and fill in your
channel, brand and platform details.

You need a **verbatim** ASR key. The scripts expect ElevenLabs Scribe
(`ELEVENLABS_API_KEY`). Whisper will not work for this — see below.

## Three things worth knowing before you run it

**Whisper deletes filler words.** It is trained to tidy speech. On the same hour of
audio, Whisper found 5 fillers; a verbatim model found 294. Prompting it for
verbatim output does not fix this. If your filler-removal tool reports that your
speakers are remarkably clean, suspect the ASR before believing it.

**Word-end timestamps are unreliable.** Onsets are good; ends are badly truncated —
one audibly ~280 ms "uh" was reported as lasting 10 ms. Cutting `[start, end]`
clips the tail and leaves the filler plainly audible. This skill takes the real
boundaries from audio energy instead.

**100% filler removal is a red flag.** Around a third of fillers run straight into a
neighbouring word with no silence to cut on. Removing those clips real speech. The
correct outcome is 60–70% removed with the non-filler word count flat.

## The verification step is the point

```bash
python3 scripts/verify_edit.py --before transcript.json --after edited.mp4
```

| Signal | Healthy | Means |
| --- | --- | --- |
| fillers before → after | large drop | cuts are landing on fillers |
| non-filler word count | flat (±1%) | no speech was clipped |

Fillers barely moving **and** real words vanishing means the audio you transcribed
drifted against the video — go back to the extraction step. Comparing two
transcripts cannot catch this on its own, because both sides drift together. Always
spot-check the actual rendered audio at one mapped timestamp.

## Thumbnails

Judge at 168px. The common failure is a beautiful 1280×720 image that is an
unreadable smudge in a results grid.

- Over ~65% of pixels below luma 40 and the tile disappears against a bright grid.
- A face needs ~80px of head height in the 1280-wide master to be recognisable at
  168px. A person composited at photorealistic scale inside a scene lands around
  7px and communicates nothing.
- Faces come from real sources only — a frame of the footage or a photo the person
  supplied. If you composite someone's real face into a scene they were never in,
  get their consent before publishing.

On macOS, `scripts/liftsubject.swift` does background removal locally and free via
Vision's foreground-instance mask (the same engine as Preview's Lift Subject).

## Files

| Path | What it is |
| --- | --- |
| `scripts/build_edit.py` | Cut list from transcript + audio energy; asserts the timebase |
| `scripts/render.py` | Batched `select`/`aselect` render, concat-joined |
| `scripts/verify_edit.py` | Re-transcribes the output and diffs it |
| `scripts/liftsubject.swift` | macOS Vision subject cutout |
| `scripts/ocr_slides.swift` | macOS Vision slide-title OCR for chapters |
| `reference/platform-retrieval.md` | Getting the MP4 off the webinar host |
| `reference/publishing.md` | The upload chain and its failure modes |
| `reference/webinar.config.example.md` | Copy to `webinar.config.md` |

## Known gaps

- Scripts assume macOS for the two Swift tools; the Python pipeline is portable.
- Chapters need slides on screen — a talking-head-only recording won't OCR.
- No Shorts/clip extraction yet.
