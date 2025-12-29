# IP Plan

Document subnets, VLANs, and management plane addressing.

## Subnets

- **WAN:** 203.0.113.0/30 (sample)
- **LAN:** 10.10.0.0/16 segmented by site
- **Management:** 10.255.0.0/24 isolated from user traffic

## VLANs

- VLAN 10 – User LAN
- VLAN 20 – Voice/IoT
- VLAN 99 – Management

## Management access

- SSH/HTTPS restricted to management VLAN.
- SNMP read-only communities mapped to monitoring hosts.
