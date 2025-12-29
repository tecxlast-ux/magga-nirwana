# Telemetry and data flow

```mermaid
sequenceDiagram
  participant Device
  participant Exporter
  participant Prometheus
  participant AI
  participant Dashboard

  Device->>Exporter: Telemetry (SNMP/ICMP)
  Exporter->>Prometheus: Metrics scrape
  Prometheus->>Dashboard: Visualize metrics
  Prometheus->>AI: Normalized telemetry
  AI-->>Dashboard: Insights/alerts
```

This sequence traces telemetry collection from devices through exporters and
Prometheus into AI enrichment and user-facing dashboards. Keep
`docs/diagrams/data-flow.mmd` in sync with pipeline updates.
