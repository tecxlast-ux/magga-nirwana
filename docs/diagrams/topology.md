# Network topology

```mermaid
flowchart LR
  WAN((WAN)) --> Edge[Edge Router]
  Edge --> Switch[Core Switch]
  Switch --> AP1[Access Point]
  Switch --> Server[Mgmt/Monitoring]
```

The topology diagram reflects WAN ingress to the edge router, core switching,
and downstream access/management segments. Update `docs/diagrams/topology.mmd`
when device roles or links change.
