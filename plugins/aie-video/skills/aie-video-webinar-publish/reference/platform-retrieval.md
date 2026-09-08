# Getting the MP4 off the webinar platform

The recording is almost never where the API suggests it should be. Budget a few
minutes for this and check the file before editing it.

## The general shape of the problem

Live webinar platforms treat the recording as a *replay experience*, not a file.
So you typically get:

- an API that lists webinars, registrants and stats but has **no recordings
  endpoint**;
- a replay URL that works only inside a replay window and then redirects to an
  "expired" page;
- an actual download link buried in the UI, often per-session rather than
  per-webinar.

Look for the per-session link. It is usually a plain CDN URL you can `curl` with no
auth once you have it.

## WebinarJam

Credentials live in the app under **Webinars → the webinar → Advanced → API custom
integration** (Member ID, Webinar ID, Webinar Hash, API Key). Put the key in the
environment; never commit it.

```bash
# list webinars: ids, hashes, names, schedules
curl -s -X POST https://api.webinarjam.com/webinarjam/webinars \
  -d "api_key=$WEBINARJAM_API_KEY"

# one webinar's detail (presenters, registration + replay URLs)
curl -s -X POST https://api.webinarjam.com/webinarjam/webinar \
  -d "api_key=$WEBINARJAM_API_KEY" -d "webinar_id=<id>"
```

**There is no recordings endpoint.** The payload's `direct_replay_room_url`
redirects to `/expired/<hash>` once the replay window closes, so it is useless
after the fact.

The MP4 is in the UI, per session:

> **Webinars → the webinar row → "Your links" → Replay tab → select the session**

That reveals a CDN link of the form
`https://<cdn-host>/u<member_id>/<file-id>.mp4` plus a download button. Fetch it
with plain `curl`; no auth headers needed. An hour of 1080p25 runs 250–350 MB.

Two traps:

- **Do not click "Edit"** looking for the recording — that opens the live webinar
  configuration wizard and risks changing settings on a real event.
- **Analytics does not have it.** Analytics gives attendance and session length,
  which is useful for sanity-checking the download, but no media.

Worth grabbing while you are in the API: `presenters[].name` and
`presenters[].picture`. Those are real, presenter-supplied headshots — the right
source for a thumbnail face. They are often small (300px), so ask the guest for a
full-resolution photo if you plan to run their face large.

## Zoom

Cloud recordings *are* in the API (`/meetings/{meetingId}/recordings`) and the
`download_url` needs an OAuth token or a `?access_token=` query parameter. The
gotcha is retention: cloud recordings expire on a plan-dependent schedule, so pull
them promptly.

## StreamYard / Riverside / Restream

These are recording-first tools and expose a normal download in the UI. Prefer the
highest-quality local/ISO recording over the streamed composite if one exists — the
streamed version is bitrate-limited by the live broadcast.

## Before you edit

```bash
ffprobe -v error -show_entries format=duration \
  -show_entries stream=codec_name,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 raw.mp4
```

Compare the duration against the session length the platform reports. A mismatch
means a partial download — re-fetch rather than edit a truncated file.
