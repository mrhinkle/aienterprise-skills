# Web QA — Full Checklist

Mark each Pass / Fail / N-A with the page or element.

## 1. Page rendering
- [ ] Every page returns 200 (or an intended 3xx redirect); no accidental 404/500.
- [ ] No blank pages, broken images, or missing content blocks.
- [ ] Layout holds at 320px, 768px, 1024px, and 1440px+.
- [ ] No console errors/warnings that indicate a rendering failure.
- [ ] No jarring flash of unstyled content (FOUC).

## 2. Cross-browser
- [ ] Chrome / Edge (latest) on Windows and macOS.
- [ ] Safari on macOS and iOS (WebKit — different engine, catches unique bugs).
- [ ] Firefox (latest) — often surfaces CSS edge cases.
- [ ] Verify in each: form submission, JS execution, CSS layout, media playback, animations.

## 3. Mobile & responsive
- [ ] `<meta name="viewport" content="width=device-width, initial-scale=1">` present and correct.
- [ ] No horizontal scrolling at any width.
- [ ] Tap targets ~48x48px+; not overlapped by sticky headers or modals.
- [ ] Images scale; no text cut off.
- [ ] Forms are single-column with large inputs.
- [ ] Tested at 320 / 375 / 768 / 1024 / 1440px.

## 4. Forms (where the site earns money or leads)
- [ ] Every field fillable without error.
- [ ] Required fields reject empty submission; email fields reject invalid input.
- [ ] Error messages are specific ("Enter a valid email," not "Error").
- [ ] Submit button doesn't double-submit on slow networks.
- [ ] Success path confirmed: message, redirect, OR email actually arrives (test with a real inbox).
- [ ] No form data leaking into the URL or browser console.

## 5. JavaScript console health
- [ ] Zero red errors in DevTools Console.
- [ ] No unhandled promise rejections.
- [ ] No failed network requests (404/500) that break functionality.
- [ ] Third-party scripts load without throwing.

## 6. Navigation flow
- [ ] Every nav/link/button destination resolves to a real page.
- [ ] Breadcrumbs accurate and clickable.
- [ ] Browser back button works; history intact.
- [ ] A styled, on-brand 404 page exists.
- [ ] No dead ends; mobile menu opens and closes correctly.

## 7. Third-party integrations
- [ ] Analytics loads (confirm a hit in the network tab or real-time dashboard).
- [ ] Email service sends and delivers a real test message.
- [ ] Payment processor loads without error (use test mode; do not run live charges).
- [ ] Newsletter/CRM embeds appear and function on repeated reloads.
- [ ] External CDNs (fonts, icons, libraries) load reliably.

## 8. Accessibility basics
Reference: https://www.w3.org/WAI/WCAG22/quickref/
- [ ] Full keyboard navigation; Enter/Space activate controls.
- [ ] Visible focus indicator on every interactive element.
- [ ] Images have alt text; buttons and inputs have accessible labels.
- [ ] Text/background contrast meets WCAG AA (4.5:1 body, 3:1 large text).
- [ ] Complex widgets (carousels, modals, dropdowns) have correct ARIA roles.

## 9. Visual regression
- [ ] Consistent spacing; no random gaps.
- [ ] No overlapping text or elements.
- [ ] Images sized correctly (not stretched/squished).
- [ ] Fonts load without a fallback flash.
- [ ] Icons aligned and consistent.
- [ ] Hover / interactive states visible.

## 10. SSL / security
- [ ] HTTPS on all pages; lock icon shows.
- [ ] Certificate valid (not expired, not self-signed).
- [ ] No mixed content (every asset over HTTPS).
- [ ] HSTS header present.

## 11. Performance smoke test
- [ ] Pages usable in under ~3s on 4G mobile.
- [ ] LCP < 2.5s.
- [ ] CLS minimal — no unexpected movement.
- [ ] No huge uncompressed media blocking render.
- [ ] Lighthouse Performance 90+ is a positive signal (not a hard gate). Full pass: hand off to `aie-web-performance`.

## Pre-QA readiness
- [ ] Site is on staging/test (not production).
- [ ] All dev work is complete.
- [ ] You have access to every form, integration, and third-party service.
- [ ] A real device or browser device-emulation is available.
- [ ] 30-60 minutes of uninterrupted time blocked.
- [ ] A way to log issues (tracker, doc, or ticket) is ready.
