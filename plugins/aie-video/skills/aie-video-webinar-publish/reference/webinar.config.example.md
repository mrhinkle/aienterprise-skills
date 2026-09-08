# webinar.config.md (example)

Copy this file to `webinar.config.md` next to the skill (or into your project) and
fill it in. The skill reads it for everything channel- and brand-specific so the
instructions stay generic.

## Channel

```yaml
platform: youtube
channel_name: Your Channel
channel_id: UC…                     # from YouTube Studio → Settings → Channel → Advanced
channel_handle: "@yourhandle"
default_privacy: private            # always upload private; a human publishes
default_category_id: "28"           # 28 = Science & Technology
```

## Webinar platform

```yaml
webinar_platform: webinarjam        # webinarjam | zoom | streamyard | riverside | other
member_id: "<your member id>"       # WebinarJam: Advanced → API custom integration
api_key_env: WEBINARJAM_API_KEY     # store the key in the environment, never here
event_slug: "<your event slug>"     # the path segment in your public event URLs
```

## Transcription

```yaml
asr: elevenlabs_scribe              # must be a VERBATIM ASR; Whisper deletes fillers
asr_key_env: ELEVENLABS_API_KEY
```

## Editing defaults

```yaml
filler_words: [um, umm, uh, uhh, er, erm, ah, eh, hm, hmm, mm]
never_cut: [like, you know, basically, actually, literally, right]
expected_removal_rate: 0.6-0.7      # anything near 1.0 means it is cutting speech
max_word_loss_pct: 1.0              # verification fails above this
```

## Brand (thumbnail + graphics)

```yaml
brand_name: Your Brand
colors:
  background: "#000000"
  primary: "#2F6FE0"                # the highlight word's colour
  accent: "#F08A3C"
  text: "#FFFFFF"
fonts:
  display: /path/to/YourDisplay.ttf
  body: /path/to/YourBody.ttf
logo: /path/to/logo.png
typography_notes: >
  Any house rules — e.g. "sentence case only, no bold weights, colour carries
  emphasis" — go here so the thumbnail pass respects them.
```

## Staging (only if uploading through Composio)

```yaml
staging: google_drive
drive_account_alias: "Your Drive Account"   # the alias Composio shows for the account
drive_mount: ~/Library/CloudStorage/GoogleDrive-<you>/My Drive
staging_folder: _upload-staging
youtube_account_alias: "<your composio youtube account>"
```

## Consent

```yaml
require_guest_consent_for_composite_thumbnails: true
```

Set this true if your thumbnails ever place a real person's face into a scene they
were not photographed in. The skill will flag it before anything goes public.
