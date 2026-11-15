#!/usr/bin/env bash
# Map aDNA reads with bwa aln.
# Default for collapsed Illumina reads: bwa aln -l 1024 (Schubert et al. 2012);
# do not mix this with the Helicos string or with -n 0.01 -o 2 unless those
# values and their sources are recorded separately (docs/WORKFLOW.md decision 5).
# Existing repository scripts must be quoted verbatim if compared.
# Untested on this box (bwa is not installed).

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "usage: 02_map_adna.sh REF.fa READS.fastq OUT_PREFIX"
  printf '%s\n' "Collapsed (merged) single-end reads:"
  printf '%s\n' "  bwa aln -l 1024 REF.fa collapsed.fastq > OUT.sai"
  printf '%s\n' "  bwa samse REF.fa OUT.sai collapsed.fastq | samtools sort -o OUT.bam"
  printf '%s\n' "  samtools index OUT.bam"
  printf '%s\n' "Unmerged paired reads (choose one and document it):"
  printf '%s\n' "  bwa aln -l 1024 REF.fa R1.fastq > R1.sai"
  printf '%s\n' "  bwa aln -l 1024 REF.fa R2.fastq > R2.sai"
  printf '%s\n' "  bwa sampe REF.fa R1.sai R2.sai R1.fastq R2.fastq | samtools sort -o OUT.bam"
  printf '%s\n' "  or map each mate as single-end after adding DeDup F_/R_ prefixes (see 03_dedup.sh)"
  printf '%s\n' "After mapping: filter MAPQ 25 or 30 (report which) and apply a length filter"
  printf '%s\n' "  (default minimum 30 bp, as in docs/WORKFLOW.md decision 5; AdapterRemoval itself defaults to 15, with the option named --minlength in 2.x and --min-length in 3.x). Example:"
  printf '%s\n' "  samtools view -b -q 25 OUT.bam"
  printf '%s\n' "If comparing with existing repo scripts, quote those scripts verbatim."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
printf '%s\n' "bwa is not invoked automatically in this wrapper; see --help."
exit 3
