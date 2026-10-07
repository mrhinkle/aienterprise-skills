# Adapter: composio-connections

## Config

```yaml
- type: composio-connections
  config:
    required_toolkits:
      - name: gmail
      - name: slack
      - name: github
```

## Behavior

1. For each toolkit slug, call connection list/status (Composio `COMPOSIO_MANAGE_CONNECTIONS` action=`list`, or equivalent REST).
2. Map: Active → ok; missing/expired/needsAuth → flags `composio:<slug> <status>`.
3. Pillars: Availability (primary), Config hygiene (secondary for needsAuth).

## Non-goals

- Creating auth links
- Executing Gmail/Slack/GitHub tools as a probe
