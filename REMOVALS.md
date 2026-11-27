# REMOVALS.md — files removed from this repository

The three capture-test scripts named below have been removed from the tree. `scripts/02_map_adna.sh` and `scripts/03_dedup.sh` are unchanged. The help / `--dry-run` wrappers `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh` remain. `scripts/run_mapdamage.sh` remains.

## Removed

| Path | Why it was removed | What remains |
|---|---|---|
| `scripts/adna_capture_pipeline_generator.sh` | Placeholder sample names (`SAMPLE_01`, `SAMPLE_02`). It wrote per-sample Slurm scripts with a `cat` heredoc into `./${sample}/${sample}.sh`. AdapterRemoval used `--minlength 25`, which is not the WORKFLOW default of 30. Mapping was `bwa aln -l 1024 -n 0.01` on collapsed reads only, then Picard `CleanSam` + `MarkDuplicates`, not DeDup. The Slurm partition was the placeholder `<PARTITION>`. The unmerged pair was not mapped. Whether `collapsed.truncated` reads were left unmapped remains **[待确认]**. | Teaching coverage: `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh` (help / `--dry-run` documentation only) plus the WORKFLOW decision tree, and `scripts/run_mapdamage.sh` for the mapDamage step. If a new production pipeline uses DeDup, read-name prefixes `M_` / `F_` / `R_` must be documented. Still not replaced: per-sample Slurm script generation; the AdapterRemoval command and parameters from the former generator; `@RG`; per-stage flagstat; Qualimap. A production pipeline should be a new validated file. |
| `scripts/dsdna_preprocess.sh` | The loop variable was misspelt `FLIES`. Mapping used `bwa aln -l 1000 -n 0.01`, which disagrees with both the former generator (`-l 1024`) and the WORKFLOW note on `-l 1024`. Same Picard MarkDuplicates path as the former generator. The script header had `#SBATCH --cpus-per-task=40` but used 35 threads in every step. Hard-coded placeholder partition. | Same remaining coverage and the same gaps as the former generator. If a dsDNA preprocess script is still wanted, write a new file. |
| `scripts/collect_mapping_stats.sh` | Placeholder sample list. At the start of each run it truncated `stats.all.tsv` and `stats_debug.log`, then appended. It parsed `flagstat` and Qualimap with `grep`/`awk`. The column meaning is fragile if flagstat wording changes. The former generator wrote `*.collapsed.stats`, but this script read `*.mapped.stats`, so those fields came out as NA. The `DupReads` column was the number of reads kept after deduplication, not the number of duplicates removed. | A new, tested summary script if one is still needed; or Qualimap/flagstat outputs kept as-is. The 02/03 wrappers do not replace Qualimap or the per-stage flagstat record. |

## Still in the repository

| Path | Why |
|---|---|
| `scripts/00_sim_damaged_fastq.py` through `scripts/07_authentication_summary.py`, `scripts/run_toy_pipeline.sh`, `testdata/` | Toy chain. The scripts README records which steps were tested. The simulator plants only 5-prime C-to-T, so the toy pattern is not a ds, ss, or UDG-treated library. |
| `scripts/run_mapdamage.sh` | Short, generic mapDamage2 wrapper. Line 6 is, verbatim, `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`. |
| `scripts/README.md`, `docs/WORKFLOW.md`, `docs/WORKFLOW.zh.md`, the main README files, `catalog/CATALOG.tsv` | Current teaching and workflow text. |
| `notes/cap_test.md`, `notes/mergeBAM.md`, `notes/check_pcrbias.md` | Historical, already desensitised lab notes. They document what was run; they are not the production protocol. `mergeBAM.md` also records a GATK HaplotypeCaller gVCF loop, which is not the low-coverage route taught in chapter 4. |

## Parameters recorded from the removed scripts

Parameters quoted from those scripts (for example `-l 1024 -n 0.01` versus `-l 1000`, `--minlength 25` versus the WORKFLOW default `30`) are recorded so they are not blended into a new default. The WORKFLOW already warns against mixing script values with literature settings.

The removed dsDNA preprocess script used `--minlength 30` at line 12, which matches the WORKFLOW default; the removed generator used `--minlength 25`.
