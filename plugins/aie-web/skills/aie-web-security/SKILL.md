---
name: aie-web-security
description: Read-only defensive self-audit of a website or web app for common security gaps — exposed secrets in client code and git history, dependency vulnerabilities, missing or weak HTTP security headers (CSP, HSTS, X-Content-Type-Options, X-Frame-Options), HTTPS/TLS and mixed-content issues, unsafe DOM sinks (innerHTML/XSS), CSRF/cookie and CORS misconfigurations, and privacy-compliance gaps. Produces findings ranked by severity with plain-language fixes. This skill NEVER attacks a live target — it only reviews code, config, and public response headers you own. Trigger on "security audit," "security review," "security check," "is my site secure," "check for exposed API keys," "audit my security headers," "am I leaking secrets," "check my CSP," "HTTPS/SSL check," "XSS review," or "privacy compliance check."
---

# Web Security Self-Audit (Defensive)

Runs a safe, read-only security review of a website or web app you control. It reviews source code, configuration, dependency manifests, git history, and public response headers. It does not scan, probe, fuzz, or attack anything — this is a self-audit, not a penetration test.

## Scope and Safety Rules

- Only audit assets the user owns or is explicitly authorized to review.
- Read-only. Do not send crafted/malicious payloads, brute-force, or exploit anything.
- Never print full secret values in output — mask them (`re_****…abcd`).
- If asked to attack a third-party site or bypass a control, decline and redirect to the defensive scope.

## Workflow

1. **Confirm scope** — which repo/folder, which deployed URL (if any), and the stack (framework, host, package manager). Stay stack-agnostic; adapt commands to what you find.
2. **Run the checks** in the order below, gathering evidence.
3. **Report** using the severity format at the end.

Read `reference/audit-checklist.md` for the full itemized checklist across all areas. Read `reference/security-headers.md` for header values and host-specific config examples. Read `reference/glossary.md` if the user needs plain-language definitions.

## Check Areas (summary)

1. **Secrets exposure (Critical)** — Grep the working tree AND git history for API keys, tokens, passwords, private keys, connection strings. Confirm `.env*` and `*.pem` are git-ignored and not committed. Confirm secrets live in the host's environment-variable store, not in client-shipped bundles. Any secret prefixed for client exposure (e.g., build-time public vars) must NOT be a real secret. If a live secret is found, flag it Critical and instruct immediate rotation.
2. **Dependencies** — Run the package manager's audit (`npm audit`, `pnpm audit`, `yarn audit`, `pip-audit`, etc.). Classify by severity, note fixable vs. breaking.
3. **Security headers** — Check for Content-Security-Policy, Strict-Transport-Security (HSTS), X-Content-Type-Options, X-Frame-Options (or CSP `frame-ancestors`), Referrer-Policy, and Permissions-Policy. See `reference/security-headers.md`.
4. **HTTPS / TLS** — Certificate validity, single 301 HTTP→HTTPS redirect, HSTS present, no mixed content (HTTP assets on an HTTPS page).
5. **Input handling / XSS** — Flag `innerHTML`, `dangerouslySetInnerHTML`, `document.write`, and unescaped user input rendered to the DOM or into URLs. Recommend `textContent` and `encodeURIComponent`.
6. **CSRF / cookies** — Confirm state-changing endpoints validate origin or use anti-CSRF tokens; confirm cookies set `SameSite` and, for sensitive cookies, `HttpOnly` + `Secure`.
7. **CORS** — Flag wildcard `Access-Control-Allow-Origin: *` on any authenticated or sensitive endpoint.
8. **Third-party scripts** — Inventory external scripts; recommend Subresource Integrity (SRI) and version pinning for CDN resources; note what data analytics/trackers collect.
9. **Abuse prevention** — Confirm public form/serverless endpoints have spam protection (honeypot and/or rate limiting) and reasonable function timeouts.
10. **Privacy compliance** — Confirm a linked privacy policy, disclosure of data collected and third parties used, cookie consent where required, and a contact path for data requests (GDPR/CCPA baseline).

## Output Format

Lead with an overall grade and counts, then list findings.

**Overall: B — 1 critical, 3 warnings, 4 recommendations**

For each finding:
- **Severity** — CRITICAL (fix before launch) / WARNING (fix within a week) / RECOMMENDATION (best practice)
- **What** — the issue, with file path and line or the header that's missing
- **Why it matters** — one plain-language sentence
- **Fix** — exact code, config, or step

Order findings Critical → Warning → Recommendation.

## References

- OWASP Top 10 — https://owasp.org/www-project-top-ten/
- OWASP Secure Headers Project — https://owasp.org/www-project-secure-headers/
- MDN HTTP headers — https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- MDN Content Security Policy — https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- MDN Mixed content — https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content
