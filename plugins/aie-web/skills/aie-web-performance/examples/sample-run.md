# Sample run — aie-web-performance

Condensed report from a run against the demo site (`brightpath.example`, fictionalized). Output shape matches a live run.

```
PERFORMANCE REPORT — brightpath.example
Date: 2026-07-14

CORE WEB VITALS (before, lab data — Lighthouse mobile)
  LCP 4.1s   INP 310ms   CLS 0.24
  Lighthouse Performance: 54/100
  Total transfer: 3,910 KB  |  LCP element: img.hero-banner

TOP BOTTLENECKS (ranked by impact)
  1. Hero image is 2.8 MB PNG at 4000px, displayed at 1200px — est. saving
     ~2,500 KB / ~1.5s LCP — resize + AVIF/WebP + fetchpriority="high"
  2. All JS in one 890 KB bundle, no code splitting — est. saving ~400 KB and
     the main INP lever — split by route, defer analytics
  3. No width/height on 14 images — the whole CLS 0.24 — add dimensions or
     aspect-ratio
  4. Two font families, 6 weights, no font-display — swap + subset + preload
  5. No Brotli on text assets — est. saving ~120 KB — enable at host

FIXES BY AREA
  Images    magick hero.png -resize 1200x -quality 82 hero.jpg
            cwebp -q 80 hero.jpg -o hero.webp   (+ <picture> block, see
            reference/optimization-guide.md for the exact HTML)
  JS        route-level dynamic imports; <script defer> on analytics.js
  Fonts     font-display: swap; preload brand.woff2; drop 3 unused weights
  Delivery  enable Brotli; Cache-Control: immutable on hashed assets

PROJECTED AFTER
  LCP ~2.2s   INP ~180ms   CLS ~0.02
  (Assumes hero fix ships and the bundle splits; estimates labeled as estimates.)

VERIFICATION
  Re-run Lighthouse after deploy; confirm field data in PageSpeed Insights
  (CrUX) after ~28 days — field data is the source of truth.
```
