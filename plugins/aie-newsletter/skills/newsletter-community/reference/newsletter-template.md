# {{ newsletter_title }}

*{{ subtitle }}*

<!-- If editions.community.hero_image is set: -->
![{{ publication_name }} logo]({{ hero_image }})

<!-- If editions.community.mission_tagline is set: -->
*{{ mission_tagline }}*

{{ opening_content }}

---

<!-- Only if editions.community.promo_block.enabled -->
## {{ promo_heading }}

**{{ promo_event_line }}**

* **{{ option_name }} — {{ price }} — {{ date }}.** {{ option_description }}
* **{{ option_name }} — {{ price }} — {{ date }}.** {{ option_description }}

*{{ promo_footnote }}*

**[{{ promo_cta_label }} →]({{ promo_cta_url }})**

---

## {{ feature_article_title }}

![{{ feature_article_image_alt }}]({{ feature_article_image_path }})

{{ feature_article_content }}

---

## {{ secondary_article_title }}

![{{ secondary_article_image_alt }}]({{ secondary_article_image_path }})

{{ secondary_article_content }}

---

## Upcoming Events

![Upcoming events]({{ events_image_path }})

{{ upcoming_events_list }}

---

{{ sign_off }}
