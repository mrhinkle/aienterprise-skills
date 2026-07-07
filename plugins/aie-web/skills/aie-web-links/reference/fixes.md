# Common Link Issues and Fixes

## Broken internal link (404 on your own site)
1. Confirm the target page/route still exists.
2. Check the URL spelling and casing.
3. Update the link, restore the page, or add a redirect.
Time: 2–5 min.

## Mixed content (HTTP asset on an HTTPS page)
1. Find the `http://` script/image/style/font reference.
2. Change it to `https://` or a root-relative path (`/asset.png`).
Time: 5–10 min.

## Redirect chain (A → B → C)
1. Point the original link directly at the final URL.
2. Or change the first redirect to target the final URL in one hop.
Time: 5–15 min.

## Broken external link (404/410)
1. Verify the destination still exists.
2. Update to the new URL, replace with an alternative, or remove.
Time: 5–20 min.

## Orphaned page (exists, nothing links to it)
1. Decide if it's still relevant.
2. Add internal links to it, or delete/redirect it.
3. Exception: intentional landing pages (e.g., a post-signup thank-you) can stay orphaned by design.
Time: 10–30 min.

## Broken anchor link (`#section` with no matching id)
1. Add `id="section"` to the target element, or
2. Correct the link to an existing anchor id.
Time: 2–5 min.

## Malformed email/phone link
1. Fix the `mailto:` address or `tel:` number format.
Time: 2 min.

## Efficiency tips
- Group fixes by page and batch-edit.
- Prefer a redirect map over hand-editing every link to a moved page.
- Re-run the checker after fixing to confirm.
- Schedule a monthly re-check; links break as sites change.
