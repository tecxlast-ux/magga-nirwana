# Scope

## In scope

- Managed WAN/LAN topology documentation and validation.
- Monitoring stack (Prometheus/Grafana) for latency, packet loss, and device health.
- AI-assisted telemetry normalization and read-only reporting API.
- Identity hygiene for operators including MFA and access tiering.

## Out of scope

- Production secrets storage or key management.
- Write access APIs for configuration changes.
- Vendor-specific automation beyond sanitized configuration exports.

## Non-goals

- Building a custom SIEM; integration points can be documented but not implemented here.
- Hosting production model weights inside the repository.
