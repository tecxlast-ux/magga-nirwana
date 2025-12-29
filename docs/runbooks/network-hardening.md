# Network Hardening Runbook

1. Apply baseline firewall policies (default deny, allow established/related).
2. Enforce management access lists and limit to jump hosts.
3. Enable logging for drops and forward to centralized collector.
4. Patch firmware per `docs/inventory.md` schedule; document deviations.
5. Rotate credentials and revoke unused accounts quarterly.
