# Security Headers Reference

These HTTP response headers tell the browser how to handle your site safely. Set them at your host/CDN, reverse proxy, or framework middleware — the mechanism differs by stack, the header names and values do not.

Verify what a deployed site actually sends with:

```bash
curl -sI https://example.com | grep -iE 'content-security-policy|strict-transport|x-content-type|x-frame|referrer-policy|permissions-policy'
```

## Content-Security-Policy (CSP)

Restricts where scripts, styles, and other resources may load from — the strongest defense against XSS. Start restrictive and loosen only as needed. Avoid `'unsafe-inline'` for scripts where possible; prefer nonces or hashes.

```
Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'self'
```

## Strict-Transport-Security (HSTS)

Forces HTTPS for future visits. Only enable once HTTPS is fully working.

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

## X-Content-Type-Options

Stops the browser from MIME-sniffing responses.

```
X-Content-Type-Options: nosniff
```

## X-Frame-Options / frame-ancestors

Prevents clickjacking via iframing. `frame-ancestors` in CSP supersedes this for modern browsers; set both for coverage.

```
X-Frame-Options: DENY
```

## Referrer-Policy

Limits how much URL information leaks on outbound navigation.

```
Referrer-Policy: strict-origin-when-cross-origin
```

## Permissions-Policy

Denies powerful features unless the site needs them.

```
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## Example: static-host config (JSON style)

Many static hosts accept a config file with a headers array. The shape below is representative; adapt keys to your host's schema.

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Content-Security-Policy", "value": "default-src 'self'; frame-ancestors 'none'" },
        { "key": "Strict-Transport-Security", "value": "max-age=31536000; includeSubDomains" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" },
        { "key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()" }
      ]
    }
  ]
}
```

## Example: Nginx

```nginx
add_header Content-Security-Policy "default-src 'self'; frame-ancestors 'none'" always;
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
```

## Subresource Integrity (SRI)

For third-party scripts loaded from a CDN, pin the version and add an integrity hash so a tampered file is rejected.

```html
<script
  src="https://cdn.example.com/lib@3.0.0/dist/lib.min.js"
  integrity="sha384-…"
  crossorigin="anonymous"></script>
```

## Reference

- OWASP Secure Headers Project — https://owasp.org/www-project-secure-headers/
- MDN CSP — https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- MDN Strict-Transport-Security — https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
