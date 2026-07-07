# Link Status Codes

How to interpret the response for each checked link.

| Code | Meaning | Action |
|------|---------|--------|
| 200 | OK | No action. |
| 301 | Moved Permanently | Update the link to the final URL; collapse any chain. |
| 302 / 307 | Temporary redirect | Works, but confirm it's intentionally temporary. |
| 304 | Not Modified (cached) | Works. |
| 400 | Bad Request | Malformed URL — fix it. |
| 401 | Unauthorized | Behind auth; may be expected. Note it, don't assume broken. |
| 403 | Forbidden | Often a bot block on external sites. Report as "could not verify." |
| 404 | Not Found | Broken — fix, redirect, or remove the link. |
| 410 | Gone | Permanently removed — remove the link. |
| 429 | Too Many Requests | You're being rate-limited; slow down and retry. Not a real break. |
| 500 | Server Error | Target has problems; retry later before flagging. |
| 502 / 503 | Bad Gateway / Unavailable | Target temporarily down; retry later. |
| Timeout | No response in time | Slow or unreachable — investigate; may be transient. |
| SSL/TLS error | Certificate problem | HTTPS issue on the target. |

## Interpreting external results

- 404 / 410 on an external link → the destination is genuinely gone. Fix on your side.
- 403 / 401 / 429 → very often the site blocking or throttling automated checks, not a real break. Mark "could not verify — check manually."
- 5xx / timeout → retry a couple of times before flagging; transient outages are common.
