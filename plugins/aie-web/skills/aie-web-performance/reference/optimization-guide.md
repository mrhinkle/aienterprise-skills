# Performance Optimization Guide — Checks, Commands, and Snippets

Free tools only. Adapt paths and framework specifics to the project.

## Measuring

```bash
# Lighthouse CLI (Node)
npx lighthouse https://example.com --output=json --output=html --output-path=./lh-report

# Mobile emulation is the default profile — most users are on mobile.
```

Also read field data from PageSpeed Insights (https://pagespeed.web.dev) or the Chrome UX Report (CrUX). Field data reflects real users; Lighthouse is a lab proxy.

## 1. Images (usually the biggest win)

Checks:
- Intrinsic image dimensions are close to the largest displayed size (not a 4000px image shown at 400px).
- Photos use lossy compression; graphics/screenshots use lossless.
- Modern formats served: AVIF (smallest) or WebP (widely supported), with a fallback.
- `srcset` + `sizes` provided so browsers pick the right resolution.
- Below-the-fold images use `loading="lazy"`. NEVER lazy-load the LCP (hero) image — preload it instead.
- Explicit `width`/`height` (or CSS `aspect-ratio`) to prevent layout shift.

Commands:
```bash
# WebP
cwebp -q 80 input.jpg -o output.webp

# AVIF (libavif)
avifenc --min 20 --max 30 input.png output.avif

# Resize + compress with ImageMagick
magick input.jpg -resize 1200x -quality 82 output.jpg
```

Responsive HTML:
```html
<picture>
  <source type="image/avif" srcset="hero-800.avif 800w, hero-1600.avif 1600w" sizes="(max-width: 800px) 100vw, 800px">
  <source type="image/webp" srcset="hero-800.webp 800w, hero-1600.webp 1600w" sizes="(max-width: 800px) 100vw, 800px">
  <img src="hero-800.jpg" width="1600" height="900" alt="..." fetchpriority="high">
</picture>
```

## 2. CSS

Checks: minified; critical above-the-fold CSS inlined; unused selectors removed; animations use `transform`/`opacity`, not `top`/`left`/`width`/`height`.

```bash
# Remove unused CSS (v3 API — verify current syntax in PurgeCSS docs)
npx purgecss --css styles.css --content "**/*.html" --output ./dist
```
- Tailwind projects: unused CSS is purged automatically via the `content` globs in the config — confirm they cover every template path.
- Inline the small critical block in `<head>`; load the rest with a non-blocking pattern.

## 3. JavaScript

Checks: minified; split by route/component; non-critical scripts `defer` or `async`; tree-shaking on; no polyfills for browsers you don't support.

```html
<script src="/js/analytics.js" defer></script>   <!-- runs after parse, in order -->
<script src="/js/widget.js" async></script>       <!-- runs ASAP, order not guaranteed -->
```
- Analyze bundles: `rollup-plugin-visualizer` (Vite/Rollup), `webpack-bundle-analyzer`, or `@next/bundle-analyzer` (Next.js).
- Large libraries (moment, lodash, full icon sets) are common offenders — replace or import only what's used.
- Reducing long tasks on the main thread is the primary lever for INP.

## 4. Fonts

```css
@font-face {
  font-family: "Brand";
  src: url("/fonts/brand.woff2") format("woff2");
  font-display: swap;   /* show fallback immediately, swap when ready */
}
```
```html
<link rel="preload" href="/fonts/brand.woff2" as="font" type="font/woff2" crossorigin>
```
- Subset to the characters/languages actually used.
- Prefer one variable font over many static weights.
- Match fallback metrics (`size-adjust`, `ascent-override`) to reduce font-swap CLS.

## 5. Resource hints

```html
<link rel="preload" href="/hero.avif" as="image" fetchpriority="high">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://analytics.example.com">
<link rel="prefetch" href="/likely-next-page">
```
Preload only what LCP needs. Over-preloading contends for bandwidth and hurts LCP.

## 6. Delivery

- Confirm Brotli (preferred) or gzip on text assets.
- Serve over HTTP/2 or HTTP/3.
- Set long `Cache-Control` (`immutable`) on hashed/fingerprinted assets.
- Put static assets behind a CDN close to users.

## Core Web Vitals cheat sheet

| Metric | Good | Mostly caused by |
|---|---|---|
| LCP | < 2.5s | slow hero image, render-blocking CSS/JS, slow server |
| INP | < 200ms | heavy JS, long main-thread tasks |
| CLS | < 0.1 | images/embeds without dimensions, injected content, font swap |

Sources: https://web.dev/articles/vitals, https://web.dev/blog/inp-cwv-launch
