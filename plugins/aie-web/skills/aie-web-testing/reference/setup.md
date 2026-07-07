# Setup: Playwright + CI

## Install

New project (interactive scaffold):

```bash
npm init playwright@latest
```

Existing project:

```bash
npm install -D @playwright/test
npx playwright install            # download browser binaries
```

## playwright.config (starter)

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  expect: { timeout: 5_000 },
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,          // retry only in CI, to absorb rare flake
  reporter: [['html', { open: 'never' }], ['list']],
  use: {
    baseURL: process.env.BASE_URL ?? 'http://localhost:3000',
    trace: 'on-first-retry',                 // trace failing runs for triage
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'desktop-chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-safari',    use: { ...devices['iPhone 14'] } },
  ],
});
```

- Point `baseURL` at local dev or staging via the `BASE_URL` env var — never hardcode production.
- `retries` only in CI so a local run surfaces flake instead of hiding it.

## Credentials

Read any test-account credentials from environment variables, never from the test source:

```ts
const email = process.env.TEST_EMAIL!;
const password = process.env.TEST_PASSWORD!;
```

Store them in a local `.env` (git-ignored) or CI secrets.

## CI (GitHub Actions)

```yaml
name: e2e
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
        env:
          BASE_URL: ${{ secrets.STAGING_URL }}
          TEST_EMAIL: ${{ secrets.TEST_EMAIL }}
          TEST_PASSWORD: ${{ secrets.TEST_PASSWORD }}
      - uses: actions/upload-artifact@v4
        if: ${{ !cancelled() }}
        with:
          name: playwright-report
          path: playwright-report/
```

Reference: Playwright docs — https://playwright.dev/docs/intro and https://playwright.dev/docs/ci-intro
