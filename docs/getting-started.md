# Getting started

## What is a skill?

A skill is a folder with a `SKILL.md` file (and optional `reference/` material). The `SKILL.md` frontmatter has a `name` and a `description`; Claude reads that description and loads the skill only when it's relevant to what you're doing. You don't call skills like commands — you just work, and the right one activates. You can also trigger one explicitly by naming it or using a phrase from its description ("de-slop this," "audit my SEO").

These skills run in **Claude Code** (the CLI) and in **Cowork** (the desktop app). No API keys are required by the skills themselves — a few of the web skills fetch public URLs, which the host already supports.

## Install

### Option A — plugin marketplace (recommended)

```
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install ai-slop-killer@aienterprise-skills
/plugin install aie-web@aienterprise-skills
/plugin install aie-social@aienterprise-skills
/plugin install baad-ai-work-setup@aienterprise-skills
```

Install only the bundles you want. Update later with `/plugin marketplace update aienterprise-skills`.

### Option B — manual

Copy any skill folder into your skills directory:

```
# project-scoped
cp -r plugins/aie-web/skills/aie-web-seo  your-project/.claude/skills/

# personal (all projects)
cp -r plugins/aie-web/skills/aie-web-seo  ~/.claude/skills/
```

A skill needs its whole folder — the `SKILL.md` and its `reference/` files.

## Trigger a skill

Just describe the work. Examples:

| You say | Skill that activates |
| --- | --- |
| "Does this paragraph sound like AI? Clean it up." | ai-slop-killer |
| "Audit thesite.com for SEO and answer engines." | aie-web-seo |
| "Check this site for broken links." | aie-web-links |
| "Is my site secure? Do a review." | aie-web-security |
| "Write a LinkedIn post about our launch, with research." | aie-social-linkedin |
| "Turn this into an X thread." | aie-social-x |
| "Set up Claude Cowork for my most important task." | baad-setup-claude-cowork |
| "Help me configure ChatGPT Work." | baad-setup-chatgpt-work |
| "Build my first Manus Project workflow." | baad-setup-manus |
| "Turn this class workflow into BAAD skills and open a draft PR." | baad-publish-class-skills |

## Configure (optional)

Some skills read a small config file from your working directory so they match your house style:

- **`slop.config.md`** (ai-slop-killer, and the social skills' final pass) — your extra banned words, words you legitimately use, a voice to preserve, and citation strictness. Copy the example from `plugins/ai-slop-killer/skills/ai-slop-killer/reference/slop.config.example.md`.

With no config, every skill applies sensible defaults.

## The order that works

1. Do the work (write the post, build the page).
2. Run the specialist skill (SEO audit, security review, LinkedIn draft).
3. For anything you publish as prose, **ai-slop-killer runs last** — the social skills do this automatically.

See each bundle's page for details: [writing](writing.md) · [web](web.md) · [social](social.md).
