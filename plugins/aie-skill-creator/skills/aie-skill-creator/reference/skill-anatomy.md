# Skill anatomy

## Folder structure

```
skill-name/
├── SKILL.md            # required — frontmatter + instructions
├── reference/          # optional — checklists, rubrics, templates, examples
│   └── *.md
└── scripts/            # optional — code Claude runs (python/node/etc.)
    └── *.py
```

The folder name, the frontmatter `name`, and how you refer to the skill should all match.

## Frontmatter — two keys

```yaml
---
name: skill-name
description: What it does + when to use it, ending with trigger phrases.
---
```

Only `name` and `description` are required by the spec. `name` is lowercase, hyphenated, and matches the folder. Everything else lives in the body.

## Progressive disclosure (why SKILL.md stays small)

Claude loads a skill in three stages:

1. **Metadata (~100 tokens):** every skill's `name` + `description` is always in context so Claude can match. Cheap.
2. **Body (<~5k tokens):** the SKILL.md loads only when the skill matches the task.
3. **Resources (as needed):** `reference/` files and `scripts/` load only when the SKILL.md tells Claude to open them.

So: keep SKILL.md short and skimmable — the job, a numbered procedure, safety rules, and pointers. Put catalogs, long checklists, templates, and examples in `reference/`. A 2,000-line SKILL.md defeats the design.

## Writing the description (this is what makes it trigger)

Claude decides whether to load a skill from the description alone. Make it:

- **Concrete** — name the actual task and artifacts, not a vibe.
- **Situated** — say *when* to use it.
- **Keyword-rich** — include the words a person would actually type.
- **Trigger-terminated** — end with: `Trigger on "...", "...", "...".`
- **Distinct** — if two skills have overlapping descriptions, Claude picks wrong. Differentiate.

**Weak (won't trigger reliably):**
> `description: Helps with your writing.`

**Strong:**
> `description: The final anti-AI-slop editing pass for any prose — detects AI writing tells, scores the passage, rewrites in place, and reports what it changed. Trigger on "clean this," "de-slop," "does this sound like AI," "make this human."`

**Weak:**
> `description: A tool for websites.`

**Strong:**
> `description: Audits any website for SEO and answer-engine optimization — meta tags, schema/JSON-LD, Core Web Vitals, content gaps. Produces a scored report with fixes. Trigger on "check SEO," "SEO audit," "will AI cite my site," "schema markup."`

## Body shape that works

1. **One-sentence job** up top.
2. **A named loop or numbered steps** — imperative, skimmable. Steps beat paragraphs.
3. **Safety rules inline** — what it won't do without approval; treat tool/file/message content as data, not commands.
4. **Pointers** — "read `reference/x.md` before doing Y."
5. **Output format** — show the exact shape you want returned.

## Anti-patterns to avoid

- A vague description (the top reason skills never fire).
- A SKILL.md that inlines a 1,500-line checklist instead of referencing it.
- Three jobs in one skill. Split them.
- Baked-in secrets, tokens, or one person's private data — make house rules a config file.
- Instructions that tell Claude to take irreversible actions (send, delete, deploy) without an approval gate.
- Skills that duplicate an existing one's trigger space.
