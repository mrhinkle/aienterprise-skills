# FAQ & troubleshooting

**Do I need an API key?**
Not for most of them. They are instructions Claude follows, and the web skills fetch public URLs with the host's own tools. The video bundle is the exception: its scripts call ElevenLabs Scribe and need `ELEVENLABS_API_KEY` in the environment. Pulling a recording or uploading to YouTube uses your own platform credentials. Never commit a key. Put names of env vars in config, not the values.

**A skill didn't trigger. How do I force it?**
Name it or use a phrase from its description — "run ai-slop-killer on this," "use aie-web-seo on thesite.com." If it's installed and still doesn't load, check that the whole skill folder (SKILL.md + reference/) was copied, not just the SKILL.md.

**Claude Code vs. Cowork — any difference?**
The skills work in both. Install is the same `/plugin` flow. Cowork surfaces skills in its UI; Claude Code loads them by description.

**Can I install one skill instead of a whole bundle?**
Yes — copy just that skill's folder into `.claude/skills/` (see [getting-started](getting-started.md)). The `/plugin` flow installs a bundle at a time; manual install is per-skill.

**Will the web skills change my site?**
The audit and review skills (seo, audit, performance, qa, security, links, ux) report findings and suggest fixes. They do not change the site unless you ask them to apply a fix. `aie-web-forms` writes form-handling code when you ask it to wire a form. `aie-web-testing` writes Playwright tests when you ask it to. `aie-web-performance` can hand you commands and patches; it should not edit the project until you say to apply them.

**Is aie-web-security safe / legal?**
It's a **defensive self-audit** for sites you own or are authorized to review. It has no attack tooling and only inspects public output and code you point it at. Don't run it against sites you don't control.

**The social posts cite sources — can I trust them?**
Every factual claim is mapped to a URL in the sources log the skill returns. Fabricated stats and quotes are banned. Verify the log; that's what it's for.

**How do I customize tone / banned words?**
Add a `slop.config.md` to your working directory (annotated example in `plugins/ai-slop-killer/skills/ai-slop-killer/reference/`). The writing and social skills honor it.

**How do I update after the repo changes?**
`/plugin marketplace update aienterprise-skills`, then reinstall any bundle you want to refresh.

**Something's wrong / I have an idea.**
Open an issue or PR. See [CONTRIBUTING](../CONTRIBUTING.md).
