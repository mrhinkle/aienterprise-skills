# Sample run — aie-web-security

Condensed defensive self-audit of the demo project (repo + deployed site, fictionalized as `brightpath.example`). Note the masked secret — full values never appear in a report.

**Overall: C+ — 1 critical, 3 warnings, 3 recommendations**

```
CRITICAL
- What: Live email-API key committed in git history (removed from HEAD in commit
  a41f2c9, still present in history) — key masked: re_****…8kQd
  Why it matters: anyone with repo access (or a leak) can send mail as your domain.
  Fix: rotate the key at the provider NOW, then purge history (git filter-repo)
  and add .env* to .gitignore. Rotation first — history-scrubbing without
  rotation fixes nothing.

WARNING
- What: No Content-Security-Policy header on any response
  Why: one injected or compromised third-party script can run with full access.
  Fix: start with default-src 'self'; script-src 'self'; add sources as needed
  (see reference/security-headers.md for host config examples).

- What: npm audit — 2 high (prototype pollution in a transitive dep), 5 moderate
  Why: known, public exploits map to known versions.
  Fix: `npm audit fix` clears both highs (non-breaking); re-run in CI weekly.

- What: Contact endpoint has no rate limiting; honeypot only
  Why: trivially scriptable spam/abuse against the email quota.
  Fix: cap ~5 submissions/IP/hour at the edge or in the handler.

RECOMMENDATION
- HSTS max-age is 300 (testing value) — raise to 31536000 once HTTPS is confirmed stable.
- Analytics CDN script is unpinned and lacks Subresource Integrity — pin + SRI hash.
- Privacy policy doesn't name the email provider as a processor — add it.
```

Behavior this sample demonstrates: read-only throughout (no probing or payloads), evidence per finding (commit hash, header name, dep path), the secret masked, and immediate-rotation instruction on the live key.
