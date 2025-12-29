# Monitoring Operations Runbook

1. Ensure `monitoring/docker-compose.yml` services are running.
2. Sync Prometheus `targets.yaml` from generated topology output.
3. Verify alert rules load without errors and silence expected maintenance windows.
4. Rotate dashboards and data sources using Grafana provisioning files.
5. Record outages and responses in `docs/risk/issue-log.md`.
