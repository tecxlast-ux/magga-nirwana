# Incident Response Runbook

1. Declare incident severity and open an issue in `docs/risk/issue-log.md`.
2. Contain affected segments (disable interfaces/VLANs) while preserving evidence.
3. Collect logs and telemetry snapshots; store outside production network.
4. Eradicate root cause (patch, credential rotation, rule updates).
5. Recover service, verify monitoring/alerts, and run post-mortem with ADR if needed.
