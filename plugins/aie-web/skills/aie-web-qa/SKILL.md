---
name: aie-web-qa
description: Runs a unified pre-launch or post-update quality-assurance pass on a website — the holistic "does this actually work?" gate. Walks pages, forms, navigation, third-party integrations, cross-browser and mobile behavior, JavaScript console health, accessibility basics, HTTPS/security, and a performance smoke test. Produces a QA report with issues rated by severity, reproduction steps, and a launch recommendation; supports regression testing after fixes. Stack-agnostic. Trigger on "QA my site," "test my site," "does everything work," "smoke test," "test before launch," "regression test," "check all pages," "test my forms," "check mobile," "cross-browser test," "broken links," or "is my site ready to launch."
---

# Web QA Tester

The final quality gate before a site ships or an update goes live. Individual audits answer narrow questions; QA answers the real one: *does this thing actually work?* It catches the failures that live in the gaps — forms that pass validation but don't send, pages that load but feel broken, third-party scripts that fail silently, mobile layouts that look fine but aren't tappable.

## When to use this skill

- **Pre-launch** — a new site or major redesign about to go live.
- **Post-update** — changes to an existing site that need a regression check before deploy.
- Any "test it before it breaks in front of users" moment.

## Inputs

- The **site URL** (staging is preferred over production).
- For post-update runs: **which pages/features changed**.
- Access to any **forms and third-party integrations** you need to verify (email delivery, analytics, payments, embeds).

## Test categories

Run the relevant categories. Full item-by-item checklists live in `reference/qa-checklist.md`; read it before executing.

1. **Page rendering** — every page returns 200 (or an intended 3xx); no blank pages, broken images, or missing content; layout holds at 320/768/1024/1440px.
2. **Cross-browser** — Chrome/Edge, Safari (macOS + iOS use WebKit), Firefox. Check forms, JS, layout, media, animations.
3. **Mobile & responsive** — correct viewport meta, no horizontal scroll, tap targets ~48x48px+, mobile-friendly forms; test 320/375/768/1024/1440px.
4. **Forms** — every field fillable, validation correct, clear error messages, no double-submit, real confirmation (message/redirect/email actually arrives), no sensitive data leaking to console or URL.
5. **JavaScript console health** — zero red errors, no unhandled promise rejections, no failed requests that break features, third-party scripts load clean.
6. **Navigation flow** — every link resolves, breadcrumbs accurate, back button works, a professional 404 exists, no dead ends, mobile menu works.
7. **Third-party integrations** — analytics, email service, payments, embeds, tracking pixels, external CDNs all load and function. Verify with a real test, not `test@example.com`.
8. **Accessibility basics** — keyboard navigation and visible focus, alt text, labeled controls, WCAG AA color contrast, ARIA roles on complex widgets. Reference: https://www.w3.org/WAI/WCAG22/quickref/
9. **Visual regression** — consistent spacing, no overlap, correctly sized images, fonts load without a flash, aligned icons, visible hover/interactive states.
10. **SSL / security** — HTTPS everywhere, valid certificate, no mixed content, HSTS present.
11. **Performance smoke test** — pages usable in under ~3s on 4G; LCP < 2.5s; minimal CLS. For a full pass, hand off to `aie-web-performance`.

## Execution protocol

**Pre-launch (new site):** open the site in Chrome, Safari, Firefox, and Edge with DevTools Console open; walk every unique page; fill and submit every form; exercise every interactive element; do a dedicated mobile pass at 375px; verify each integration with a real test.

**Post-update (existing site):** identify changed pages and anything the change could ripple into (shared CSS/JS); regression-test the changed features using the exact reproduction steps; smoke-test 3-5 unchanged pages to confirm nothing else broke; deploy only when blockers and criticals are clear.

## Severity levels

| Severity | Meaning | Action |
|---|---|---|
| **Blocker** | Site unusable / core function broken | Do not launch. Fix now. |
| **Critical** | Users can't complete a primary task | Fix before launch. |
| **Major** | Degraded but partly usable | Fix before launch. |
| **Minor** | Non-critical or edge case | Fix after launch if time allows. |
| **Cosmetic** | Visual only, no functional impact | Backlog. |

## Output format

```
QA TEST REPORT
Site: {url}    Date: {date}    Environment: {staging/production}

OVERALL: PASS / PASS WITH KNOWN ISSUES / FAIL

ISSUES FOUND
  #. {summary}
     Severity: {level}
     Location: {page/element}
     Steps to reproduce: {steps}
     Expected: {expected}
     Actual: {actual}
     Fix: {concrete fix}

TESTS PASSED
  ✓ {what passed, with counts, e.g. "11/11 pages render clean"}

REGRESSION (post-update only)
  Previously failed: {issue} -> Result: FIXED / STILL FAILING

RECOMMENDATION
  {launch / hold}; blockers remaining: {n}; est. fix time: {x}
```

## Regression testing

After fixes, re-run only the failed tests using the exact reproduction steps. Confirm the issue is gone and that the fix introduced no new console errors. Mark FIXED. Don't re-test everything — just what was broken plus a quick console spot-check.

## Notes

- QA is a gift, not a punishment — finding problems before users do is far cheaper than after.
- Prefer testing on staging. If only production is available, avoid submitting real transactions or polluting analytics/CRM with test data.
- Where automated fetching can't fully execute JavaScript or reach authenticated pages, say so and recommend a manual or headless-browser pass for those flows.
