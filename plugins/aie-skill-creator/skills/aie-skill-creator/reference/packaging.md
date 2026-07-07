# Packaging & shipping a skill

Three ways to ship, smallest to largest.

## 1. Plain folder (project or personal)

The skill is just its folder. Drop it in:

```
# project-scoped (this repo only)
your-project/.claude/skills/skill-name/

# personal (all your projects)
~/.claude/skills/skill-name/
```

Copy the whole folder — `SKILL.md` plus `reference/` and `scripts/`.

## 2. `.skill` zip (one-click install / sharing)

Zip the skill folder with a `.skill` extension so it installs in one click:

```bash
cd path/to/skill-name/..
zip -r skill-name.skill skill-name
```

The archive must contain the `SKILL.md` at (or one level under) its root. In Cowork, a `.skill` file renders with a **Save skill** button.

## 3. Plugin + marketplace (installable by others)

To make it installable with `/plugin install`, wrap it in a plugin and list it in a marketplace repo.

**Plugin** — add `plugin-name/.claude-plugin/plugin.json`:

```json
{
  "name": "plugin-name",
  "version": "1.0.0",
  "description": "What this plugin's skills do.",
  "author": { "name": "You", "url": "https://you.example" },
  "license": "MIT"
}
```

Skills live under `plugin-name/skills/<skill-name>/`. A plugin can hold several related skills.

**Marketplace** — at the repo root, `.claude-plugin/marketplace.json`:

```json
{
  "name": "my-marketplace",
  "owner": { "name": "You", "url": "https://you.example" },
  "metadata": { "description": "My skills.", "version": "1.0.0" },
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugins/plugin-name",
      "description": "...",
      "version": "1.0.0",
      "keywords": ["..."],
      "category": "..."
    }
  ]
}
```

Push the repo to GitHub, then anyone installs it:

```
/plugin marketplace add <owner>/<repo>
/plugin install plugin-name@my-marketplace
```

Validate the JSON before shipping (`python3 -c "import json;json.load(open('.claude-plugin/marketplace.json'))"`), and confirm every `source` path exists and every skill folder has a `SKILL.md` whose `name` matches its folder.

## Ship checklist

- [ ] `SKILL.md` starts with `---` and has `name` + `description`; `name` matches the folder.
- [ ] Description is concrete and ends with trigger phrases.
- [ ] Heavy content is in `reference/`, pointed to from SKILL.md.
- [ ] No secrets or private data committed.
- [ ] JSON manifests validate; `source` paths resolve.
- [ ] README/usage: the install command and one example.
