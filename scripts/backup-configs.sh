#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR=${1:-backups}
mkdir -p "$BACKUP_DIR"

echo "Collecting RouterOS configs..."
# Placeholder: replace with device-specific fetch commands
cp configs/routeros/hex/export.sanitized.rsc "$BACKUP_DIR/hex.rsc"
cp configs/routeros/l009/export.sanitized.rsc "$BACKUP_DIR/l009.rsc"

echo "Backups stored in $BACKUP_DIR"
