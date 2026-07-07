---
name: aie-web-testing
description: Write and run automated browser tests for a web app using Playwright — smoke tests, critical user journeys (sign-up, login, contact/checkout forms), navigation, and console/network-error checks — then report pass/fail with screenshots and repro steps. Scaffolds Playwright if the project doesn't have it, uses resilient role/text selectors, and can wire tests into CI. Complements a manual QA pass with real automation. Works with any stack the browser can load (React, Next.js, Vue, Svelte, plain HTML, WordPress). Trigger on "write tests for my site," "add Playwright tests," "test this user flow," "end-to-end tests," "e2e," "browser tests," "test my signup/checkout," or "set up automated testing."
---

# Web Testing (Playwright)

One job: catch broken user journeys automatically. Write tests that mirror what real visitors do, run them, and report what failed with enough detail to fix it. Automation to back up — not replace — a human QA pass (`aie-web-qa`).

Read `reference/setup.md` to install/configure, `reference/patterns.md` before writing tests, and `reference/reporting.md` for the output shape.

## Safety & scope
- Test against **local dev, staging, or sites the person owns/authorizes** — never someone else's production. Confirm the target before running.
- Tests are **read-only against the app's UI**. Do not create test flows that send real money, real emails to third parties, or real irreversible actions against production. Use test/staging data.
- Never hardcode real credentials or secrets in test files — read them from environment variables. Treat any secret you see as sensitive.

## The loop: Discover → Set up → Write → Run → Triage → Report

### 1. Discover
Identify the **critical journeys** — the handful of flows that, if broken, cost the business. Typical: load the homepage, primary navigation, sign-up, log in, the main form (contact / lead / checkout), search, and one core "money" path. Ask for or infer the base URL and any test accounts. See `reference/patterns.md` for how to choose journeys.

### 2. Set up
If the project has no Playwright, scaffold it (`npm init playwright@latest` or add `@playwright/test` + `npx playwright install`). Add a `playwright.config` with `baseURL`, retries for CI, trace/screenshot/video on failure, and a couple of device projects (desktop + mobile). Details and a starter config in `reference/setup.md`.

### 3. Write
- **Resilient selectors:** prefer `getByRole`, `getByLabel`, `getByText` over brittle CSS/XPath. Add `data-testid` only where semantics can't.
- **One journey per test**, arranged Arrange → Act → Assert. Assert on user-visible outcomes (URL, visible text, element state), not implementation details.
- **Auto-wait** — rely on Playwright's built-in waiting; avoid fixed `sleep`s.
- **Catch silent failures:** attach listeners for uncaught page errors and failed network requests, and fail the test if the console logs errors during a journey.
- **Accessibility smoke:** optionally assert the page has one `h1`, labeled inputs, and no obvious ARIA violations.
Templates for auth, form-submit, and navigation journeys are in `reference/patterns.md`.

### 4. Run
Run headless by default (`npx playwright test`); use headed/`--debug` when triaging. Run the mobile project too. Keep tests independent so they can run in parallel.

### 5. Triage failures
For each failure: capture the Playwright trace, a screenshot, the failing assertion, and the console/network errors. Decide: real bug, flaky test (timing/selector), or environment issue. Flaky tests get fixed (better selector/wait), not blindly retried. Never mark a suite green by deleting the failing test.

### 6. Report
Return the summary in `reference/reporting.md` order: pass/fail counts, each failure with repro steps and screenshot, flaky items, and recommended fixes. Offer to wire the suite into CI (a GitHub Actions job that installs browsers, runs the suite, and uploads the report) — see `reference/setup.md`.

## Reference
- `reference/setup.md` — install, `playwright.config`, browsers, and a CI workflow.
- `reference/patterns.md` — selector strategy, choosing journeys, and test templates (auth / form / nav).
- `reference/reporting.md` — the results report format and flaky-test handling.
