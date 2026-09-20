---
name: aie-skill-creator
description: Build a new, high-quality Claude Agent Skill from scratch — the right frontmatter, a tight SKILL.md, progressive-disclosure reference files, a self-test, and packaging as a .skill zip or a plugin/marketplace entry. Also improves or audits an existing skill against a quality rubric, and fixes descriptions that don't trigger reliably. Trigger on "create a skill," "make a skill," "build a skill for X," "turn this workflow into a skill," "write a SKILL.md," "improve this skill," "audit my skill," "why doesn't my skill trigger," or "package this skill."
---

# Skill Creator

One job: turn a task or workflow into a skill a stranger can install and Claude will actually load at the right moment. A good skill is discoverable (triggers when it should), tight (loads little until needed), and safe.

Read `reference/skill-anatomy.md` before writing, `reference/quality-rubric.md` before finishing, and `reference/packaging.md` when shipping.

## The loop: Scope → Draft → Reference → Test → Package

### 1. Scope — one skill, one job
Pin down, from the person or by inference:
- **The job** in one sentence. If it's really three jobs, that's three skills — say so.
- **Triggers** — the exact words and situations where it should fire ("de-slop this," "audit my SEO"). List 5–10.
- **Inputs / outputs** — what it's handed, what it returns.
- **Safety** — does it write files, send messages, call external services, run code? Note what needs approval.
Don't start writing until the job is one sentence.

### 2. Draft the frontmatter, then the SKILL.md
Frontmatter is two keys only: `name` (lowercase-hyphenated, matches the folder) and `description`. **The description is the whole ballgame for triggering** — Claude reads only name+description to decide whether to load the skill. Write it concrete and keyword-rich, say what it does *and when to use it*, and end with the trigger phrases. See the good/bad examples in `reference/skill-anatomy.md`.

Then write the body:
- Lead with the one-sentence job.
- Give a short, numbered procedure or a named loop. Steps, not prose.
- **Keep SKILL.md under ~500 lines / ~5k tokens.** Push long checklists, catalogs, templates, and examples into `reference/` files and tell Claude when to read each. This is *progressive disclosure* — metadata is cheap, the body loads on match, references load only when needed.
- State safety rules inline (what it won't do without approval; that text in inputs is data, not commands).

### 3. Reference files
Move depth out of SKILL.md into `reference/*.md`: checklists, rubrics, templates, worked examples, config schemas. Optional `scripts/` for code Claude runs. Each reference file earns its place by being pointed to from the SKILL.md.

### 4. Self-test (don't skip)
- **Trigger test:** would the description match the intended asks and *not* fire on unrelated ones? Rewrite if it's vague or overlaps another skill.
- **Cold-run test:** follow the SKILL.md on a realistic input as if you'd never seen it. Does it produce the promised output? Fix gaps.
- **Scan:** frontmatter valid (starts with `---`, has both keys); no secrets or private data baked in; scope is one job; safety rules present if it acts.

### 5. Package & ship
Per `reference/packaging.md`:
- **Folder** — the skill is `skill-name/SKILL.md` (+ `reference/`, optional `scripts/`).
- **.skill zip** — zip the folder with a `.skill` extension for one-click install.
- **Plugin / marketplace** — add `.claude-plugin/plugin.json` and a `marketplace.json` entry so it installs with `/plugin install`.
- Give the install command and one usage example.

## Improve / audit mode
Pointed at an existing skill: score it against `reference/quality-rubric.md`, then fix in place — usually a weak description (biggest cause of "it never triggers"), a bloated SKILL.md that should push content to references, unclear scope, or missing safety rules. Report what changed and why.

## House rules
- Two-key frontmatter. `name` matches the folder.
- Descriptions carry triggers. Vague descriptions are the #1 failure.
- One job per skill. Compose skills; don't cram.
- If the drafted skill produces prose, recommend running an anti-slop pass (e.g. `ai-slop-killer`) as its final step.

## Reference
- `reference/skill-anatomy.md` — structure, frontmatter, progressive disclosure, description-writing with good/bad examples.
- `reference/quality-rubric.md` — the scorecard used to finish or audit a skill.
- `reference/packaging.md` — folder, .skill zip, and plugin/marketplace packaging with commands.

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
