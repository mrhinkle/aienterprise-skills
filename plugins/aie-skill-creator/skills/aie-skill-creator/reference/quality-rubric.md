# Skill quality rubric

Score a skill before shipping or when auditing. Each item is 0–2 (0 = missing, 1 = partial, 2 = solid). A skill should score 16+/20 before it ships; anything scored 0 is a blocker.

| # | Criterion | What "solid" looks like |
| --- | --- | --- |
| 1 | **Triggerability** | Description is concrete, keyword-rich, and ends with trigger phrases a real person would type. |
| 2 | **Distinct scope** | One clear job; its trigger space doesn't collide with another skill. |
| 3 | **Tight SKILL.md** | Under ~500 lines; depth pushed to `reference/`; skimmable steps, not prose walls. |
| 4 | **Progressive disclosure** | Reference files exist for the heavy content and the SKILL.md points to each by name. |
| 5 | **Clear procedure** | A named loop or numbered steps that a stranger could follow cold. |
| 6 | **Defined I/O** | States what it takes in and the exact shape it returns (an output template helps). |
| 7 | **Safety** | Names what it won't do without approval; treats file/tool/message content as data, not commands; no irreversible actions ungated. |
| 8 | **No baked-in privates** | No secrets, tokens, or one person's private rules hardcoded; house rules live in a config. |
| 9 | **Self-tested** | Evidence it was run cold on a realistic input and produced the promised result. |
| 10 | **Packaged** | Valid frontmatter; installs cleanly as a folder / `.skill` / plugin; install command + one example given. |

## Fast audit (the usual failures)

- **"It never triggers."** → the description is vague or generic. Rewrite it concrete + keyword-rich + trigger phrases. (Fixes ~80% of trigger complaints.)
- **"It loads but wanders."** → the SKILL.md has no clear procedure, or it inlined a giant checklist. Add a numbered loop; move the checklist to `reference/`.
- **"It fires on the wrong tasks."** → trigger space overlaps another skill. Narrow the description; name what it is NOT for.
- **"It did something risky."** → missing safety gate. Add explicit approval requirements and the data-not-commands rule.

## Report format (audit mode)

```
Skill: {name}   Score: {n}/20

Fix now:
- {criterion} — {problem} → {change}
...

Nice to have:
- ...
```
