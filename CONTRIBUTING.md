# Contributing

Thanks for wanting to add to this. The bar is simple: a skill has to do one job well and be usable by a stranger.

## Skill format

Each skill is a folder with a `SKILL.md` at its root:

```
skills/<skill-name>/
├── SKILL.md            # required — frontmatter + instructions
└── reference/          # optional — catalogs, examples, configs Claude loads on demand
```

`SKILL.md` frontmatter needs a `name` and a `description`. The description is what Claude uses to decide when to trigger the skill, so make it concrete: say what it does and list the trigger phrases.

```markdown
---
name: my-skill
description: What it does, in one or two sentences, plus when to use it. Trigger on "phrase," "phrase," "phrase."
---

# My Skill

Instructions here. Keep the SKILL.md short; push detail into reference/ files.
```

## To add a skill to the marketplace

1. Put the skill under `plugins/<plugin-name>/skills/<skill-name>/`.
2. Add `plugins/<plugin-name>/.claude-plugin/plugin.json`.
3. Add an entry to `.claude-plugin/marketplace.json`.

## Quality bar

- **Depersonalized.** No private names, tokens, or company-only rules baked in. Make house rules configurable instead.
- **Sourced.** If a skill makes factual or research claims, cite them.
- **Tested.** Show that it works — a before/after, a sample run, something.
- **Tight.** One job. If it's doing three things, it's three skills.

## License

By contributing you agree your work ships under the repo's [MIT license](LICENSE).
