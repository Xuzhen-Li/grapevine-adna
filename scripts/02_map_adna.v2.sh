#!/usr/bin/env bash
# Map aDNA reads with bwa aln.
# Default for collapsed Illumina reads: bwa aln -l 1024 (Schubert et al. 2012,
# PMC3468387 full text opened 2026-11-15 CST: "the seed was disabled in the
# optimized set of mapping parameters (−l 1024)").
# do not mix this with the Helicos string or with -n 0.01 -o 2 unless those
# values and their sources are recorded separately (docs/WORKFLOW.md decision 5).
# Schubert 2012 also states that BWA's "-n option" has "a default value of 0.04".
# Existing repository scripts must be quoted verbatim if compared.
# Untested in this environment (`bwa` is not installed).
# This file is scripts/02_map_adna.v2.sh. The live scripts/02_map_adna.sh is
# unchanged in this addition.
#
# AdapterRemoval length default and option names, opened 2026-11-15 CST:
# v2.3.4 man page (AdapterRemoval.1, 19,302 bytes): "--minlength length"
# "Reads shorter than this length are discarded following trimming. Defaults to 15."
# 3.0.2 manpage https://adapterremoval.readthedocs.io/en/v3.0.2/manpage.html
# (first opened 2026-11-15 CST, 73,940 bytes, sha256
# 72a82265279c2d81736b4da77e99fe0c0ae2ee5759212ff2f99ccce831ee74ae):
# "--min-length" with the same "Defaults to 15." sentence. The page recorded
# on 2026-11-15 CST as “latest” (73,938 bytes, sha256 cd3ac4e7…) has
# the HTML title “AdapterRemoval 3.0.2 documentation”.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "usage: 02_map_adna.v2.sh REF.fa READS.fastq OUT_PREFIX"
  printf '%s\n' "Collapsed (merged) single-end reads:"
  printf '%s\n' "  bwa aln -l 1024 REF.fa collapsed.fastq > OUT.sai"
  printf '%s\n' "  bwa samse REF.fa OUT.sai collapsed.fastq | samtools sort -o OUT.bam"
  printf '%s\n' "  samtools index OUT.bam"
  printf '%s\n' "Unmerged paired reads (choose one and document it):"
  printf '%s\n' "  bwa aln -l 1024 REF.fa R1.fastq > R1.sai"
  printf '%s\n' "  bwa aln -l 1024 REF.fa R2.fastq > R2.sai"
  printf '%s\n' "  bwa sampe REF.fa R1.sai R2.sai R1.fastq R2.fastq | samtools sort -o OUT.bam"
  printf '%s\n' "  or map each mate as single-end after adding DeDup F_/R_ prefixes (see 03_dedup.v2.sh)"
  printf '%s\n' "After mapping: filter MAPQ 25 or 30 (report which) and apply a length filter"
  printf '%s\n' "  (default minimum 30 bp, as in docs/WORKFLOW.md decision 5; AdapterRemoval itself defaults to 15, with the option named --minlength in 2.3.4 and --min-length in 3.0.2; see the header comment for the man pages opened 2026-11-15 CST). Example:"
  printf '%s\n' "  samtools view -b -q 25 OUT.bam"
  printf '%s\n' "If comparing with existing repo scripts, quote those scripts verbatim."
  printf '%s\n' "--dry-run prints this help text only; it does not run bwa or a command pipeline."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
printf '%s\n' "bwa is not invoked automatically in this wrapper; see --help."
exit 3
