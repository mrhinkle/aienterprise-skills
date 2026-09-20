---
name: aie-web-ux
description: Review a website or web app for usability and user-experience problems that hurt real visitors — confusing navigation, weak visual hierarchy, buttons that don't look clickable, forms with poor feedback, cluttered layouts, mobile/touch issues, low readability, and missing error handling. Evaluates against Nielsen's usability heuristics and WCAG-informed readability, then scores each area and lists prioritized, actionable fixes. Trigger on "review the UX," "UX review," "usability review," "is my site easy to use," "hard to navigate," "confusing layout," "improve the flow," "design review," "mobile experience," "users can't find," or "information architecture."
---

# Web UX Review

Evaluates whether a site works well *for humans*, not just whether it technically works. Catches the friction that automated tools miss: confusing navigation, buried content, unclear CTAs, and mobile pain. Produces a scored review with prioritized fixes.

## Workflow

1. **Confirm the target and audience** — the URL or pages to review, who the primary visitor is, and what they're trying to accomplish. UX is judged against a goal.
2. **Walk the key journeys** — at minimum: homepage first impression, the primary conversion path (contact/signup/purchase), and mobile. See `reference/journeys.md` for what to ask on each page type.
3. **Evaluate against the heuristics and checklists** — apply Nielsen's 10 usability heuristics plus the navigation, visual-hierarchy, mobile, and readability checklists in `reference/checklists.md`.
4. **Flag anti-patterns** — scan for the common UX traps in `reference/checklists.md` (mystery-meat navigation, walls of text, auto-playing media, hidden contact info, hover-only interactions, etc.).
5. **Score and prioritize** — fill the scorecard below, then rank fixes by impact. Navigation and mobile issues usually outrank cosmetic ones.

## Nielsen's 10 usability heuristics (what to check)

1. **Visibility of system status** — loading/feedback states, active-page highlighting, visible success/error messages.
2. **Match with the real world** — plain-language labels and CTAs, intuitive icons, no unexplained jargon.
3. **User control and freedom** — working back button, clear escape routes (logo/home), no dead ends, no forced signup to explore.
4. **Consistency and standards** — buttons look like buttons, links styled consistently, nav in the same place everywhere.
5. **Error prevention** — validate before submit, mark required fields, sensible defaults, confirm irreversible actions.
6. **Recognition over recall** — options visible or one click away, breadcrumbs, clear category labels over generic "More".
7. **Flexibility and efficiency** — skip-to-content link, multiple paths to content, bookmarkable URLs, filters over endless scroll.
8. **Aesthetic and minimalist design** — every element earns its place, generous whitespace, high signal-to-noise, no distracting motion.
9. **Recognize and recover from errors** — helpful 404s, field-level errors that say how to fix, friendly tone.
10. **Help and documentation** — FAQ/help near the point of confusion, contact reachable from every page.

Full source: Nielsen Norman Group — https://www.nngroup.com/articles/ten-usability-heuristics/

## Scorecard

Score each 0–100; overall is the average.

| Category | Score | Notes |
|----------|-------|-------|
| Navigation & structure | | Can visitors find things fast? |
| Visual hierarchy | | Is important content prominent? |
| Mobile experience | | Does it work on phones? |
| Readability | | Is text easy to read? |
| Forms & interaction | | Are CTAs clear and clickable? |
| Perceived performance | | Does it feel responsive? |
| Error handling | | Are problems communicated well? |
| Content quality | | Is information useful and complete? |
| Design consistency | | Does everything feel cohesive? |
| Accessibility & inclusivity | | Usable by everyone? |
| **Overall** | | Average |

Bands: 80–100 excellent · 60–79 good · 40–59 fair (fix friction) · below 40 needs redesign.

## Output Format

1. **Overall score and one-line verdict.**
2. **Top 3 friction points** — the highest-impact problems, stated as what the visitor experiences.
3. **Scorecard** table (above), filled in.
4. **Findings by area** — grouped by category, each with: what's wrong, why it hurts the visitor, and the concrete fix. Tag each **High / Medium / Low** priority.
5. **Prioritized fix list** — the order to tackle them (navigation and mobile first).

## Reference

- `reference/checklists.md` — navigation, visual-hierarchy, mobile, readability checklists and the anti-pattern list.
- `reference/journeys.md` — page-type-specific questions for homepage, about/services, contact, and blog/resources.

## Standards

- Nielsen's 10 usability heuristics — https://www.nngroup.com/articles/ten-usability-heuristics/
- WCAG 2.2 (contrast, targets, readability) — https://www.w3.org/WAI/WCAG22/quickref/

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
