# Patterns: selectors, journeys, templates

## Choosing critical journeys

Test the flows that cost real money or trust if they break — not every page. A good default set:

1. **Homepage loads** — 200, key content visible, no uncaught errors from your own origin.
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

Fail the journey on uncaught page errors that come from your page's own origin. `page.on('pageerror')` gives you an `Error` with a message and a stack, and it also fires for other-origin iframes and third-party scripts. The old fixture kept only `err.message`, which drops the stack and still does not say which script threw. Classify with `browserContext.on('weberror')` instead. This pattern needs Playwright 1.60 or newer, because that is when `WebError.location()` was added, and an existing install may be older. Use `location().url` when it is set. When it is empty, which is what `eval` does, read the script URL from a stack frame (a line starting with `at`), not from the error message. The message can name any URL. If you cannot read a frame location, or the location is `about:blank`, count the error as this page so a first-party throw is not dropped. Do not fail on every `console` error or `requestfailed` event: ad pixels, analytics, and font CDNs fail constantly and will make a healthy page look broken. If you also watch the console, keep an explicit allowlist and assert it inside the test. Do not hang the list off `(page as any)` and do not leave the assertion in a comment.

```ts
import { test as base, expect, type Page, type WebError } from '@playwright/test';

// Playwright 1.60+ — WebError.location() was added then.
// An empty location URL means eval. The script URL is on an `at` frame,
// never in the message. about:blank, or no frame URL, counts as this page.
function stackFrameURL(stack: string): string {
  for (const line of stack.split('\n')) {
    if (!/^\s*at\s+\S/.test(line)) continue;
    const match = line.match(/https?:\/\/[^\s)]+?(?=:\d+:\d+)/);
    if (match) return match[0];
  }
  return '';
}

function ownsPageError(page: Page, webError: WebError): boolean {
  if (webError.page() !== page) return false;
  const locationURL = webError.location().url;
  const resourceURL = locationURL || stackFrameURL(webError.error().stack ?? '');
  if (!resourceURL || resourceURL.startsWith('about:')) return true;
  let resourceOrigin = '';
  try {
    resourceOrigin = new URL(resourceURL).origin;
  } catch {
    return true;
  }
  let pageOrigin = '';
  try {
    pageOrigin = new URL(page.url()).origin;
  } catch {
    return true;
  }
  if (!pageOrigin || pageOrigin === 'null') return true;
  return resourceOrigin === pageOrigin;
}

export const test = base.extend<{ pageErrors: string[] }>({
  pageErrors: async ({ page }, use) => {
    const errors: string[] = [];
    const onWebError = (webError: WebError) => {
      if (!ownsPageError(page, webError)) return;
      const location = webError.location();
      const err = webError.error();
      const where = location.url || page.url();
      errors.push(
        `${where}:${location.line}:${location.column} ${err.name}: ${err.message}\n${err.stack ?? ''}`,
      );
    };
    page.context().on('weberror', onWebError);
    await use(errors);
    page.context().off('weberror', onWebError);
  },
});

test('homepage has no uncaught page errors', async ({ page, pageErrors }) => {
  await page.goto('/');
  await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
  expect(pageErrors, pageErrors.join('\n')).toEqual([]);
});
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
