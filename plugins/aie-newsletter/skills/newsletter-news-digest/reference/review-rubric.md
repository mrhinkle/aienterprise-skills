# News digest — review rubric

Score out of 100. The edition advances only at `review.pass_score` (default 90)
or above. Record the score in the staged entry's `review_score_field`.

Run the `ai-slop-killer` prose pass before scoring.

| Dimension | Pts | What it scores |
|---|---|---|
| Correctness | 30 | Every factual claim (numbers, dates, attributions, superlatives) verified against a primary source via web search |
| Story selection & freshness | 20 | Big Story and Quick Hits inside the freshness window; Quick Hits cover distinct vectors; tools are real discoveries |
| Business read | 20 | Every item closes on a clear "so what" for the reader; the Big Story passes the "tell a friend" test |
| Structure & completeness | 15 | All sections present with the configured counts; headlines work as standalone lines; inside the word range |
| Style & voice | 15 | Matches the style file and persona; no banned words or phrases; spelling rules followed; every link canonical |
| **Total** | **100** | **Pass ≥ pass_score** |

## Auto-fail

Do not stage until fixed, whatever the score:

- An uncited statistic or factual claim presented as fact
- Any link to a source in `citations.never_link_to` instead of a canonical one
- A dead link
- A missing section
- A word from `banned_words`

## Correctness traps — check every time

- **Funding rounds:** who *led* versus who *participated*.
- **Pricing comparisons:** check the actual numbers on the vendor's pricing page.
- **Dates:** each Big Story and Quick Hit date sits inside the freshness window.
- **Superlatives:** "largest ever," "first to," "only" — find the source that
  says so, or cut the superlative.

## Concentration rule

If any single company is named in more than
`editions.news_digest.max_share_single_company` (default 40%) of the Key
Takeaways and Quick Hits combined, the edition is too narrow. Swap a story.
