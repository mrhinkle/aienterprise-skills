---
name: aie-web-performance
description: Audits and fixes web page load performance. Analyzes images, CSS, JavaScript, fonts, and third-party assets, then produces a prioritized before/after report with concrete optimization steps and copy-paste code. Targets Core Web Vitals (LCP, INP, CLS) and Lighthouse scores. Stack-agnostic — plain HTML, WordPress, React, Next.js, Vite, Astro, or a hosted builder; uses free tools only (Lighthouse, ImageMagick, cwebp/AVIF, PurgeCSS, bundle analyzers). Trigger on "my site is slow," "speed up my site," "improve page load," "optimize performance," "Core Web Vitals," "LCP/INP/CLS," "Lighthouse score," "reduce bundle size," "optimize images," "why is my site slow," or "performance audit."
---

# Web Performance Optimizer

Find what makes a page slow, then fix it. Produce a prioritized report with real byte savings and ready-to-use code — not generic advice.

## Why it matters

Speed affects conversion, bounce rate, and search ranking. Google uses Core Web Vitals as a ranking signal (https://developers.google.com/search/docs/appearance/page-experience), and field data consistently ties faster pages to higher engagement and revenue. Optimize the metrics that reflect real user experience: LCP, INP, and CLS.

## When to use this skill

The user says the site feels slow, has poor Lighthouse or Core Web Vitals scores, or wants to trim page weight. Works from a live URL or from a local project directory / source files.

## Inputs to gather

- **URL or local path** to the site.
- **Stack** if known (plain HTML, WordPress, React, Next.js, Vite, Astro, etc.) — it changes which build fixes apply.
- **Target devices/browsers** and any specific concern (slow mobile, janky scroll, layout jump).

## Audit procedure

Measure first, then attribute weight to the biggest offenders. For the full checklists and the exact commands and code snippets, read `reference/optimization-guide.md`.

1. **Baseline** — run Lighthouse (or read PageSpeed Insights field data) and record LCP, INP, CLS, FCP, TBT/TTI, and total transfer size. Note the LCP element specifically.
2. **Images** — usually 50-80% of page weight. Check dimensions vs. displayed size, compression, modern formats (AVIF/WebP), `srcset`/`sizes`, and lazy loading for below-the-fold images (never lazy-load the LCP image).
3. **CSS** — minification, critical-CSS inlining for above-the-fold, unused-selector removal, and avoiding layout-triggering animations (prefer `transform`/`opacity`).
4. **JavaScript** — the most expensive resource. Check bundle size, code splitting, `defer`/`async`, tree-shaking, and unnecessary polyfills. Reducing main-thread work is the main lever for INP.
5. **Fonts** — `font-display: swap`, preload critical fonts, subsetting, and variable fonts to replace multiple files. Prevents invisible-text delays and font-swap CLS.
6. **Preload / preconnect / prefetch** — preload the LCP resource, preconnect to critical third-party origins, prefetch likely next-page assets. Don't over-preload.
7. **Delivery** — confirm Brotli/gzip compression, HTTP/2 or HTTP/3, caching headers, and CDN use.

## Core Web Vitals targets (good thresholds)

Source: https://web.dev/articles/vitals

- **LCP** (Largest Contentful Paint) — < 2.5s
- **INP** (Interaction to Next Paint) — < 200ms  *(replaced FID as a Core Web Vital in March 2024 — https://web.dev/blog/inp-cwv-launch)*
- **CLS** (Cumulative Layout Shift) — < 0.1
- Supporting: FCP < 1.8s, TBT low, Lighthouse Performance 90+.

## Priority of fixes

**High impact (do first)**
1. Image optimization — 30-50% byte reduction typical.
2. JS minification + code splitting — 20-40% reduction, big INP win.
3. Unused CSS removal — 20-60% reduction.
4. Font-display + subsetting — faster text render, less CLS.
5. Reserve space for images/embeds/ads (width+height or aspect-ratio) — kills CLS.

**Medium impact**
- Critical CSS inlining, defer/async scripts, preload the LCP resource, Brotli/gzip.

**Lower impact (situational)**
- Service-worker caching, CDN tuning, HTTP/3.

## Output format

```
PERFORMANCE REPORT — {url}
Date: {date}

CORE WEB VITALS (before)
  LCP {x}s   INP {x}ms   CLS {x}
  Lighthouse Performance: {n}/100
  Total transfer: {x} KB   |  LCP element: {selector}

TOP BOTTLENECKS (ranked by impact)
  1. {issue} — est. saving {x} KB / {x}ms — {fix}
  ...

FIXES BY AREA
  Images    ...  (with commands/HTML)
  CSS       ...
  JavaScript...
  Fonts     ...
  Delivery  ...

PROJECTED AFTER
  LCP ~{x}s   INP ~{x}ms   CLS ~{x}   (state assumptions)

VERIFICATION
  Re-run Lighthouse; confirm field data in PageSpeed Insights / CrUX after ~28 days.
```

## Guardrails

- Optimizations must preserve functionality — flag anything that could change behavior.
- Field data (real users, CrUX) is the source of truth; lab data (Lighthouse) is a proxy. Say which one a number comes from.
- Don't invent savings numbers — label estimates as estimates and show the reasoning.
- All recommended tools are free: Lighthouse CLI, ImageMagick, `cwebp`/`avifenc`, PurgeCSS, and framework bundle analyzers.

**Sample run:** `examples/sample-run.md` — a condensed real run showing the exact output this skill produces.
