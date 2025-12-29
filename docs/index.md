# Private AI Secure Network Documentation

Welcome to the public documentation site for the Private AI Secure Network.
This site consolidates all planning, topology, monitoring, and operational
guidance into a single, easy-to-browse reference.

## Getting started

- Review the project tracking board to see current milestones and owners in context.
- Confirm scope, acceptance criteria, and non-goals before provisioning hardware or services.
- Follow the IP plan and inventory to keep device roles, firmware, and addressing aligned.

## Navigation highlights

- **Project delivery**: [Project tracking](project-tracking.md), [Scope](scope.md),
  [Acceptance criteria](acceptance-criteria.md)
- **Operational runbooks**: [Network hardening](runbooks/network-hardening.md),
  [Monitoring operations](runbooks/monitoring-operations.md),
  [Incident response](runbooks/incident-response.md),
  [Backup & restore](runbooks/backup-restore.md)
- **Architecture**: [Inventory](inventory.md), [IP plan](ip-plan.md),
  [Topology diagram](diagrams/topology.md), [Data flow](diagrams/data-flow.md)
- **Governance**: [ADR guide](decisions/README.md), [ADR template](decisions/adr-template.md),
  [Risk register](risk/risk-register.md), [Issue log](risk/issue-log.md)

## Related repositories and folders

- **Topology source of truth**: maintain `topology/topology.yaml` and examples under `topology/samples/`.
- **Monitoring stack**: deploy from `monitoring/docker-compose.yml` with Prometheus, Grafana, and alerting rules.
- **AI telemetry and redaction**: schemas, examples, and prompts live under `ai/` with runtime configs in `ai/runtime/`.
- **Identity and access**: follow checklists and policies in `identity/` to keep administrative accounts controlled.
- **Sanitized configs**: store scrubbed device exports in `configs/` only—never commit secrets.

## Preview locally

1. Install MkDocs: `pip install mkdocs`
2. Serve locally: `mkdocs serve`
3. Open `http://127.0.0.1:8000` in a browser to preview the site.

For production, the site is built automatically from the main branch via GitHub Pages.
