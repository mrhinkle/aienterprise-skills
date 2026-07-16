# Security and maintenance review

Run this deeper path no more than once per 24 hours unless the user asks for an immediate audit.

## Host security

On macOS, check:

- FileVault, application firewall, Gatekeeper, and System Integrity Protection.
- Automatic checks and installation of security/system-data updates.
- Remote Login, Screen Sharing, Remote Management, and unexpected listening services.
- Sleep, automatic restart after power loss, and power settings relevant to an unattended host.

On Linux, check:

- Full-disk encryption status when observable, firewall policy, unattended security updates, and time synchronization.
- SSH exposure and hardening, including password authentication, root login, authorized keys, and listening interfaces.
- Unexpected listening services and failed-login patterns.
- Service enablement at boot and restart policy for Hermes and Tailscale.

Do not enable, disable, or reconfigure security controls without approval. A remote host can be stranded by a well-intended firewall or SSH change.

## Hermes and secret hygiene

- Locate configuration and secret files without printing their contents.
- Confirm secret files are not world-readable, committed to version control, copied into logs, or passed on command lines where process listings expose them.
- Check logs for accidental token-shaped values and report only masked evidence.
- Confirm the Hermes service runs with the least privilege supported by its installation.
- Confirm logs have bounded retention and correct ownership; do not delete history automatically.

## Exposure review

- Inventory listening ports and map each to its owning process and intended interface.
- Prefer loopback or tailnet-only binding for administrative services.
- Flag public listeners, wildcard binds, or port forwards that are not documented as required.
- Confirm Tailscale does not accidentally advertise routes or an exit node outside the intended design.

## Update review

Check for supported updates to:

- The operating system and security data.
- Tailscale.
- Hermes core and its runtime/package manager.
- Telegram and Slack integrations and their dependencies.

Classify each update as security, patch, minor, major, or migration-bearing. Identify release notes or compatibility evidence before recommending installation.

Default to report-only. Apply an update automatically only when all of these are true:

1. The user or local policy explicitly allows low-risk patch updates.
2. The update requires no reboot, privilege escalation, schema/config migration, or meaningful downtime.
3. Hermes and adapter compatibility is confirmed.
4. A tested rollback path exists.
5. The remote-access path remains available throughout.

Never use force-fix or major-upgrade flags automatically. Never update Hermes, its runtime, or an adapter merely because a package manager reports a newer version.

## Daily review output

Record:

- Security controls: pass, degraded, unknown, or needs approval.
- Exposure findings with process, interface, and port; omit sensitive peer/client data.
- Updates available, risk class, compatibility evidence, rollback, and recommended maintenance window.
- Secret-permission findings with file path and masked evidence only.
- Content-free timestamp of the completed review.
