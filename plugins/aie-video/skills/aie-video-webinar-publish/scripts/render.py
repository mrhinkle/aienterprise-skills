#!/usr/bin/env python3
"""Render the edited cut from a cuts.json produced by build_edit.py.

Three constraints shape this, each learned from a wrong render:

  * select/aselect, not trim+concat. 200+ trim branches force ffmpeg to split the
    input that many ways and buffer most of the file.
  * ffmpeg's expression parser cannot allocate a select expression much past ~100
    terms ("Cannot allocate memory"); 100 works, 140 fails. So keeps are rendered
    in batches and joined with the concat demuxer.
  * -ss must NOT be used to skip to a batch. Input seeking lands on the preceding
    keyframe without discarding the pre-roll, which shifts the filter's `t` by up
    to a GOP and puts every cut on the wrong word. Each pass decodes from 0
    (~100x realtime) and uses absolute timestamps; select drops the rest.
"""
import argparse, json, subprocess, sys
from pathlib import Path

BATCH = 80          # select terms per pass; 100 works, 140 fails, 80 is margin


def encode(src, keeps, out, crf):
    expr = "+".join(f"between(t,{s:.3f},{e:.3f})" for s, e in keeps)
    graph = (f"[0:v]select='{expr}',setpts=N/FRAME_RATE/TB[vout];"
             f"[0:a]aselect='{expr}',asetpts=N/SR/TB[aout]")
    gf = Path(f"{out}.graph.txt"); gf.write_text(graph)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-stats", "-i", src,
         "-filter_complex_script", str(gf), "-map", "[vout]", "-map", "[aout]",
         "-c:v", "libx264", "-crf", str(crf), "-preset", "veryfast",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
         "-ar", "44100", "-ac", "2", out],
        check=True)
    gf.unlink()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", help="source mp4 (default: the one recorded in cuts.json)")
    ap.add_argument("--cuts", default="cuts.json")
    ap.add_argument("--out", required=True)
    ap.add_argument("--crf", type=int, default=21)
    a = ap.parse_args()

    data = json.loads(Path(a.cuts).read_text())
    src = a.src or data.get("source")
    if not src or not Path(src).exists():
        sys.exit(f"source mp4 not found: {src!r} (pass --src)")
    keeps = [tuple(k) for k in data["keeps"]]
    if not keeps:
        sys.exit("no keep segments in cuts.json")

    groups = [keeps[i:i + BATCH] for i in range(0, len(keeps), BATCH)]
    tmp = Path(a.out + ".parts"); tmp.mkdir(exist_ok=True)
    parts = []
    for i, g in enumerate(groups):
        p = tmp / f"part_{i:03d}.mp4"
        print(f"pass {i + 1}/{len(groups)}  {len(g)} segs  "
              f"{g[0][0] / 60:.1f}-{g[-1][1] / 60:.1f} min", flush=True)
        encode(src, g, str(p), a.crf)
        parts.append(p)

    lst = tmp / "concat.txt"
    lst.write_text("".join(f"file '{p.name}'\n" for p in parts))
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", "-movflags", "+faststart",
                    a.out], check=True)

    kept = sum(e - s for s, e in keeps)
    print(f"wrote {a.out}  ({kept / 60:.2f} min expected)")
    print("now VERIFY: scripts/verify_edit.py --before <scribe_full.json> --after "
          f"{a.out}")


if __name__ == "__main__":
    main()
