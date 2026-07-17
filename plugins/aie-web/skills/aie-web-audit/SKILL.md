---
name: aie-web-audit
description: Runs a broad four-part health audit of any live website from just its URL — no repo or code access needed. Covers SEO/AEO signals, copy and messaging, UX and mobile usability, and a public-facing security surface scan. Produces an overall health score, category scores, top quick wins, and findings sorted by severity. Stack-agnostic — WordPress, Squarespace, Wix, Webflow, Shopify, plain HTML, or a custom React/Next/Vite build. Trigger on "audit my site," "check my website," "how's my site doing," "score my website," "what's wrong with my site," "review my site," "is my site any good," "site health check," or "review my WordPress/Squarespace/Wix site."
---

# Website Health Audit

A fast, broad first look at any live website. One URL in, one consolidated report out — health score, quick wins, and a fix roadmap across four dimensions. This is the wide-angle audit; when a dimension needs depth, hand off to the focused skills noted at the end.

## When to use this skill

The user has a live site and wants an honest overall read: what's working, what's broken, and what to fix first. No GitHub, no code handoff, no login required — the audit works from public pages only.

## Inputs

- A **live URL**. That's the minimum.
- Optional: specific pages or flows to prioritize; known concerns; the audience the site serves.

Fetch the URL and a few key public pages (home, about, primary product/service, contact). Analyze the rendered HTML and CSS. Client-side JavaScript state is only partially visible from a fetch — note that where it limits a finding.

## The four-part audit

Work through all four. For the full checkable item lists, read `reference/audit-areas.md`.

1. **SEO & AEO** — title/meta tags, heading hierarchy, Open Graph/social tags, JSON-LD schema, mobile signals, image alt text, URL structure, Core Web Vitals indicators, and answer-engine readiness. (For a deep SEO pass, use the `aie-web-seo` skill.)
2. **Copy & content** — headline hook, value proposition clarity ("can a stranger get it in 5 seconds?"), CTA strength and placement, readability, microcopy, and tone consistency.
3. **UX** — navigation depth (find anything in ~3 clicks), mobile responsiveness, visual hierarchy, tap-target size, line length and font size, and common anti-patterns (autoplay video, load-time pop-ups, ambiguous buttons).
4. **Security surface** — HTTPS enforcement, security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options), mixed content, third-party script inventory, and presence of a privacy/cookie policy. This is a public-signal scan only — see limits below.

## Scoring

Score each of the four categories 0-100, then average for the overall health score. Interpret:

- **80-100** Strong — minor polish only.
- **65-79** Good — a few meaningful fixes.
- **50-64** Fair — clear gaps, solid quick wins available.
- **Below 50** Needs work — prioritize the critical findings.

## Output format

```
WEBSITE HEALTH AUDIT — {url}
Date: {date}

OVERALL HEALTH: {n}/100

CATEGORY SCORES
  SEO & AEO   {n}/100
  Copy        {n}/100
  UX          {n}/100
  Security    {n}/100

TOP QUICK WINS (high impact, low effort)
  1. {fix} — {effort estimate}
  ... (up to 5)

FINDINGS BY SEVERITY
  [Critical] security issues, broken functionality
  [Major]    significant SEO or UX problems
  [Minor]    good-to-fix issues
  [Cosmetic] polish

WHAT'S NEXT
  {which focused skill or action addresses each major finding}
```

Each finding names the exact page/element and a concrete fix. Keep the tone encouraging and specific: "62/100 is a solid base — these five changes could push it past 80." No shame; every site is a work in progress.

## What this audit cannot check

Be transparent. A public URL audit does **not** see:

- Server-side code quality (Node, Python, PHP, database queries).
- Database security or injection risk.
- Backend dependencies (packages, plugins, libraries).
- Full client-side JavaScript execution and dynamic state.
- Authenticated pages (admin panels, member dashboards).
- The complete sitemap — it samples public pages.
- Performance under real global load — it tests from one location.

For those, the focused skills go deeper: `aie-web-seo` (SEO/AEO), `aie-web-performance` (speed and Core Web Vitals), and `aie-web-qa` (does everything actually work).

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
