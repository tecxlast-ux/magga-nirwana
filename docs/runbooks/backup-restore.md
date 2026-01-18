# Backup and Restore Runbook

1. Schedule config exports via `scripts/backup-configs.sh` to secure storage.
2. Sanitize exports with `scripts/sanitize-routeros-export.sh` before committing.
3. Validate backups by restoring to lab devices or virtual appliances monthly.
4. During restore, verify credentials and certificates are rotated post-recovery.
5. Document restoration steps and outcomes in `docs/risk/issue-log.md`.
