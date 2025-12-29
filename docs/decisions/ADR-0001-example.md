# ADR-0001: Use Prometheus and Grafana for Monitoring

- Status: Accepted
- Date: 2024-01-01

## Context

We need an open-source monitoring stack that integrates with network devices and supports custom alerting.

## Decision

Adopt Prometheus for metrics collection with Blackbox and SNMP exporters, and Grafana for dashboards.

## Consequences

- Pros: Rich community support, flexible alerting, easy dashboarding.
- Cons: Requires ongoing maintenance and storage planning.

## Alternatives considered

- Commercial NMS suite
- Self-built telemetry database
