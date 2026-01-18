# Monitoring Stack

This directory holds Prometheus, Grafana, and exporters used to observe the Private AI Secure Network.

- `docker-compose.yml` brings up Prometheus, Grafana, Alertmanager, and Blackbox exporter.
- `prometheus/` contains scrape configuration, alert rules, and generated targets.
- `grafana/` stores provisioning files and example dashboards.
- `exporters/` houses SNMP and Blackbox exporter configuration references.
