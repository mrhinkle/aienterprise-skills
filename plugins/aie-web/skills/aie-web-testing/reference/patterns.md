# Patterns: selectors, journeys, templates

## Choosing critical journeys

Test the flows that cost real money or trust if they break — not every page. A good default set:

1. **Homepage loads** — 200, key content visible, no uncaught page errors. A third-party script host is ignored only when you pass its hostname in `ignoreHosts` and `location().url` is an `http:` or `https:` URL whose hostname is that host or a subdomain of it.
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

Every uncaught page error fails the test. Do not classify the error by origin. `page.on('pageerror')` gives you an `Error` with a message and a stack, and it also fires for iframes and third-party scripts. The old fixture kept only `err.message`, which drops the stack. Listen with `browserContext.on('weberror')` so the failure text includes the message, the full stack, and `location()`. The message and the stack are failure diagnostics only. Do not parse them, and do not match `ignoreHosts` against them. This pattern needs Playwright 1.60 or newer, because that is when `WebError.location()` was added ([docs](https://playwright.dev/docs/api/class-weberror#web-error-location)), and an existing install may be older.

To ignore a known third-party script host, pass `ignoreHosts`: an array of hostnames. Suppress an error only when `location().url` parses with `new URL()`, the protocol is `http:` or `https:`, and its hostname equals an entry or ends with `.` plus that entry. The comparison is case-insensitive. The check reads only `location().url`. It is never tested against `err.stack` or `err.message`. A message line such as `    at http://host/...` is not a location, even when that line also shows up inside `err.stack`. Leave `ignoreHosts` empty and every uncaught error fails.

Anything `new URL()` cannot parse, or any URL whose protocol is not `http:` or `https:`, is never suppressed. It fails even when the message or the stack names an allowlisted host. A missing location is not proof the script was allowlisted. The trade-off is plain: some third-party `eval` errors in WebKit report the location string `undefined`. That string does not parse, so those errors cannot be allowlisted and will fail the test. That is intended. A virtual URL such as `webpack-internal:///` is not an `http:` or `https:` URL, so it is not suppressible and the error still fails. Pass hostnames, for example `ignoreHosts: ['googletagmanager.com']`. That entry also ignores a subdomain such as `www.googletagmanager.com`. It does not ignore a first-party page whose path or query only mentions that name, and it does not ignore a lookalike host such as `googletagmanager.com.evil.test`. Use the full host. A short entry such as `com` matches every hostname that ends in `.com`. Do not put your own origin on the list.

Do not fail on every `console` error or `requestfailed` event: ad pixels, analytics, and font CDNs fail constantly and will make a healthy page look broken. If you also watch the console, keep a separate allowlist and assert it inside the test. Do not hang the list off `(page as any)` and do not leave the assertion in a comment.

```ts
import { test, expect, type Page, type WebError } from '@playwright/test';

// Playwright 1.60+ — WebError.location() was added then.
// ignoreHosts matches only the hostname of location().url, never err.stack or err.message.
// The URL must parse with new URL() and the protocol must be http: or https:.
// Anything else is not suppressible.
function hostIsIgnored(locationURL: string, ignoreHosts: string[]): boolean {
  if (typeof locationURL !== 'string') return false;
  let parsed: URL;
  try {
    parsed = new URL(locationURL);
  } catch {
    return false;
  }
  if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') return false;
  const host = parsed.hostname.toLowerCase();
  return ignoreHosts.some((entry) => {
    const name = entry.toLowerCase();
    if (name === '') return false;
    return host === name || host.endsWith('.' + name);
  });
}

function watchPageErrors(page: Page, ignoreHosts: string[] = []) {
  const errors: string[] = [];
  const onWebError = (webError: WebError) => {
    const owner = webError.page();
    if (owner && owner !== page) return;
    const err = webError.error();
    const location = webError.location();
    const stack = err.stack ?? '';
    if (hostIsIgnored(location.url, ignoreHosts)) return;
    const where = location.url || '(no location)';
    errors.push(
      `${where}:${location.line}:${location.column} ${err.name}: ${err.message}\n${stack}`,
    );
  };
  page.context().on('weberror', onWebError);
  return {
    errors,
    dispose() {
      page.context().off('weberror', onWebError);
    },
  };
}

test('homepage has no uncaught page errors', async ({ page }) => {
  // Pass a hostname only when you mean to ignore that host and its subdomains:
  // const watched = watchPageErrors(page, ['googletagmanager.com']);
  const watched = watchPageErrors(page);
  try {
    await page.goto('/');
    await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
    expect(watched.errors, watched.errors.join('\n\n')).toEqual([]);
  } finally {
    watched.dispose();
  }
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
