#!/usr/bin/env bash
# Tested Python aDNA toy chain. Does not call bwa, DeDup, or mapDamage.
set -Ceu
if [ "${1:-}" = "--help" ] || [ $# -lt 2 ]; then
  printf '%s\n' "usage: run_toy_pipeline.sh REF.fa OUTDIR"
  exit 0
fi
REF=$1
OUT=$2
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$OUT"
python3 "$HERE/00_sim_damaged_fastq.py" --ref "$REF" --out-prefix "$OUT/reads" --n-reads 400 --seed 11
python3 "$HERE/01_trim_collapse.py" --r1 "$OUT/reads_R1.fastq" --r2 "$OUT/reads_R2.fastq" --collapsed-fa "$OUT/collapsed.fa"
python3 "$HERE/04_damage_profile.py" --collapsed-fa "$OUT/collapsed.fa" --ref "$REF" --summary-tsv "$OUT/damage.tsv"
python3 "$HERE/06b_make_toy_pileup.py" --collapsed-fa "$OUT/collapsed.fa" --ref "$REF" --pileup-tsv "$OUT/pileup.tsv"
python3 "$HERE/06_pseudohaploid.py" --pileup-tsv "$OUT/pileup.tsv" --calls-tsv "$OUT/pseudo.tsv" --seed 3
mkdir -p "$OUT/tv_test"
python3 "$HERE/06_test_transversions.py" --out-dir "$OUT/tv_test"
python3 "$HERE/07_authentication_summary.py" --damage-tsv "$OUT/damage.tsv" --summary-txt "$OUT/auth_summary.txt"
printf '%s\n' "toy aDNA pipeline finished in $OUT"
