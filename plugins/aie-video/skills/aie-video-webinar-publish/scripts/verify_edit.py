#!/usr/bin/env python3
"""Verify an edit by re-transcribing the RENDERED OUTPUT and diffing it.

This exists because every other check passes while the edit is silently wrong.
If the audio timebase drifted (see build_edit.check_timebase), comparing the
source transcript to the expected-survivors list still lines up perfectly --
both sides share the drift. Only re-transcribing the actual rendered file, and
listening at a mapped timestamp, catches it.

Two numbers decide it:
  fillers before -> after   should drop hard
  non-filler word count     should stay flat against what SHOULD survive

That second baseline matters: pass --cuts cuts.json when a cold-open range was
used, and the baseline becomes "words not inside any merged cut" rather than the
raw source total. Without it, a legitimate cold-open cut that removes real
dialogue (an apology, chit-chat) reads as clipped speech and fails a healthy
edit -- caught on the Build Skills recording, where a 12-minute cold-open cut
removed 272 real words and the raw-total comparison flagged a false failure at
-3.39% before the true figure (against cuts.json's keep list) was -0.7%.
"""
import argparse, json, os, re, subprocess, sys, collections
from pathlib import Path

FILLERS = {"um", "umm", "ummm", "uh", "uhh", "uhhh", "er", "err", "erm",
           "ah", "ahh", "eh", "hm", "hmm", "mm", "mhm"}


def norm(w):
    return re.sub(r"[^\w']", "", w).lower()


def scribe(mp3):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY not set (it lives in ~/.zshrc)")
    out = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.elevenlabs.io/v1/speech-to-text",
         "-H", f"xi-api-key: {key}", "-F", "model_id=scribe_v1",
         "-F", "timestamps_granularity=word", "-F", f"file=@{mp3}"],
        capture_output=True, text=True).stdout
    d = json.loads(out)
    if "words" not in d:
        sys.exit(f"Scribe error: {str(d)[:300]}")
    return d


def norm_words(d):
    return [w for w in d["words"] if w.get("type") == "word"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True, help="source transcript json (Scribe)")
    ap.add_argument("--after", required=True, help="rendered mp4")
    ap.add_argument("--cuts", help="cuts.json from build_edit.py -- use this whenever "
                                    "a cold-open range was cut, or the baseline below "
                                    "counts real removed dialogue as clipped speech")
    ap.add_argument("--keep-audio", action="store_true")
    a = ap.parse_args()

    mp3 = Path(a.after).with_suffix(".verify.mp3")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", a.after, "-vn",
                    "-af", "aresample=async=1:first_pts=0",
                    "-ac", "1", "-ar", "16000", "-c:a", "libmp3lame",
                    "-b:a", "64k", str(mp3)], check=True)
    after = scribe(str(mp3))
    Path(a.after).with_suffix(".verify.json").write_text(json.dumps(after))
    if not a.keep_audio:
        mp3.unlink(missing_ok=True)

    before_words = norm_words(json.loads(Path(a.before).read_text()))
    act = norm_words(after)

    if a.cuts:
        # Correct baseline: only words NOT inside any merged cut should survive.
        merged = [tuple(m) for m in json.loads(Path(a.cuts).read_text())["merged"]]
        def inside(w):
            return any(x <= w["start"] < y or x < w["end"] <= y for x, y in merged)
        baseline = [w for w in before_words if not inside(w)]
        baseline_label = "expected survivors (post-cuts)"
    else:
        baseline = before_words
        baseline_label = "source total (no --cuts given)"

    bw = [norm(w["text"]) for w in baseline]
    aw = [norm(w["text"]) for w in act]
    fb_src = [norm(w["text"]) for w in before_words if norm(w["text"]) in FILLERS]
    fb = [w for w in bw if w in FILLERS]
    fa = [w for w in aw if w in FILLERS]
    nb, na = len(bw) - len(fb), len(aw) - len(fa)

    def dur(p):
        return float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True).stdout.strip())
    d_after = dur(a.after)

    pct = (1 - len(fa) / len(fb_src)) * 100 if fb_src else 0.0
    drift = (na - nb) / nb * 100 if nb else 0.0
    print(f"output length  {int(d_after) // 60}:{int(d_after) % 60:02d}")
    print(f"baseline       {baseline_label}")
    print(f"fillers        {len(fb_src)} -> {len(fa)}   ({pct:.0f}% removed)")
    print(f"real words     {nb} -> {na}   ({drift:+.2f}%)")
    print(f"remaining      {dict(collections.Counter(fa).most_common(6))}")

    ok = pct >= 40 and abs(drift) <= 1.5
    if not ok:
        print("\nFAIL. Likely causes, in order:")
        if not a.cuts:
            print("  0. no --cuts given -- if a cold-open range removed real dialogue,")
            print("     re-run with --cuts cuts.json before concluding this is real drift")
        print("  1. audio timebase drift  -> re-extract with aresample=async=1,")
        print("     re-run Scribe on the synced wav, rebuild cuts")
        print("  2. cuts built from Scribe word ends rather than energy bursts")
        print("  3. -ss used to seek to a render batch")
    else:
        print("\nPASS. Spot-check the audio at one mapped timestamp before shipping.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
