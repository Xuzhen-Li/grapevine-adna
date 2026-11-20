#!/usr/bin/env bash
# Document DeDup for collapsed single-end aDNA reads (docs/WORKFLOW.md).
# Do not overwrite scripts/run_mapdamage.sh or other existing scripts.
# Untested in this environment.
# Citation: Peltzer et al. 2016 Genome Biology, doi:10.1186/s13059-016-0918-z
# (EAGER; DeDup is introduced there for merged paired-end reads).
# Code: https://github.com/apeltzer/DeDup
# This file is scripts/03_dedup.v2.sh. The live scripts/03_dedup.sh is
# unchanged in this addition.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "usage: 03_dedup.v2.sh IN.bam OUT.bam"
  printf '%s\n' "Documented default: DeDup on collapsed reads; report MAPQ 25 or 30."
  printf '%s\n' "Picard MarkDuplicates is not the default for collapsed SE aDNA reads."
  printf '%s\n' "DeDup requires read-name prefixes:"
  printf '%s\n' "  M_  merged / collapsed reads (deduplicated by both ends)"
  printf '%s\n' "  F_  forward unmerged mate (deduplicated by one end)"
  printf '%s\n' "  R_  reverse unmerged mate (deduplicated by one end)"
  printf '%s\n' "AdapterRemovalFixPrefix can add these prefixes after AdapterRemoval."
  printf '%s\n' "DeDup is not designed for plain single-end data. Using --merged on"
  printf '%s\n' "unprefixed SE reads can leave duplicates. Decide and document a"
  printf '%s\n' "strategy for unmerged pairs before running DeDup."
  printf '%s\n' "Citation: Peltzer et al. 2016 Genome Biology 10.1186/s13059-016-0918-z"
  printf '%s\n' "--dry-run prints this help text only; it does not run DeDup or a command pipeline."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
printf '%s\n' "DeDup is not invoked automatically in this wrapper; see --help."
exit 3
