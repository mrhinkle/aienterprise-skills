# Web Security Self-Audit — Full Checklist

Work top to bottom. Gather evidence (file path, line, header name) for every item so findings are checkable.

## 1. Secrets exposure (Critical)

- [ ] Grep working tree for key patterns: `sk_`, `re_`, `AKIA`, `AIza`, `xox`, `-----BEGIN * PRIVATE KEY-----`, `password=`, `mongodb://`, `postgres://`, bearer tokens.
- [ ] Search git history, not just the current tree, for the same patterns (secrets removed from HEAD may still be in history).
- [ ] Confirm `.env`, `.env.local`, `.env.*`, `*.pem`, `*.key` are in `.gitignore` and NOT tracked.
- [ ] Confirm no secret is hardcoded in client-side JS/TS or shipped in the build bundle.
- [ ] Confirm build-time "public" variables (client-exposed prefixes) contain only non-sensitive values.
- [ ] Confirm secrets are stored in the host's environment variable / secret manager, scoped to the right environment (prod vs. preview).
- [ ] If any live secret is found: flag Critical, mask it in the report, and instruct the user to rotate it immediately at the provider.

## 2. Dependency vulnerabilities

- [ ] Run the ecosystem audit tool (`npm audit`, `pnpm audit`, `yarn audit`, `pip-audit`, `bundle audit`, `cargo audit`).
- [ ] List findings by severity (Critical/High/Medium/Low) with CVE IDs.
- [ ] Note which are auto-fixable vs. require a breaking upgrade.
- [ ] Recommend running audits on a schedule and in CI.

## 3. Security headers

Check the deployed response headers (or the config that sets them). See `security-headers.md` for values.

- [ ] Content-Security-Policy present and not trivially permissive.
- [ ] Strict-Transport-Security (HSTS) with a long max-age.
- [ ] X-Content-Type-Options: nosniff.
- [ ] X-Frame-Options: DENY/SAMEORIGIN (or CSP `frame-ancestors`).
- [ ] Referrer-Policy set (e.g., strict-origin-when-cross-origin).
- [ ] Permissions-Policy locks down camera/mic/geolocation unless needed.

## 4. HTTPS / TLS

- [ ] Valid, unexpired certificate.
- [ ] Single 301 redirect from HTTP to HTTPS (no chains).
- [ ] HSTS present.
- [ ] No mixed content — every script/style/image/font/media URL is https or relative.

## 5. Input handling / XSS

- [ ] Flag `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `dangerouslySetInnerHTML`.
- [ ] Flag user-controlled input rendered to the DOM without escaping — recommend `textContent`.
- [ ] Flag user input interpolated into URLs without `encodeURIComponent`.
- [ ] Flag user input interpolated into email/HTML templates on the server without escaping.

## 6. CSRF / cookies

- [ ] State-changing endpoints validate origin or use anti-CSRF tokens.
- [ ] Cookies set `SameSite` (Lax or Strict).
- [ ] Session/auth cookies set `HttpOnly` and `Secure`.

## 7. CORS

- [ ] No wildcard `Access-Control-Allow-Origin: *` on authenticated or sensitive endpoints.
- [ ] Allowed origins are an explicit allowlist.
- [ ] Preflight (OPTIONS) handled correctly.

## 8. Third-party scripts

- [ ] Inventory every external `<script>` / embed.
- [ ] CDN resources pinned to a version and carry Subresource Integrity (SRI) hashes.
- [ ] Note what data analytics/tracking scripts collect and whether disclosed.

## 9. Abuse prevention

- [ ] Public forms have a honeypot field and/or rate limiting.
- [ ] Serverless/API endpoints have sane timeouts and are rate-limited.

## 10. Privacy compliance (GDPR/CCPA baseline)

- [ ] Privacy policy page exists and is linked (footer is fine).
- [ ] Discloses data collected (email, IP, analytics) and retention.
- [ ] Names third-party processors used.
- [ ] Cookie consent where required by jurisdiction.
- [ ] Contact path for access/deletion requests.

## Pre-launch gate

Treat any unchecked Critical item as a launch blocker: committed secrets, critical dependency CVEs, missing HTTPS, or user input written via innerHTML.
