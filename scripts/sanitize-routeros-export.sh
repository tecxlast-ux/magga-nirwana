#!/usr/bin/env bash
set -euo pipefail

INPUT=${1:-export.rsc}
OUTPUT=${2:-export.sanitized.rsc}

grep -v "(password|secret)" "$INPUT" > "$OUTPUT"
echo "Sanitized export written to $OUTPUT"
