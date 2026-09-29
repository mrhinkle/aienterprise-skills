# Community newsletter — social posts

When the user asks for LinkedIn or other social posts from an edition:

- Hashtags follow `metadata.linkedin_hashtags` (default: none).
- Lead with a provocative hook or a value statement, not "Our new newsletter is
  out."
- Include the details a reader needs to act: every workshop or session, prices,
  dates, and the link.
- Close with a clear call to action. If `editions.community.reshare_ask` is set,
  end with it.
- No tables.
- If `images.skill` is set, generate a 1:1 square image for the post.
- Run the `ai-slop-killer` pass and the banned-word check on each post.
