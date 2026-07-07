# Reporting & flaky tests

## Results report

```
E2E TEST RUN — {baseURL}
{date} · {browsers/projects run}

RESULT: {passed}/{total} passed   ({failed} failed, {flaky} flaky)

FAILURES
  ✗ {test name}  [{project}]
     Assertion: {what was expected vs got}
     Console/network errors: {captured, if any}
     Repro: {step 1 → step 2 → step where it broke}
     Artifact: {screenshot / trace path}
     Likely cause: {real bug | selector | timing | environment}
     Fix: {concrete next step}

FLAKY (passed on retry)
  ~ {test} — {why it's flaky} → {stabilization}

RECOMMENDATIONS
  1. {highest-impact fix}
  ...

Coverage: {journeys tested} · Gaps: {important flows not yet covered}
```

## Real bug vs flaky

- **Real bug** — fails consistently, assertion is on a genuine user outcome. File it; don't touch the test.
- **Flaky** — passes on retry, or fails only sometimes. Cause is usually a race or a brittle selector. Fix by switching to a role/text selector and letting auto-wait do its job. Do **not** paper over flake with long fixed sleeps or by raising retries indefinitely.
- **Environment** — base URL down, missing test data, expired credentials. Fix the environment, note it, re-run.

## Rules

- Never make a suite pass by deleting or skipping the failing test. A red test that found a real bug is the suite doing its job.
- Every failure ships with a screenshot/trace and repro steps — a failure the developer can't reproduce is half a bug report.
- Track coverage honestly: say which critical journeys are tested and which aren't yet.
- Re-run the suite before every deploy; wire it into CI so it runs on each push (see `setup.md`).
