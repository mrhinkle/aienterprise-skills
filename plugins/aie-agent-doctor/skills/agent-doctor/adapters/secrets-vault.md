# Adapter: secrets-vault

## Config

```yaml
- type: secrets-vault
  config:
    providers: [onepassword, bitwarden]  # one or both
    onepassword:
      required_refs: [...]
    bitwarden:
      status_command: "bw status"
      required_items: [...]
```

## Behavior

1. Per provider: auth/unlock status.
2. Required refs/items reachable (boolean) — no value exfiltration.
3. Flags: `vault:1p unauthenticated`, `vault:bw locked`, `vault:bw missing:agent-openrouter`.

## Non-goals

- Unlocking Bitwarden with a stored password in the pulse
- Dumping `op` item fields into scores JSON
