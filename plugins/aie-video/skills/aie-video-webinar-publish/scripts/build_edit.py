#!/usr/bin/env python3
"""Build a cut list that removes filler words (and an optional cold open).

Why this is not a one-liner over the transcript:

  ElevenLabs Scribe marks word ONSETS accurately but badly truncates word ENDS --
  it reported an audibly ~280 ms "uh" as lasting 10 ms. A window built from
  [start, end] + padding therefore clips only the filler's tail and leaves it
  plainly audible in the render. So the transcript is used to LOCATE each filler
  and the audio decides where it actually starts and stops: a filler is one burst
  of speech energy bounded by silence, and that burst is what gets cut.

  Fillers whose burst merges into a neighbouring word are skipped, not forced.
  There is no silence to cut on, so removing them would clip real speech.

Writes cuts.json (machine) and cuts.csv (a vetoable log for a human).
"""
import argparse, csv, json, re, subprocess, sys
from pathlib import Path

FILLERS = {"um", "umm", "ummm", "uh", "uhh", "uhhh", "er", "err", "erm",
           "ah", "ahh", "eh", "hm", "hmm", "mm", "mhm"}
# Counted and reported, never cut: removing these changes sentences, not noise.
MARKERS = {"like", "basically", "actually", "literally", "right"}

PAD = 0.06          # breathing room before the filler's reported onset
ONSET_GUARD = 0.03  # never clip the next word's onset, which Scribe gets right
MAX_CUT = 3.00      # a runaway window means a bad timestamp; skip it
KEEP_BEAT = 0.15    # natural pause handed back when the cut span is long


def norm(w):
    """Scribe attaches punctuation to tokens ("uh," / "Um..."). Strip it."""
    return re.sub(r"[^\w']", "", w).lower()


def energy_envelope(path, hop=0.01):
    """Per-frame dB envelope plus a speech threshold above the noise floor."""
    import numpy as np, soundfile as sf
    y, sr = sf.read(path, dtype="float32")
    if y.ndim > 1:
        y = y.mean(axis=1)
    H = int(hop * sr)
    n = len(y) // H
    rms = np.sqrt(np.maximum(1e-12, np.array(
        [np.mean(y[i * H:(i + 1) * H] ** 2) for i in range(n)])))
    db = 20 * np.log10(rms)
    return db, hop, float(np.percentile(db, 20)) + 12.0


def check_timebase(src, audio):
    """The WAV must share the MP4's timebase or every cut lands on the wrong word."""
    def dur(cmd):
        return float(subprocess.run(cmd, capture_output=True, text=True).stdout.strip())
    a = dur(["ffprobe", "-v", "error", "-select_streams", "a",
             "-show_entries", "stream=duration", "-of", "csv=p=0", src])
    w = dur(["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", audio])
    if abs(a - w) > 0.15:
        sys.exit(
            f"TIMEBASE MISMATCH: {src} audio is {a:.2f}s, {audio} is {w:.2f}s "
            f"({a - w:+.2f}s).\nRe-extract with:\n"
            f'  ffmpeg -y -i "{src}" -vn -af "aresample=async=1:first_pts=0" '
            f'-ac 1 -ar 16000 -c:a pcm_s16le "{audio}"')
    print(f"timebase ok      mp4 {a:.2f}s / wav {w:.2f}s")
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="source mp4")
    ap.add_argument("--audio", required=True, help="timing-preserving wav (see --help of the skill)")
    ap.add_argument("--transcript", required=True, help="ElevenLabs Scribe json")
    ap.add_argument("--cold-open", help="json list of [start,end] ranges to remove outright")
    ap.add_argument("--out", default="cuts.json")
    a = ap.parse_args()

    total = check_timebase(a.src, a.audio)

    data = json.loads(Path(a.transcript).read_text())
    words = [w for w in data["words"]
             if w.get("type") == "word" and w.get("start") is not None]
    if not words:
        sys.exit("no word timestamps in transcript (is this a Scribe response?)")

    marker_count = sum(1 for w in words if norm(w["text"]) in MARKERS)
    n_fillers = sum(1 for w in words if norm(w["text"]) in FILLERS)

    # Group CONSECUTIVE fillers into runs. "we have, uh, um, Don" is one run:
    # cutting each against its immediate neighbour leaves slivers that spare the rest.
    runs, i = [], 0
    while i < len(words):
        if norm(words[i]["text"]) in FILLERS:
            j = i
            while j < len(words) and norm(words[j]["text"]) in FILLERS:
                j += 1
            runs.append((i, j - 1))
            i = j
        else:
            i += 1

    env, hop, thr = energy_envelope(a.audio)
    nfr = len(env)

    def frame(t):
        return max(0, min(nfr - 1, int(round(t / hop))))

    def burst_around(t_on, t_off):
        """The speech burst containing the filler, bounded by silence either side."""
        f = frame(t_on)
        if env[f] < thr:                      # onset slightly early: step into speech
            for d in range(1, frame(0.30) + 1):
                if f + d < nfr and env[f + d] >= thr:
                    f += d
                    break
            else:
                return None
        s = f
        while s > 0 and env[s - 1] >= thr:
            s -= 1
        e = max(f, frame(t_off))
        while e + 1 < nfr and env[e + 1] >= thr:
            e += 1
        return s, e

    cuts, log, skipped = [], [], 0
    for i0, i1 in runs:
        prev_end = words[i0 - 1]["end"] if i0 else 0.0
        next_start = (words[i1 + 1]["start"] if i1 + 1 < len(words)
                      else words[i1]["end"] + 10)

        got = burst_around(words[i0]["start"], words[i1]["end"])
        if got is None:
            skipped += 1
            continue
        s, e = got
        lo, hi = s * hop - 0.01, e * hop + hop + 0.01

        # The burst must be the filler alone. If it ran into a neighbouring word we
        # cannot separate them by energy, so leave it: clipping speech is worse.
        if lo < prev_end - 0.12 or hi > next_start + 0.12 or (hi - lo) > 1.2:
            skipped += 1
            continue

        # Cutting the burst leaves silence on both sides, which reads as an
        # unnaturally long pause. Reclaim the surplus beyond one natural beat.
        gap = (lo - prev_end) + (next_start - hi)
        if gap > KEEP_BEAT:
            hi = min(hi + (gap - KEEP_BEAT), next_start - ONSET_GUARD)

        if not (0.06 <= hi - lo <= MAX_CUT):
            skipped += 1
            continue
        cuts.append((lo, hi))
        log.append({"word": " ".join(w["text"].strip() for w in words[i0:i1 + 1]),
                    "start": round(lo, 3), "end": round(hi, 3), "dur": round(hi - lo, 3)})

    cold = []
    if a.cold_open:
        cold = [tuple(r) for r in json.loads(Path(a.cold_open).read_text())]
        cuts.extend(cold)
        print(f"cold open        {len(cold)} ranges, {sum(b - x for x, b in cold):.1f}s")

    cuts.sort()
    merged = []
    for lo, hi in cuts:
        if merged and lo <= merged[-1][1] + 0.02:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])

    keeps, pos = [], 0.0
    for lo, hi in merged:
        if lo - pos > 0.05:
            keeps.append((pos, lo))
        pos = hi
    if total - pos > 0.05:
        keeps.append((pos, total))

    removed = sum(b - x for x, b in merged)
    json.dump({"source": a.src, "source_duration": total, "cuts": log,
               "cold_open": cold, "merged": merged, "keeps": keeps,
               "removed_seconds": removed,
               "discourse_markers_left_alone": marker_count},
              open(a.out, "w"), indent=1)
    with open(Path(a.out).with_suffix(".csv"), "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["word", "start", "end", "dur"])
        wr.writeheader(); wr.writerows(log)

    print(f"filler runs      {len(runs)} ({n_fillers} words) | cut {len(log)} | skipped {skipped}")
    print(f"removed          {removed:.1f}s ({removed / total * 100:.1f}%)")
    print(f"output length    {(total - removed) / 60:.2f} min")
    print(f"kept segments    {len(keeps)}")
    print(f"markers left     {marker_count} (like/basically/actually/... never cut)")


if __name__ == "__main__":
    main()
