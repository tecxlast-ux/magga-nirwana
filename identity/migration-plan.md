# Identity Migration Plan

1. Audit existing accounts and map to `account-inventory.template.md`.
2. Enforce MFA for all administrative roles with hardware tokens.
3. Migrate legacy accounts to tiered access groups (read-only, operator, admin).
4. Validate recovery flows and break-glass accounts.
5. Decommission legacy accounts and document in `checklists/decommission-legacy.md`.
