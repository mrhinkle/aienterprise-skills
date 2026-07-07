# Patterns: selectors, journeys, templates

## Choosing critical journeys

Test the flows that cost real money or trust if they break — not every page. A good default set:

1. **Homepage loads** — 200, key content visible, no console errors.
2. **Navigation** — primary nav links resolve and land on the right page.
3. **Auth** — sign-up and log in (against test accounts on staging).
4. **The main form** — contact / lead / newsletter / checkout submits and shows success.
5. **Search** (if present) — a query returns results.
6. **One "money" path** — the single flow the business depends on.

Five to eight solid journeys beat fifty brittle ones.

## Selector strategy (most to least preferred)

1. `getByRole('button', { name: 'Sign up' })` — role + accessible name. Most resilient; doubles as an accessibility check.
2. `getByLabel('Email')`, `getByPlaceholder(...)`, `getByText(...)` — user-visible semantics.
3. `getByTestId('checkout-submit')` — add a `data-testid` only when semantics can't identify the element.
4. CSS/XPath — last resort; brittle and breaks on restyles.

Rely on Playwright's auto-waiting. Never use fixed `page.waitForTimeout(...)` as a substitute for a proper assertion.

## Catch silent failures

```ts
test.beforeEach(async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', e => errors.push(`pageerror: ${e.message}`));
  page.on('console', m => { if (m.type() === 'error') errors.push(`console: ${m.text()}`); });
  page.on('requestfailed', r => errors.push(`net: ${r.url()} ${r.failure()?.errorText}`));
  (page as any)._errors = errors;
});
// ...at the end of a journey: expect((page as any)._errors).toEqual([]);
```

## Template — smoke

```ts
import { test, expect } from '@playwright/test';

test('homepage loads cleanly', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/.+/);
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
});
```

## Template — form submission

```ts
test('contact form submits', async ({ page }) => {
  await page.goto('/contact');
  await page.getByLabel('Name').fill('Test User');
  await page.getByLabel('Email').fill('test@example.com');
  await page.getByLabel('Message').fill('Hello from the test suite.');
  await page.getByRole('button', { name: /send|submit/i }).click();
  await expect(page.getByText(/thank you|received|success/i)).toBeVisible();
});
```

## Template — auth

```ts
test('user can log in', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill(process.env.TEST_EMAIL!);
  await page.getByLabel('Password').fill(process.env.TEST_PASSWORD!);
  await page.getByRole('button', { name: 'Log in' }).click();
  await expect(page).toHaveURL(/dashboard|account|home/);
  await expect(page.getByRole('button', { name: /log ?out|account/i })).toBeVisible();
});
```

## Template — navigation

```ts
test('primary nav works', async ({ page }) => {
  await page.goto('/');
  for (const name of ['About', 'Pricing', 'Contact']) {
    await page.getByRole('link', { name }).click();
    await expect(page.getByRole('heading', { name: new RegExp(name, 'i') })).toBeVisible();
    await page.goBack();
  }
});
```

Keep each test independent (no shared state), so the suite runs in parallel.
