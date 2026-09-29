# Analogy Bank

Starting pairings, not scripts. Always verify the structural match for the specific question, and describe references in your own words.

| Concept | Pattern | Candidate 1980s reference | Where the match holds | Where it breaks |
|---|---|---|---|---|
| Context window | Memory | A car's dashboard sensors in *Knight Rider* | Only what is in view right now is usable | Real models have no persistent memory between sessions by default |
| Vector database | Storage | A library card catalog, sorted by topic similarity instead of alphabet | Finds "close" items, not exact matches | Card catalogs are exact; similarity search is probabilistic |
| RAG | Memory | Looking things up in an encyclopedia set before answering a quiz question | Answer grounded in a reference | Encyclopedias are curated; your documents may not be |
| Tokens | Assembly line | Arcade tokens: every play costs a fixed unit | Usage and cost are counted in small units | Tokens are pieces of words, not whole words |
| Fine-tuning | Cast and crew | A new cast member rehearsing for a specific long-running TV role | Specializes a general performer | Fine-tuning changes model weights, not just instructions |
| Prompting | Coordinator | A director's notes before a take | Shapes the performance without retraining | Notes can be ignored or misread |
| Agents | Coordinator | *MacGyver* improvising a plan from available tools | Goal, tools, sequence of actions | Needs guardrails and supervision |
| Multi-agent systems | Cast and crew | *The A-Team*, each member with a specialty | Specialized roles, one coordinator | Real agents can loop, disagree, or duplicate work |
| Guardrails | Control room | Bowling lane bumpers | Prevent the worst outcomes | Do not improve aim |
| Evaluation | Control room | High-score tables on an arcade cabinet | Consistent scoring lets you compare runs | Benchmarks can be gamed |
| Hallucination | Memory | A game show contestant who bluffs confidently instead of passing | Confident wrong answer | Models are not "choosing" to bluff |
| Model drift | Assembly line | A cassette tape copied from a copy, getting noisier | Quality degrades over time | Drift comes from changing data, not copying |
| Orchestration | Coordinator | An air traffic control scene in a disaster comedy of the era | One layer routes many moving parts | Keep the tone serious enough for the room |

## Picking well

1. Name the structure of the concept in one phrase (for example: "finds similar things, not identical things").
2. Pick the reference whose mechanics share that phrase.
3. Write the "where it breaks" line before you commit. If it is longer than the analogy, pick again.
