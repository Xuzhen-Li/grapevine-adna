#!/usr/bin/env bash
# Document plant-applicable contamination checks. Do not run hapCon.
# Untested beyond --help / --dry-run.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "In a viticulture institute, modern grape DNA is the primary contamination"
  printf '%s\n' "hazard, not only human DNA (docs/WORKFLOW.md decision 2)."
  printf '%s\n' "Do not use hapCon or other human X-chromosome contamination modules on grape."
  printf '%s\n' "AuthentiCT is for single-stranded libraries only, not UDG-treated or PMD-filtered data."
  printf '%s\n' "Documented checks: sequence blanks; compare PCA or f-statistics before and after PMD filtering."
  printf '%s\n' "A clear shift of the sample on PCA or in f-statistics after PMD filtering"
  printf '%s\n' "suggests modern DNA contamination."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
exit 3
