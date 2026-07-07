# Slop Catalog — the field guide

Every entry: what it is, why it reads as machine-written, and the fix. **Match on the pattern, not the exact words.** A single instance of almost anything here is human; the tell is repetition and clustering. When you cut something, name the pattern so it stays visible.

Sourced from Wikipedia's *Signs of AI writing*, the tropes.fyi pattern directory, and working editors' guides (see Sources at the bottom).

---

## 1. Sentence-shape tells (the loudest)

**Negative parallelism — "Not X. It's Y."** *(the #1 tell)*
- Forms: "It's not a tool, it's a teammate." / "not because it's cheap, but because it's inevitable." / em-dash dismissal "It's bold — not reckless." / cross-sentence reframe "The question isn't how. It's why."
- Why: manufactures false profundity by framing everything as a surprising reversal. Before LLMs, nobody wrote this at scale.
- Fix: state the point plainly, once. One earned instance per piece, max.

**Triple-negation reveal — "Not X. Not Y. Just Z."**
- "Not a bug. Not a feature. A design flaw." Dramatic countdown to a "truth."
- Fix: cut to the claim.

**Rhetorical Q&A — "The X? A Y."**
- Self-posed question answered immediately: "The result? Devastating." / "Why does this matter? Because…"
- Fix: delete the question, keep the answer.

**Tricolon (rule-of-three) pile-up.**
- One triad is elegant; three back-to-back is a tic. "Products solve problems; platforms create worlds. Products scale linearly; platforms scale exponentially…"
- Fix: break the rhythm — use two items, or four, or a full sentence. One triad per section.

**Anaphora abuse.**
- Same sentence-opening repeated in quick succession: "They assume users will pay. They assume developers will build. They assume ecosystems will emerge."
- Fix: vary the openings; keep one repetition if it genuinely drives.

**False ranges — "from X to Y."**
- Implies a spectrum that doesn't exist: "from innovation to cultural transformation." What's the middle? Nothing.
- Fix: name the two things plainly or cut one.

**"The kind of X that Y" / "something that felt like Z."** Reflexive simile scaffolding. Usually cut whole.

**Superficial analysis — trailing "-ing" phrase.**
- Bolts fake significance onto a fact: "…, highlighting its importance," "…, reflecting broader trends," "…, contributing to the region's rich heritage."
- Fix: cut the participial tail, or replace with a real, specific consequence.

**"Serves as / stands as / represents" dodge.**
- Pompous substitutes for "is." "The building serves as a reminder…" → "The building reminds…"

---

## 2. Structural / composition tells

**Wind-up intro.** "In today's fast-paced world…", "In an era where…", "At its core…". Delete; start at the first real sentence. (The real article usually starts in paragraph two.)

**Signposted conclusion.** "In conclusion," "To sum up," "At the end of the day," "Ultimately." Competent writing doesn't announce it's ending. Cut, or end on a concrete beat / call to action.

**False-suspense transition.** "Here's the kicker," "Here's the thing," "Here's what most people miss," "That's only half the story," "Real talk." Manufactured drama before an unremarkable point. Cut and just say it.

**Pedagogical voice / "Think of it as…".** "Let's break this down," "Let's unpack this," "Think of it like a highway for data." Teacher-to-student tone even for expert readers, often with an analogy less clear than the thing. Cut the framing; keep the substance.

**"Imagine a world where…" / "Picture this…".** Futurist invitation or fake-empathy scenario ("As a business owner, you know…"). Replace with a specific, messy, real detail.

**Signposted / enumerated prose ("Listicle in a trench coat").** A list disguised as paragraphs: "The first wall is… The second wall is… The third wall is…". Convert to a real list or to genuine prose that doesn't count itself.

**Fractal summaries.** "In this section we'll explore… [3000 words] …as we've seen in this section." Every level re-summarizes itself. Cut the redundant frames.

**One-point dilution.** A single argument restated ten ways to feel "comprehensive." An 800-word point ballooned to 4000. Cut to the argument.

**Bothsidesing to a mushy middle.** RLHF-trained neutrality: "While there are challenges, there are also opportunities." Take a position or cut.

**"Despite its challenges…" formula.** Acknowledge a problem only to instantly dismiss it: "Despite these challenges, the initiative continues to thrive." Cut the reflex or engage the problem for real.

---

## 3. Tone / stance tells

**Grandiose stakes inflation.** A post about API pricing becomes "this will fundamentally reshape how we think about everything." Right-size the claim.

**Invented concept labels.** Abstract compound nouns presented as established terms: "the supervision paradox," "the acceleration trap," "workload creep." Naming a thing is not arguing it. Cut or actually make the case.

**Vague attributions.** "Experts argue," "studies show," "several publications have cited," "industry observers note." If you can't name the source, you don't have one. Name it or cut it.

**False vulnerability.** Polished, risk-free "honesty": "And yes, I'll admit I'm biased here." Real vulnerability is specific and uncomfortable; performed vulnerability is a tell.

**"The truth is simple" / "the real story is…".** Asserting something is obvious instead of proving it, or waving away everything prior to claim privileged insight. Prove it or drop it.

**Hedging / softening.** "It's important to consider," "it could be argued," "generally speaking," "aims to." RLHF politeness that signals fear of being wrong. Be direct: "This article aims to explore…" → say what it does.

---

## 4. Word-choice tells

**Hard-default banlist (documented AI overuse — replace on sight):**
delve, tapestry, landscape, realm, paradigm, testament, beacon, symphony, journey (metaphorical), roadmap, unleash, unlock, harness, leverage (verb), synergy, cutting-edge, game-changer, revolutionary, transformative, elevate, foster, streamline, robust, seamless, scalable, myriad, plethora, comprehensive, pivotal, multifaceted, holistic, underscore, utilize, spearhead, facilitate. *(Users can extend or trim this via `slop.config.md`.)*

**Magic adverbs.** "quietly" (quietly orchestrating…), "deeply," "fundamentally," "remarkably," "arguably," "notably," "seamlessly." Overused to make the mundane feel profound. Cut most.

**"It's worth noting" family.** "It bears mentioning," "importantly," "interestingly," "notably." Filler transitions that connect nothing. Cut.

**Filler connectors that pile up.** furthermore, moreover, additionally, thus, hence, that said, indeed. One or two across a piece is fine; a stack is a tell. Prefer "also," "plus," or nothing.

**"Designed to / built to / aims to" scaffolding.** "a system designed to help you…" → "a system that helps you…" or just say what it does.

**Stock phrases to kill on sight:** "it's important to note," "in a world where," "a testament to," "stark reminder," "navigate the complexities," "little did they know," "only time will tell," "when it comes to," "in order to" (→ "to"), "a wide range of," "plays a key role," "the ever-evolving," "rapidly changing," "at its core."

**The pub test (fix heuristic).** Read the sentence aloud. Would you say it to a colleague over a beer? "We empower users to optimize their workflows" → "We help you work faster." Replace abstraction with a concrete noun or number.

---

## 5. Rhythm & burstiness tells (structural, easy to miss)

**Rectangle paragraphs / low burstiness.** Every paragraph three sentences of 15–20 words, subject-verb-object, uniform. Lulls readers into skim mode. **Fix:** the high-low technique — a long explanatory sentence followed by a short punch. Vary length deliberately.

**Short-punchy-fragment spam.** The opposite failure: one thought per line, fragment paragraphs stacked for manufactured emphasis. "He published this. Openly. In a book. As a priest." A little is punchy; a page of it is an inhuman RLHF cadence. Fix: recombine into real sentences; keep fragments rare and earned.

**Dead-metaphor beating.** Introducing one metaphor and repeating it 5–10 times ("the ecosystem needs ecosystems to build ecosystem value"). Use a metaphor once, then move on.

**Historical-analogy stacking** *(common in tech writing)*. Rapid-fire company/era name-drops to fake authority: "Apple didn't build Uber. Facebook didn't build Spotify. Stripe didn't build Shopify." Keep one comparison if it earns its place.

---

## 6. Punctuation & formatting tells

**Em-dash addiction.** More than ~1 per 1–2 sentences reads as AI; humans use 2–3 per piece. Vary with periods, commas, parentheses, colons. Never a paragraph that's mostly em-dashes.

**Unicode decoration.** Curly/smart quotes mixed with straight, unicode arrows (→, ⇒), decorative bullets. Real drafts in a text editor produce straight quotes and "->". Normalize.

**Bold-first bullets.** Every list item opening with a **Bold Header:** then a sentence. Extremely common in LLM markdown; almost nobody hand-writes lists this way. Mix bullet types, drop some headers, or convert a 3-point list to a paragraph.

**Bold-word confetti / emoji bullets.** Mid-paragraph bold every few lines, or ✅🚀💡 leading each item in professional copy. Cut unless the channel truly calls for it (set per channel in config).

**Header inflation.** An H2 every ~60 words. Real writing carries readers across paragraphs without a signpost each time.

**Too-perfect parallel lists.** Every item identical length and grammar. Real lists are lumpier.

---

## 7. Substance / factual tells

**Vague quantifiers instead of numbers.** "significantly reduced," "many companies," "a growing number." Replace with a real figure + source, or cut.

**Unsourced confident claims.** Per config `citations: required|preferred`, every factual claim gets a source. No source → soften to opinion or cut. (AI frequently invents plausible stats — treat every number as a lie until verified.)

**Invented-feeling specificity.** Fake-precise brand names, made-up stats, plausible-but-unverifiable quotes. Prefer real, checkable texture.

**Content duplication.** Whole sentences/sections repeated verbatim — an unedited-AI artifact. Deduplicate.

---

## 8. Fiction mode — extra checks

Run everything above, plus:
- **One negative-parallelism per book, maximum.** Fiction earns fewer, not more.
- **Don't explain the metaphor after the scene made it.** If a beat lands, cut the sentence that tells the reader it landed (telling-after-showing).
- **Don't beat one metaphor to death** (dead-metaphor trope) — deploy once, trust the reader. Series-specific metaphor limits go in `slop.config.md`.
- **Real, checkable texture** over invented-feeling brand names.
- **Sentence case in narration** unless a proper noun.
- **Paste artifacts:** duplicated sentences ("Her face was troubled. Her face was troubled."), garbled/half-deleted sentences, stray markdown fences.
- Preserve the manuscript voice (config `voice:` or the project's voice skill).

---

## 9. What is NOT slop (don't over-correct)

- One well-placed em-dash, one triad, one rhetorical question, one metaphor per piece.
- Deliberate fragments used for rhythm.
- A real list of real steps; a genuine strong stance.
- Correct technical terms — don't "plain-language" a term of art into vagueness.
- The humanizer over-correction is its own tell: if de-slopping makes a sentence harder to say aloud ("paramountly significant"), you've gone too far. Revert.

The goal: prose that reads like one human wrote it on purpose — lived-in, not scrubbed flavorless.

---

## Sources
- Wikipedia: *Signs of AI writing* — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- tropes.fyi — AI Writing Pattern Directory — https://tropes.fyi/directory
- The Register, "Why AI writing is so generic / semantic ablation" — https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/
- Olivia Cal, "How to Spot AI Writing Tells + AI Words Blacklist 2026" — https://www.oliviacal.com/post/ai-writing-tells
