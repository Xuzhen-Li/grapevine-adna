#!/usr/bin/env bash
# Generic mapDamage2 run for aDNA damage assessment.
# Usage: bash run_mapdamage.sh <REF> <BAM> <OUT_DIR>
set -euo pipefail
REF="$1"; BAM="$2"; OUT="${3:-mapdamage_out}"
mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences
