#!/usr/bin/env python3
"""
Manuscript rubric scoring helper.

Usage:
    python3 score.py <s1> <s2> ... <sN>
    python3 score.py key=score key=score ...
    python3 score.py --rubric path/to/rubric.json <scores...>
    python3 score.py --show [--rubric path/to/rubric.json]

Scores are 0-100, one per rubric dimension, in rubric order (or as key=score
pairs in any order). With no --rubric, the default eight-dimension rubric is
used. A custom rubric is a JSON file:

    {
      "name": "My Book rubric",
      "dimensions": [
        {"key": "theme", "name": "Theme & Meaning", "weight": 0.13},
        ...
      ]
    }

Weights should sum to 1.0 (or 100). If they don't, they are normalized and a
warning is printed. Prints the weighted total, a per-dimension table, and the
chapter- and manuscript-level decisions. Standard library only.
"""

import json
import sys

DEFAULT_RUBRIC = {
    "name": "Default novel rubric",
    "dimensions": [
        {"key": "theme",     "name": "Theme & Meaning",          "weight": 0.13},
        {"key": "story",     "name": "Story Engine",             "weight": 0.14},
        {"key": "character", "name": "Character",                "weight": 0.14},
        {"key": "world",     "name": "World & Authenticity",     "weight": 0.12},
        {"key": "voice",     "name": "Voice & Prose",            "weight": 0.12},
        {"key": "dialogue",  "name": "Dialogue",                 "weight": 0.11},
        {"key": "pacing",    "name": "Pacing & Structure",       "weight": 0.14},
        {"key": "hook",      "name": "Hook & Reader Conversion", "weight": 0.10},
    ],
}


def band(score: float) -> str:
    if score >= 90: return "Exceptional"
    if score >= 75: return "Strong"
    if score >= 60: return "Solid"
    if score >= 40: return "Weak"
    if score >= 20: return "Failing"
    return "Broken"


def chapter_decision(total: float) -> str:
    if total >= 85: return "Lock it. Move on."
    if total >= 70: return "One more revision pass on the lowest-scoring dimensions."
    if total >= 55: return "Structural problem. Diagnose before line-editing."
    return "Cut, rewrite, or move to a different position in the book."


def manuscript_decision(total: float) -> str:
    if total >= 85: return "Submit or publish with confidence."
    if total >= 75: return "One more developmental pass with a trusted editor."
    if total >= 60: return "Major revision. Likely a structural or character problem."
    return "Back to the outline."


def fail(msg: str) -> int:
    print(msg, file=sys.stderr)
    return 1


def load_rubric(path):
    if path is None:
        return DEFAULT_RUBRIC
    with open(path, encoding="utf-8") as fh:
        rubric = json.load(fh)
    dims = rubric.get("dimensions")
    if not isinstance(dims, list) or not dims:
        raise ValueError("Rubric JSON needs a non-empty 'dimensions' list.")
    for i, d in enumerate(dims):
        if "name" not in d or "weight" not in d:
            raise ValueError(f"Dimension {i + 1} needs 'name' and 'weight'.")
        d.setdefault("key", d["name"].split()[0].lower().strip("&,"))
        d["weight"] = float(d["weight"])
    rubric.setdefault("name", path)
    return rubric


def normalized_weights(dims):
    total = sum(d["weight"] for d in dims)
    if total <= 0:
        raise ValueError("Rubric weights must sum to more than zero.")
    if abs(total - 1.0) > 0.001:
        if abs(total - 100.0) > 0.1:
            print(f"Warning: weights sum to {total:g}; normalizing to 1.0.",
                  file=sys.stderr)
        return [d["weight"] / total for d in dims]
    return [d["weight"] for d in dims]


def parse_scores(args, dims):
    keyed = [a for a in args if "=" in a]
    if keyed and len(keyed) != len(args):
        raise ValueError("Use either all positional scores or all key=score pairs.")
    if keyed:
        by_key = {}
        for a in keyed:
            k, v = a.split("=", 1)
            by_key[k.strip().lower()] = float(v)
        keys = [d["key"].lower() for d in dims]
        missing = [k for k in keys if k not in by_key]
        extra = [k for k in by_key if k not in keys]
        if missing or extra:
            raise ValueError(f"Missing keys: {missing or 'none'}; unknown keys: {extra or 'none'}.")
        scores = [by_key[k] for k in keys]
    else:
        if len(args) != len(dims):
            raise ValueError(f"Expected {len(dims)} scores, got {len(args)}. "
                             f"Run with --show to see the dimensions.")
        scores = [float(x) for x in args]
    for s in scores:
        if not 0 <= s <= 100:
            raise ValueError(f"Score out of range: {s:g}. Each must be 0-100.")
    return scores


def show(rubric, weights):
    print(f"\n{rubric['name']}\n")
    print(f"{'#':<4}{'Key':<14}{'Dimension':<32}{'Weight':>8}")
    print("-" * 58)
    for i, (d, w) in enumerate(zip(rubric["dimensions"], weights), 1):
        print(f"{i:<4}{d['key']:<14}{d['name']:<32}{w:>8.2f}")
    print()


def main(argv) -> int:
    args = list(argv)
    rubric_path = None
    want_show = False
    if "--help" in args or "-h" in args:
        print(__doc__)
        return 0
    if "--rubric" in args:
        i = args.index("--rubric")
        if i + 1 >= len(args):
            return fail("--rubric needs a path.")
        rubric_path = args[i + 1]
        del args[i:i + 2]
    if "--show" in args:
        want_show = True
        args.remove("--show")

    try:
        rubric = load_rubric(rubric_path)
        dims = rubric["dimensions"]
        weights = normalized_weights(dims)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return fail(f"Could not load rubric: {exc}")

    if want_show:
        show(rubric, weights)
        return 0
    if not args:
        print(__doc__)
        show(rubric, weights)
        return 1

    try:
        scores = parse_scores(args, dims)
    except ValueError as exc:
        return fail(str(exc))

    width = max(25, max(len(d["name"]) for d in dims) + 2)
    print(f"\n{rubric['name']}")
    print(f"\n{'Dimension':<{width}}{'Score':>8}{'Weight':>10}{'Weighted':>12}  Band")
    print("-" * (width + 38))
    total = 0.0
    for d, w, s in zip(dims, weights, scores):
        weighted = s * w
        total += weighted
        print(f"{d['name']:<{width}}{s:>8.1f}{w:>10.2f}{weighted:>12.2f}  {band(s)}")
    print("-" * (width + 38))
    print(f"{'FINAL':<{width}}{'':>8}{'':>10}{total:>12.2f}  {band(total)}")
    print()
    print(f"Chapter-level decision:    {chapter_decision(total)}")
    print(f"Manuscript-level decision: {manuscript_decision(total)}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
