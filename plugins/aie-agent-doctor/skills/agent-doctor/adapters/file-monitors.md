# Adapter: file-monitors (default)

Reads paths listed under `monitors[]` / adapter config. Expected JSON shapes are site-defined; map common keys:

- `ok` / `status` / `rejected` → Availability
- `failed_jobs` / `paused` → Job reliability
- `quota` / `429` → Model/quota
- `invalid_json` → −10 monitor artifact deduction

Does not spawn probes.
