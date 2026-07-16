# AIEnterprise Skills

Open source [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) from [The AIE Network](https://theaie.net) — practical, source-backed tools for people doing real work with Claude.

Skills are folders of instructions and reference material that Claude loads on demand, only when they're relevant. These are the ones we use ourselves, cleaned up and depersonalized so anyone can run them. They work in **Claude Code** and in **Cowork**.

**15 skills across 6 bundles:** writing, web, social, chief-of-staff, Hermes operations, and skill-creator.

---

## Bundles & skills

### ✍️ ai-slop-killer &nbsp;·&nbsp; [plugin](plugins/ai-slop-killer)

| Skill | What it does |
| --- | --- |
| **[ai-slop-killer](plugins/ai-slop-killer/skills/ai-slop-killer)** | The final editing pass for any prose. Detects documented AI writing tells (from Wikipedia's *Signs of AI writing*, tropes.fyi, and working editors' guides), scores how bad it was, rewrites in place, and shows its work. Configurable to your house style via `slop.config.md`. |

### 🌐 aie-web &nbsp;·&nbsp; [plugin](plugins/aie-web) &nbsp;·&nbsp; stack-agnostic

| Skill | What it does |
| --- | --- |
| **[aie-web-seo](plugins/aie-web/skills/aie-web-seo)** | Audit a site for search-engine **and** answer-engine optimization (ChatGPT, Perplexity, AI Overviews). Meta, schema/JSON-LD, Core Web Vitals, content gaps. Scored report + fix list. |
| **[aie-web-audit](plugins/aie-web/skills/aie-web-audit)** | Broad four-part health audit of any live site from just its URL — no code access needed. Hands off to the specialist skills below. |
| **[aie-web-performance](plugins/aie-web/skills/aie-web-performance)** | Audit and fix page load performance (LCP, INP, CLS), with concrete optimizations. |
| **[aie-web-qa](plugins/aie-web/skills/aie-web-qa)** | The pre-launch / post-update "does this actually work?" gate. |
| **[aie-web-security](plugins/aie-web/skills/aie-web-security)** | Read-only **defensive** self-audit: exposed secrets, dependency risks, security headers, HTTPS, XSS sinks, CORS/CSRF, privacy. No attack tooling. |
| **[aie-web-links](plugins/aie-web/skills/aie-web-links)** | Crawl and validate every link, image, and asset — broken links, mixed content, redirect chains, orphaned pages, dead anchors. |
| **[aie-web-forms](plugins/aie-web/skills/aie-web-forms)** | Wire forms to any provider with validation, spam protection, accessible labels, and success/error states. |
| **[aie-web-ux](plugins/aie-web/skills/aie-web-ux)** | Usability review against Nielsen's heuristics + readability. Scorecard and prioritized fixes. |
| **[aie-web-testing](plugins/aie-web/skills/aie-web-testing)** | Write and run automated Playwright browser tests for critical journeys (sign-up, login, forms), catch console/network errors, and report failures with screenshots. Wires into CI. |

### 📣 aie-social &nbsp;·&nbsp; [plugin](plugins/aie-social) &nbsp;·&nbsp; research-driven

| Skill | What it does |
| --- | --- |
| **[aie-social-linkedin](plugins/aie-social/skills/aie-social-linkedin)** | Turn any topic into a high-quality LinkedIn post. Real research phase with cited sources, proven hooks, 2026 algorithm-aware formatting, quality rubric, and a final ai-slop-killer pass. Outputs the post + alternative hooks. |
| **[aie-social-x](plugins/aie-social/skills/aie-social-x)** | The same research-then-draft-then-review flow, tuned to X — single post vs. thread, hooks, character limits. |

### 🧭 aie-chief-of-staff &nbsp;·&nbsp; [plugin](plugins/aie-chief-of-staff) &nbsp;·&nbsp; read-only & safe

| Skill | What it does |
| --- | --- |
| **[aie-chief-of-staff](plugins/aie-chief-of-staff/skills/aie-chief-of-staff)** | A morning brief that pulls together your calendar, your inbox (read-only triage), and a scan of your industry news + tracked competitors — with your top 3 for the day, prep flags, and a focus block. Configurable per person and industry via `cos.config.md`. Drafts and recommends; never sends or deletes. |

### 🛡️ aie-hermes &nbsp;·&nbsp; [plugin](plugins/aie-hermes) &nbsp;·&nbsp; safe operations

| Skill | What it does |
| --- | --- |
| **[aie-hermes-ha](plugins/aie-hermes/skills/aie-hermes-ha)** | Creates and operates safe recurring monitoring for a remote Hermes host: machine health, Tailscale, Telegram, Slack, security posture, and update readiness. Performs only bounded self-healing and protects remote access with explicit approval gates. |

### 🛠 aie-skill-creator &nbsp;·&nbsp; [plugin](plugins/aie-skill-creator) &nbsp;·&nbsp; meta

| Skill | What it does |
| --- | --- |
| **[aie-skill-creator](plugins/aie-skill-creator/skills/aie-skill-creator)** | Build a new, high-quality skill from scratch — right frontmatter, tight SKILL.md, progressive-disclosure reference files, a self-test, and packaging as a `.skill` or plugin. Also audits and improves existing skills and fixes descriptions that don't trigger. The tool for growing this marketplace. |

---

## Install

### As a plugin marketplace (recommended)

In Claude Code or Cowork:

```
/plugin marketplace add mrhinkle/aienterprise-skills
/plugin install ai-slop-killer@aienterprise-skills
/plugin install aie-web@aienterprise-skills
/plugin install aie-social@aienterprise-skills
/plugin install aie-chief-of-staff@aienterprise-skills
/plugin install aie-hermes@aienterprise-skills
/plugin install aie-skill-creator@aienterprise-skills
```

Install only the bundles you want. Skills trigger automatically when relevant, or on cue ("de-slop this," "audit my SEO," "write a LinkedIn post about X").

### Manually

Copy any skill folder (e.g. `plugins/aie-web/skills/aie-web-seo/`) into your project's `.claude/skills/` directory, or your personal skills folder.

---

## How these fit together

The skills are designed to hand off to each other:

- **aie-web-audit** runs a broad scan, then points you to **aie-web-seo**, **-performance**, **-security**, or **-qa** for depth.
- **aie-social-linkedin** and **aie-social-x** both run **ai-slop-killer** as their mandatory final pass, so posts ship clean.
- **ai-slop-killer** is the last pass for anything you publish — it's useful on its own, and the writing engine behind the social skills.

Full usage docs: **[docs/](docs/)**.

---

## Configure to your voice

Skills that support it read an optional config from your working directory — add your own banned words, allow words you legitimately use, name a voice to preserve, and set citation strictness. See `ai-slop-killer`'s `reference/slop.config.example.md`. With no config, sensible defaults apply.

## Contributing

Issues and pull requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill format and the quality bar.

## License

[MIT](LICENSE). Use them, fork them, ship them.

---

Built by [Mark R. Hinkle](https://github.com/mrhinkle) and The AIE Network. If these save you time, [subscribe to the newsletters](https://theaie.net).
