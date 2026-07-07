# Skill Creator bundle (aie-skill-creator)

## aie-skill-creator

The meta-skill: build a new, high-quality Claude Agent Skill from scratch — or audit and improve one you already have. It's the tool for growing this marketplace, and it encodes the same standards every skill here was built to.

### What it does

Runs a five-step loop: **Scope → Draft → Reference → Test → Package.**

1. **Scope** — pins the job to one sentence, lists the trigger phrases, defines inputs/outputs, and flags anything that needs a safety gate. If it's really three jobs, it says so.
2. **Draft** — writes two-key frontmatter (the description is what makes a skill trigger, so it's concrete and keyword-rich, ending in trigger phrases) and a tight, skimmable SKILL.md with a numbered procedure.
3. **Reference** — moves long checklists, rubrics, templates, and examples into `reference/` files, keeping the SKILL.md small (progressive disclosure).
4. **Test** — a trigger test (does the description fire for the right asks and not the wrong ones?) and a cold-run test (follow the SKILL.md on a real input and check the output).
5. **Package** — as a plain folder, a `.skill` zip for one-click install, or a plugin + marketplace entry with the install command.

### Audit / improve mode

Point it at an existing skill and it scores it against a 10-point rubric, then fixes the usual failures: a vague description that never triggers, a bloated SKILL.md that should push content to references, unclear scope, or a missing safety gate.

### Why it's useful

If you're building a skills library, this is the highest-leverage tool in it — it turns "I keep typing the same instructions" into a clean, installable, reusable skill, and keeps quality consistent across a growing set.

### Triggers

"create a skill," "make a skill," "build a skill for X," "turn this workflow into a skill," "write a SKILL.md," "improve this skill," "audit my skill," "why doesn't my skill trigger," "package this skill."

### Reference files

- `skill-anatomy.md` — structure, frontmatter, progressive disclosure, and how to write a description that triggers (with good/bad examples).
- `quality-rubric.md` — the 10-point scorecard used to finish or audit a skill.
- `packaging.md` — folder, `.skill` zip, and plugin/marketplace packaging with commands.
