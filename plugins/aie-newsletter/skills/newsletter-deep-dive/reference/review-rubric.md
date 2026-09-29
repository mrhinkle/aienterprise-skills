# Deep dive — review rubric

Score out of 100. The edition advances only at `review.pass_score` (default 90)
or above. Verify every statistic, source, and claim via web search before
scoring. Record the score in the staged entry's `review_score_field`.

Run the `ai-slop-killer` prose pass before scoring.

| Dimension | Pts | What it scores |
|---|---|---|
| Executive Summary | 20 | Stands alone; thesis + 3–4 sourced findings + posture line; inside `exec_summary_words` |
| Argument & evidence | 20 | Thesis stated early; at least `min_sources_deep_dive` unique high-quality sources; counterargument acknowledged; no logical gaps |
| Narrative & engagement | 20 | Specific first-person hook; reader pull sustained; at least 2 quotable lines |
| Structure & completeness | 20 | All sections present; correct heading levels; inside the word range; configured count of named missteps and key takeaways |
| Actionability | 10 | A senior reader could use it to inform a real decision; takeaways are imperative; close is a playbook |
| Style & voice | 10 | Matches the style file and persona; citations in the configured style; no banned words or phrases; spelling rules followed |
| **Total** | **100** | **Pass ≥ pass_score** |

## Auto-fail

Do not stage until fixed, whatever the score:

- An unsourced statistic presented as fact
- A dead link on a key claim
- A missing Executive Summary or Key Takeaways block
- Fewer than `citations.min_sources_deep_dive` external sources
- A fabricated personal anecdote
- A word from `banned_words`
