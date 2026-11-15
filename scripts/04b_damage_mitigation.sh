#!/usr/bin/env bash
# Document damage mitigation after profiling, by library type and UDG treatment
# (docs/WORKFLOW.md decision 6). Untested on this box.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "usage: 04b_damage_mitigation.sh --library ds|ss --udg none|half|full IN.bam OUT"
  printf '%s\n' "Documented defaults from docs/WORKFLOW.md; none of these values is newly invented:"
  printf '%s\n' "  --udg half : trimBam, 2 nt from each end (or an equivalent trim)."
  printf '%s\n' "  --udg none : a longer trim, quality rescaling with mapDamage2, and/or"
  printf '%s\n' "               PMDtools filtering; consider restricting later calls to transversions."
  printf '%s\n' "  --udg full : UDG does not remove thymines from methylated cytosines in plant"
  printf '%s\n' "               CG, CHG or CHH contexts; residual C-to-T still needs caution."
  printf '%s\n' "  --library ss : later genotyping with pileupCaller --singleStrandMode."
  printf '%s\n' "  --library ds : 5-prime C-to-T and 3-prime G-to-A are expected on non-UDG data."
  printf '%s\n' "Choose and record one route; this wrapper does not run the tools."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
exit 3
