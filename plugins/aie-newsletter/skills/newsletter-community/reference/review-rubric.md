# Community newsletter — review rubric

Score out of 100. The edition advances only at `review.pass_score` (default 90)
or above. Verify every date, price, and link before scoring.

Run the `ai-slop-killer` prose pass before scoring.

| Dimension | Pts | What it scores |
|---|---|---|
| Correctness | 25 | Every date, price, speaker detail, and claim verified against its source and cited or linked |
| Events roundup | 20 | Every configured source checked; sorted by date; full day and month names; every title links to a canonical event page |
| Drives action | 20 | Each section ends in a clear next step; the key ask is unmistakable |
| Opening & voice | 15 | Opening reads as the organizer's own note; warm, community-first; matches the style file |
| Structure & format | 10 | Sections in order; article titles as bare H2s; no tables; sign-off from config; metadata kept out of the body |
| Style | 10 | No banned words or phrases; spelling rules followed |
| **Total** | **100** | **Pass ≥ pass_score** |

## Auto-fail

Do not stage until fixed, whatever the score:

- An event linked to a group homepage instead of its event page
- A wrong date or price
- A table in the body
- An uncited claim presented as fact
- A word from `banned_words`
