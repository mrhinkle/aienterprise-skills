# Tactic — review rubric

Score out of 100. The edition advances only at `review.pass_score` (default 90)
or above, **after** the expert panel's Must Fix and Should Fix items are
applied. Record the final score in the staged entry's `review_score_field`.

Run the `ai-slop-killer` prose pass before scoring.

| Dimension | Pts | What it scores |
|---|---|---|
| Usable today | 25 | The reader can act within `act_within_minutes`; the artifact works as written |
| Artifact quality | 20 | The template or prompt is complete, has clear fill-ins, and shows a realistic sample output |
| Correctness | 20 | Every claim and the news hook verified against a primary source and cited |
| Tight | 15 | Under the word cap; every sentence earns its place; no padding |
| Voice & style | 10 | Matches the style file and persona; first-person problem opener; no banned words or phrases; spelling rules followed |
| Differentiation | 10 | A tactic: not a news roundup, not a tutorial, not a strategic analysis |
| **Total** | **100** | **Pass ≥ pass_score** |

## Auto-fail

Do not stage until fixed, whatever the score:

- The artifact does not work
- An uncited claim presented as fact
- Over the word cap
- A word from `banned_words`
