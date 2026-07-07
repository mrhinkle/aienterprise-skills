# Web bundle (aie-web)

Eight focused skills for auditing and improving any website. All are **stack-agnostic** — plain HTML, WordPress, React, Next.js, Vite, Astro, or a hosted builder — and most work from just a live URL. Each produces a scored findings report with severity levels and a prioritized fix list.

Start with **aie-web-audit** for a broad scan; it hands off to the specialists below. Or call a specialist directly.

---

## aie-web-audit — broad health audit
Four-part scan of a live site from its URL: on-page basics, performance signals, obvious SEO issues, and surface UX. No repo or code access needed. Best first step — it tells you which specialist to run next.
Trigger: "audit my site," "review thesite.com."

## aie-web-seo — SEO + answer-engine optimization
Classic search (Google, Bing) **and** answer engines (ChatGPT, Perplexity, Google AI Overviews, Claude). Checks meta tags, heading hierarchy, JSON-LD structured data mapped to rich results, sitemaps/robots, Core Web Vitals signals (LCP, INP, CLS), keyword-to-page mapping, content gaps, and extractable direct-answer blocks. Cites standards (schema.org, Google Search Central, web.dev).
Trigger: "check SEO," "will AI cite my site," "schema markup audit," "AEO."
Reference: `audit-checklist.md`, `schema-and-aeo.md`.

## aie-web-performance — load performance
Audits LCP, INP, CLS and the usual culprits (images, render-blocking assets, fonts, bundle size), then gives concrete fixes with an effort/impact call.
Trigger: "why is my site slow," "improve performance," "Core Web Vitals."
Reference: `optimization-guide.md`.

## aie-web-qa — pre-launch / post-update gate
The holistic "does this actually work?" pass before you ship or after an update: functionality, responsiveness, cross-browser basics, console errors, obvious regressions.
Trigger: "QA this site," "is it ready to launch," "test before deploy."
Reference: `qa-checklist.md`.

## aie-web-security — defensive self-audit (read-only)
A **defensive** review only — no attack tooling. Looks for exposed secrets in client code and git history, dependency vulnerabilities, missing/weak security headers (CSP, HSTS, X-Frame-Options), HTTPS/TLS and mixed content, unsafe DOM sinks (innerHTML/XSS), CSRF/cookie and CORS misconfigurations, and privacy gaps. Cites OWASP.
Trigger: "security review," "is my site secure," "check for exposed secrets."
Reference: `audit-checklist.md`, `security-headers.md`, `glossary.md`.

## aie-web-links — link & asset validation
Crawls the site and validates every internal link, external link, image, and asset. Flags broken links (404/410/5xx), mixed content, redirect chains, orphaned pages, dead in-page anchors, and malformed `mailto:`/`tel:` links.
Trigger: "check my links," "find broken links," "link audit."
Reference: `status-codes.md`, `fixes.md`.

## aie-web-forms — make forms actually work
Wires a contact, inquiry, or newsletter form to a delivery provider (server + email API, hosted backend, or newsletter embed — providers shown as swappable examples), with client- and server-side validation, spam protection (honeypot + rate limiting), accessible labels and error messages, loading states, and clear success/error feedback.
Trigger: "wire up my form," "my contact form doesn't send," "connect form to email."
Reference: `providers.md`, `serverless-example.md`, `accessibility.md`.

## aie-web-ux — usability review
Reviews the site against Nielsen's 10 usability heuristics plus WCAG readability: navigation clarity, visual hierarchy, clickable affordances, form feedback, clutter, mobile/touch, readability, and error handling. Returns a scorecard and prioritized fixes.
Trigger: "review the UX," "is this confusing," "usability audit."
Reference: `checklists.md`, `journeys.md`.

---

## Notes and limits

- A remote-URL audit sees only public, rendered pages — not authenticated areas or server code. The skills say so and sample accordingly.
- They don't fabricate numbers (search volume, domain authority): estimates are marked as estimates.
- Findings name the exact element, page, or file and the concrete fix — the point is improvement, not a grade.
