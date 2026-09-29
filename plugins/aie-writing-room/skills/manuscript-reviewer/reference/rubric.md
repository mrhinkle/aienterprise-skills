# Manuscript Evaluation Rubric

A 0–100 scoring framework for chapters or a full manuscript, built for fiction where craft, meaning, and reader conversion all have to work. Use it on your own drafts, with beta readers, or with an editor.

**How to use:** score each dimension 0–100 using the bands below, multiply by its weight, and add. `scripts/score.py` does the math.

**Weighting principle:** no dimension should dominate, and no commercial-readiness dimension should become decorative. The defaults keep every weight between 10% and 14%.

---

## Customizing per book

The eight default dimensions fit most novels. To change them, set `rubric` in `writing-room.config.md` to a JSON file (see `rubric.example.json`) and run `score.py --rubric <path>`.

- **Reweight** for the genre. A business fable might weight Theme up; a thriller might weight Pacing and Hook up; literary fiction might weight Voice up.
- **Rename** to fit the book. For a mystery, "Story Engine" might become "Puzzle & Fair Play." For narrative nonfiction, "World & Authenticity" becomes "Accuracy & Sourcing" and "Dialogue" becomes "Scene & Quotation."
- **Replace or add** a dimension if the book has a job the defaults don't cover (e.g. "Humor," "Romance Arc," "Period Accuracy"). Write bands for it in the same shape as below.
- **Keep the auto-flags in sync.** If you rename or remove a dimension an auto-flag uses, update or drop that flag in your notes.
- Keep weights summing to 1.0 (the script normalizes and warns if not).

Record the book's rubric choices in the project, not in this file.

---

## Universal scoring bands (every dimension)

| Score | Band | Meaning |
|---|---|---|
| 90–100 | Exceptional | Best-in-class. Nothing to fix |
| 75–89 | Strong | Working well. Light polish at most |
| 60–74 | Solid | Functional but unremarkable |
| 40–59 | Weak | Real problems. Targeted revision needed |
| 20–39 | Failing | Doesn't do its job. Rewrite required |
| 0–19 | Broken | Absent, incoherent, or hurting the book |

---

## The eight default dimensions

### 1. Theme & Meaning (13%)
Does what the book is about land through scene and consequence rather than lecture? Would a reader leave seeing their world a little differently? (For business or idea-driven fiction, call this **Theme & Argument**.)
- **90–100** — The reader understands the book's central question more deeply because of how the story unfolds, not what characters say. Meaning is inseparable from plot
- **75–89** — Strong thematic spine; occasional drift into exposition but recovers
- **60–74** — Consistent but easy to miss; buried under plot mechanics
- **40–59** — Delivered through speeches, monologue, or thinly veiled author voice
- **20–39** — Contradicts what the story actually shows
- **0–19** — No discernible meaning, or pure sermon

### 2. Story Engine (14%)
Is there a question the reader needs answered? Are stakes clear, escalating, and personal to a character we care about?
- **90–100** — Page-turner; something specific is at risk
- **75–89** — Strong forward pull, clear stakes, occasional drift
- **60–74** — Works, but the reader could put it down without anxiety
- **40–59** — Reading because they should, not because they have to
- **20–39** — Stakes vague or impersonal; motion is mechanical, not emotional
- **0–19** — No question, stakes, or motion

### 3. Character (14%)
Are the people distinct, contradictory, and consequential? Do they want something specific and sweat for it? Can you tell them apart in dialogue without tags?
- **90–100** — People you'd recognize on the street; surprising but consistent
- **75–89** — Strong protagonist plus two or three vivid supporting characters
- **60–74** — Clear archetypes that serve the story
- **40–59** — Characters blur or exist only to deliver plot
- **20–39** — Mouthpieces for the author
- **0–19** — Names on a page

### 4. World & Authenticity (12%)
Do the places, institutions, and specialist details feel lived-in and right? Identify the book's two or three authenticity **lanes** (e.g. *the city; the profession; the technology*, or *the period; the court; the household*) and judge each.
- **90–100** — An insider from any lane would say "yes, this is right." Specific, sensory, accurate
- **75–89** — Vivid in most lanes; the rest competent
- **60–74** — Present but generic; could be anywhere
- **40–59** — Details borrowed from other novels or news clips
- **20–39** — Wrong in ways an insider would catch
- **0–19** — Backdrops with no texture

### 5. Voice & Prose (12%)
Sentence-level craft. Clean, distinctive, alive? Does the narrative voice have a point of view, or does it sound machine-generated?
- **90–100** — Distinctive; sentences worth underlining; only this author could have written it
- **75–89** — Confident, clean, rhythmic, with standout passages
- **60–74** — Workmanlike; doesn't get in the way
- **40–59** — Flat, generic, or overwritten; adverbs doing verbs' work
- **20–39** — First-draft prose; tense and POV slips
- **0–19** — Unreadable

### 6. Dialogue (11%)
Does dialogue advance plot AND reveal character? Do people sound different? Is there subtext?
- **90–100** — Quotable; subtext, rhythm, distinct voices
- **75–89** — Strong, with occasional info-dumps
- **60–74** — Functional; moves the scene
- **40–59** — Characters explain the plot to each other
- **20–39** — On-the-nose, expository, interchangeable
- **0–19** — Speakers can't be told apart

### 7. Pacing & Structure (14%)
Does each chapter end with a reason to turn the page? Do slow scenes earn their keep? Is the structure intentional?
- **90–100** — Architectural; every chapter does specific work; end hooks land
- **75–89** — Strong, with one or two soft spots
- **60–74** — Decent rhythm; some chapters feel like padding
- **40–59** — Flat momentum; scenes don't earn their length
- **20–39** — Reader gets lost or bored
- **0–19** — Structureless

### 8. Hook & Reader Conversion (10%)
Can the book be pitched in one sentence that makes someone want it? Do the first pages convert browsers into readers? Clear comparable titles, a clear shelf, and a reason to recommend it?
- **90–100** — Killer logline, obvious comps, clear shelf, strong first-30-page pull, a word-of-mouth sentence readers repeat
- **75–89** — Strong concept and promise; comps or opening need light sharpening
- **60–74** — Works once explained; doesn't yet sell itself
- **40–59** — Hard to pitch, or the opening doesn't deliver the promise fast enough
- **20–39** — No clear category, comps, reader, or recommendation path
- **0–19** — Unsellable as is

---

## Scoring math (default weights)

Final = Theme×0.13 + Story×0.14 + Character×0.14 + World×0.12 + Voice×0.12 + Dialogue×0.11 + Pacing×0.14 + Hook×0.10

## Decision thresholds

**Chapter level (during revision)**
- **85–100** — Lock it. Move on
- **70–84** — One more pass on the lowest dimensions
- **55–69** — Structural problem. Diagnose before line-editing
- **Below 55** — Cut, rewrite, or move it

**Manuscript level (before submission or publication)**
- **85–100** — Submit or publish with confidence
- **75–84** — One more developmental pass with a trusted editor
- **60–74** — Major revision; likely structure or character
- **Below 60** — Back to the outline

## Auto-flags (any one = stop and address, regardless of total)

1. Theme 85+ but Story Engine below 60 — an essay, not a novel
2. Voice 85+ but Character below 60 — pretty sentences, no people
3. Any chapter with Pacing below 40 — readers quit here
4. A character scoring 85+ early (first ~15% of the book) who vanishes by the midpoint — an abandoned asset
5. Manuscript-level Hook & Reader Conversion below 70 — not submit-ready, whatever the total
6. First-30-pages average across Story Engine, Pacing, and Hook below 75 — fix the opening first

---

## Per-chapter quick score

```
Chapter: ____________   Reviewer: ____________   Date: ____________

Dimension              Score   Weight   Weighted
Theme & Meaning        _____   × 0.13 = ______
Story Engine           _____   × 0.14 = ______
Character              _____   × 0.14 = ______
World & Authenticity   _____   × 0.12 = ______
Voice & Prose          _____   × 0.12 = ______
Dialogue               _____   × 0.11 = ______
Pacing & Structure     _____   × 0.14 = ______
Hook & Reader Conv.    _____   × 0.10 = ______

FINAL SCORE: _____ / 100

What worked:
What didn't:
What to fix next pass:
```
