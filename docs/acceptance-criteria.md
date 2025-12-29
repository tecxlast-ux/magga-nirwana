# Acceptance Criteria

## Phase gates

- **Repository Foundation (M0)**
  - Required files present (`LICENSE`, `README.md`, `SECURITY.md`, `.editorconfig`).
  - Scope, risk register, and ADR process documented.
- **Topology Ready (M1)**
  - `topology/topology.yaml` validated by `scripts/validate-topology.py`.
  - Sample topology provided for reference.
- **Monitoring Ready (M2)**
  - `monitoring/docker-compose.yml` starts Prometheus and Grafana without errors.
  - Prometheus targets generated from topology and rules loaded.
- **AI Normalizer/API Ready (M3)**
  - Schemas validated against example payloads.
  - `ai/api/openapi.yaml` reviewed and published as read-only contract.
- **Identity Ready (M4)**
  - Account inventory template filled, MFA policy approved, migration plan documented.

## Definition of Done (per item)

- Documentation updated with links to ADRs where decisions exist.
- Risks logged or updated in `docs/risk/risk-register.md`.
- Tests or validation scripts executed where applicable.
