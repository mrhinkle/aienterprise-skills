# Tutorial — review rubric

Score out of 100. The edition advances only at `review.pass_score` (default 90)
or above. Verify the procedure and every claim via web search before scoring.
Record the score in the staged entry's `review_score_field`.

Run the `ai-slop-killer` prose pass before scoring.

| Dimension | Pts | What it scores |
|---|---|---|
| Teaches one usable skill | 25 | The reader can do the thing after reading; scope is one skill, not five |
| The procedure works | 20 | Steps are concrete, numbered, reproducible, and verified against current tool behavior |
| Correctness | 20 | Every claim, setting, and product behavior verified against a primary source and cited |
| Hook & framing | 15 | Specific first-person hook; a clear "real shift" reframe; takeaway placed high |
| Structure & completeness | 10 | Kicker, hook, action subhead, takeaway, CTA, procedure, and close all present; inside the word range |
| Voice & style | 10 | Matches the style file and persona; no banned words or phrases; spelling rules followed |
| **Total** | **100** | **Pass ≥ pass_score** |

## Auto-fail

Do not stage until fixed, whatever the score:

- A procedure step that does not work as written
- An uncited claim presented as fact
- A missing procedure or takeaway
- A fabricated personal anecdote
- A word from `banned_words`
