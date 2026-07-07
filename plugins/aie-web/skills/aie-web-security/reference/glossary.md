# Plain-Language Security Glossary

**API key** — A secret credential that lets your code use a service. Treat it like a password; never ship it to the browser or commit it.

**Secret** — Any credential: API key, token, database URL, private key, password.

**XSS (Cross-Site Scripting)** — An attacker gets malicious script to run in your visitors' browsers, usually via unescaped input. Defense: escape output, avoid `innerHTML`, use a Content-Security-Policy.

**CSRF (Cross-Site Request Forgery)** — An attacker tricks a logged-in user's browser into making a state-changing request. Defense: anti-CSRF tokens and `SameSite` cookies.

**HTTPS / TLS** — Encrypts data between browser and server so it can't be read in transit.

**CSP (Content-Security-Policy)** — Browser rules for which scripts and resources are allowed to load.

**HSTS** — A header that forces browsers to use HTTPS for your site going forward.

**SRI (Subresource Integrity)** — A hash on a third-party script tag; if the file is modified, the browser refuses to run it.

**CORS** — Rules controlling which other websites may call your API from a browser.

**Mixed content** — Loading an insecure `http://` resource on a secure `https://` page; browsers block or warn.

**Vulnerability** — A flaw an attacker can exploit.

**CVE** — A public numbered ID for a known vulnerability (e.g., CVE-2024-1234).

**Honeypot** — A hidden form field real users never fill; if it's filled, the submission is almost certainly a bot.
