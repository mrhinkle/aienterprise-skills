# Uploading to YouTube

Two routes. Pick by how your account is wired.

## Route A — upload by hand (always works)

Drag the MP4 into YouTube Studio, set it **Private**, paste the title, description
and chapters, and attach the thumbnail. Everything before this step in the skill is
platform-independent, so stopping here costs you nothing but a minute.

Do this if you have no API integration, or if the file is large and your upload is
slow enough that you would rather watch a progress bar.

## Route B — upload through a Composio-connected account

The thing that trips people up: `YOUTUBE_MULTIPART_UPLOAD_VIDEO` takes
`videoFile: {name, mimetype, s3key}` where the s3key must reference **Composio's own
storage**. Passing a local path fails with

```
Failed to download file with s3key '/Users/.../edited.mp4': storage returned HTTP 404
```

Browser-automation upload is not an alternative either — those tools cap around
10 MB against a file of hundreds of MB.

So the file has to get into Composio storage first. The reliable way is Google
Drive, because a Drive download through Composio stages the file and hands back a
key as a side effect.

### 1. Copy into the mounted Drive

```bash
D="$DRIVE_MOUNT/_upload-staging"
mkdir -p "$D" && cp edited.mp4 thumb.jpg "$D/"
```

### 2. Read the Drive file id off the file

Do **not** wait for the Drive API to index the upload — it lags by minutes. Drive
for desktop stamps the id as an extended attribute as soon as it registers the file:

```bash
xattr -l "$D/edited.mp4" | grep item-id
# com.google.drivefs.item-id#S: 1AbC…
```

The attribute name carries a `#S` suffix, so `xattr -p com.google.drivefs.item-id`
returns nothing and looks like the file is not synced. Always `xattr -l | grep`.

If the attribute really is missing, the file has not registered yet — wait.

### 3. Stage it into Composio storage

```
GOOGLEDRIVE_DOWNLOAD_FILE  { file_id: "<id>" }   account: "<your drive account alias>"
```

If several Drive accounts are connected the `account` field is required, and the
call errors helpfully if you omit it.

The response's `downloaded_file_content.s3url` is a presigned URL. **The s3key is
the path portion after the bucket host** — everything from the workspace id up to
the object id, without the query string.

### 4. Confirm the staged object is complete

A partially-synced Drive file stages happily and uploads a truncated video. Range-
request one byte and read the total:

```bash
curl -s -r 0-0 -D - -o /dev/null "<s3url>" | grep -i content-range
# content-range: bytes 0-0/251262691   <- must equal the local file size
```

A `HEAD` returns 403; the presign is GET-scoped.

### 5. Upload — private

```
YOUTUBE_MULTIPART_UPLOAD_VIDEO {
  title, description, tags,
  categoryId: "<from webinar.config.md>",
  privacyStatus: "private",
  videoFile: { name, mimetype: "video/mp4", s3key: "<key from step 3>" }
}
```

### 6. Thumbnail

`YOUTUBE_UPDATE_THUMBNAIL` takes a **URL**, not a key — give it the thumbnail's own
`s3url` from its own `GOOGLEDRIVE_DOWNLOAD_FILE` call. JPG/PNG/GIF, under 2 MB,
1280×720. The channel must be phone-verified for custom thumbnails.

Presigned URLs expire in about an hour; re-run step 3 if you were slow.

### 7. Verify, then clean up

```
YOUTUBE_GET_VIDEO_DETAILS_BATCH { id: ["<videoId>"],
  parts: ["snippet","status","contentDetails","processingDetails"] }
```

Check `contentDetails.duration` matches your edit, `hasCustomThumbnail: true`,
`processingDetails.processingStatus: "succeeded"`, and
`status.privacyStatus: "private"`. Then delete the Drive staging copies — they land
in Drive trash, so it is reversible.

## Standing rules

- **Private on upload, every time.** Publishing public is a human decision.
- Report the video id and a `https://youtu.be/<id>` link so it can be reviewed in
  one tap.
- If the thumbnail composites a real person's face into a scene they were never in,
  get their consent before it goes public.
