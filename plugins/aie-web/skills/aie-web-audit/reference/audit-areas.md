# Website Health Audit — Detailed Checklist

Mark each item Pass / Fail / N-A and note the page or element.

## 1. SEO & AEO

- [ ] Title tags present, unique, 50-60 chars.
- [ ] Meta descriptions present, unique, 150-160 chars.
- [ ] One unique H1 per page; H2-H6 in logical order.
- [ ] Open Graph and Twitter/X card tags present for social sharing.
- [ ] JSON-LD structured data present and valid (Organization, Article, Product, LocalBusiness, etc.).
- [ ] Viewport meta tag and responsive patterns present.
- [ ] Every meaningful image has descriptive alt text.
- [ ] URLs are readable, lowercase, hyphenated, low-parameter.
- [ ] Answer-engine readiness: direct-answer lead paragraphs, Q&A blocks, tables, cited sources, visible freshness dates.
- [ ] Core Web Vitals signals look healthy (LCP, INP, CLS). For depth, hand off to `aie-web-performance`.

## 2. Copy & content

- [ ] Headline hooks and states a clear benefit.
- [ ] Value proposition understandable by a stranger within ~5 seconds.
- [ ] CTAs are specific, visible, and action-oriented ("Start free trial" not "Submit").
- [ ] Reading level is accessible (aim ~6th-8th grade for general audiences); sentences are short.
- [ ] Microcopy (buttons, form labels, error/help text) is clear and human.
- [ ] Voice and tone are consistent across pages.
- [ ] No filler, no jargon walls, no contradictory claims.

## 3. UX

- [ ] Any key page reachable in ~3 clicks or fewer.
- [ ] Layout works at 320px, 375px, 768px, 1024px, and 1440px+ with no horizontal scroll.
- [ ] Most important content is the most visually prominent.
- [ ] Tap targets are at least ~48x48px and not overlapped by sticky headers/modals.
- [ ] Body line length ~50-75 characters; base font size 16px+.
- [ ] No hostile anti-patterns: autoplaying video with sound, pop-ups on load, ambiguous submit buttons, hidden nav.
- [ ] Visible focus states and clear interactive feedback.

## 4. Security surface (public signals only)

- [ ] HTTPS enforced on all pages; valid, non-expired certificate.
- [ ] Security headers present: Content-Security-Policy, Strict-Transport-Security (HSTS), X-Frame-Options, X-Content-Type-Options. Reference: https://owasp.org/www-project-secure-headers/
- [ ] No mixed content — every asset loads over HTTPS.
- [ ] Third-party script inventory reviewed (what loads, from where, why).
- [ ] Privacy policy and cookie/consent handling present where required.

## Severity guide

- **Critical** — security exposure or broken core functionality.
- **Major** — significant SEO or UX problem that costs traffic or conversions.
- **Minor** — worth fixing, not urgent.
- **Cosmetic** — polish with no functional impact.
