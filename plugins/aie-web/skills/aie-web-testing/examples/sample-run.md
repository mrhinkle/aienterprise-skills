# Sample run — aie-web-testing

Condensed run: Playwright scaffolded into the demo project and pointed at its staging URL (`staging.brightpath.example`, fictionalized). Report shape matches `reference/reporting.md`.

## What was written

Five journeys, from `reference/patterns.md` templates: homepage smoke, primary nav, contact form submit, newsletter signup, and the services→contact "money path." Config: desktop-chromium + mobile-safari projects, trace on first retry, `BASE_URL` from env.

## Run report

```
E2E TEST RUN — staging.brightpath.example
2026-07-14 · desktop-chromium, mobile-safari

RESULT: 8/10 passed   (1 failed, 1 flaky)

FAILURES
  ✗ contact form submits  [mobile-safari]
     Assertion: expected getByText(/thank you|received/i) to be visible
     Console/network errors: POST /api/contact → 422 (missing "message" field)
     Repro: fill form on mobile viewport → textarea below the fold is clipped
       by the sticky footer → Playwright fills it, but the submit fires before
       the field's blur handler writes to state
     Artifact: test-results/contact-mobile/trace.zip + screenshot
     Likely cause: real bug — state update race on mobile layout
     Fix: read field values from the form at submit time, not from blur-synced
       state; then re-run

FLAKY (passed on retry)
  ~ primary nav works [desktop-chromium] — "Services" matched two links (header
    + footer) → strict-mode violation on first run
    → stabilization: scope to header: page.getByRole('navigation').getByRole('link', ...)

RECOMMENDATIONS
  1. Fix the mobile submit race (it's a user-facing bug, not a test problem)
  2. Land the nav selector fix — committed in this run
  3. Wire the suite into CI (workflow from reference/setup.md) so it runs per push

Coverage: home, nav, contact form, newsletter, services→contact
Gaps: search (none on site), 404 behavior not yet asserted
```

Behavior this sample demonstrates: the failing test stayed in the suite (never deleted to go green), the flake was fixed with a better selector rather than a retry bump, and the failure ships with a trace, repro steps, and a real-bug-vs-flaky call.
