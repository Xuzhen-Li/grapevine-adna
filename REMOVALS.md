# REMOVALS.md — proposed retirement list (nothing is deleted in this update)

Please check this list before any pull request that would delete files. This update appends material to the existing `README.md`, `README.zh.md`, and `catalog/CATALOG.tsv`; it also adds new teaching files. It does not modify the existing `scripts/02_map_adna.sh` or `scripts/03_dedup.sh`. Every existing line in the README files and the catalogue is unchanged. New wrapper versions are `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh`. The scripts named below remain in the repository until a removal is approved.

File-by-file reads were done on the inventory clone of commit b6e4302e (2026-11-15 17:29 CST), using only `git --no-optional-locks rev-parse` / `ls-files` (no `git status` on that clone). Paths below are repository-relative.

## Two options (either choice is possible; nothing is deleted here)

- **Option A.** Move the three scripts to `scripts/legacy/` and leave a short stub at each old path, labelled “historical, not recommended.” The following cross-references would then need a one-line update or they will break: README.md and README.zh.md around the current L385; `scripts/README.md` L5–7; CATALOG A14; ADDITIONS L60; `notes/cap_test.md` L9 and L19; `docs/04_capture_shotgun_lowcov.md` L23 (alignment reminders that name the generator and `dsdna_preprocess.sh`) and L55 (claim–source table row on those scripts); `docs/04_capture_shotgun_lowcov.zh.md` L9; `SOURCES_READ.tsv` L88; `CHANGELOG.md` L13.
- **Option B.** Keep the three scripts in place and add the same “historical, not recommended” note at the top of each file. **Until a production pipeline is validated, option B is the more conservative choice, and is the recommendation of this update.** The new `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh` are dry-run / help wrappers only; they do not yet replace the old capture-test record. The existing `scripts/02_map_adna.sh` and `scripts/03_dedup.sh` are left byte-identical.

## Keep

| Path | Why |
|---|---|
| `scripts/00_sim_damaged_fastq.py` through `scripts/07_authentication_summary.py`, `scripts/run_toy_pipeline.sh`, `testdata/` | Newly merged toy chain. The scripts README records which steps were tested. The simulator plants only 5-prime C-to-T, so the toy pattern is not a ds, ss, or UDG-treated library. |
| `scripts/run_mapdamage.sh` | Short, generic mapDamage2 wrapper. Line 6 is, verbatim, `mapDamage -i "$BAM" -r "$REF" -d "$OUT" --merge-reference-sequences`. This is the replacement named for the mapDamage step of the old scripts. Still the right thin wrapper for a named step. |
| `scripts/README.md`, `docs/WORKFLOW.md`, `docs/WORKFLOW.zh.md`, the main README files, `catalog/CATALOG.tsv` | Current teaching and workflow text. This update appends a section to the existing README files and appends rows to the existing catalogue; it does not replace existing lines. |
| `notes/cap_test.md`, `notes/mergeBAM.md`, `notes/check_pcrbias.md` | Historical, already desensitised lab notes. They document what was run; they are not proposed as the production protocol. `mergeBAM.md` also records a GATK HaplotypeCaller gVCF loop, which is not the low-coverage route taught in chapter 4. |

## Propose to retire (list only)

| Path | Why retire | What is in place, and what is still missing |
|---|---|---|
| `scripts/adna_capture_pipeline_generator.sh` | Placeholder sample names (`SAMPLE_01`, `SAMPLE_02`, `# ...`). It writes per-sample Slurm scripts with a `cat` heredoc into `./${sample}/${sample}.sh`. AdapterRemoval uses `--minlength 25`, which is not the WORKFLOW default of 30. Mapping is `bwa aln -l 1024 -n 0.01` on collapsed reads only, then Picard `CleanSam` + `MarkDuplicates`, not DeDup. The Slurm partition is the placeholder `<PARTITION>`. The unmerged pair is not mapped. Whether `collapsed.truncated` reads are left unmapped is **[待确认]**. | Teaching coverage: `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh` (help / `--dry-run` documentation only) plus the WORKFLOW decision tree, and `scripts/run_mapdamage.sh` for the mapDamage step. If a new production pipeline uses DeDup, read-name prefixes `M_` / `F_` / `R_` must be documented. **Not replaced:** per-sample Slurm script generation; the AdapterRemoval command and parameters from generator lines 32–44; `@RG` from generator line 56; per-stage flagstat; Qualimap. For production, a rewritten pipeline should be a new validated file rather than an in-place modification of this generator. |
| `scripts/dsdna_preprocess.sh` | The loop variable is misspelt `FLIES` (`ls *_R1.fastq.gz \| sed ...`). Mapping uses `bwa aln -l 1000 -n 0.01`, which disagrees with both the generator (`-l 1024`) and the WORKFLOW note on `-l 1024`. Same Picard MarkDuplicates path as the generator. The script header has `#SBATCH --cpus-per-task=40` (line 5) but uses `35` threads in every step (lines 12–27: AdapterRemoval, bwa, samtools, Qualimap). Hard-coded placeholder partition. There is no opened source for calling this script a “later” addition. | Same replacement path and the same gaps as the generator. If a dsDNA preprocess script is still wanted, write a new file; do not silently “fix” this one in place as part of a deletion. |
| `scripts/collect_mapping_stats.sh` | Placeholder sample list. At the start of each run it truncates `stats.all.tsv` and `stats_debug.log` (shell `>`), then appends. It parses `flagstat` and Qualimap with `grep`/`awk` and uses `head -n 10` to copy file starts into a debug log. The column meaning is fragile if flagstat wording changes. The generator writes `*.collapsed.stats`, but collect reads `*.mapped.stats`, so those fields come out as NA. The `DupReads` column is the number of reads kept after deduplication, not the number of duplicates removed. | A new, tested summary script if one is still needed; or Qualimap/flagstat outputs kept as-is. There is no replacement in the 02/03 wrappers for Qualimap or for the per-stage flagstat record. |

## Not a deletion proposal

Parameters quoted from the old scripts (for example `-l 1024 -n 0.01` versus `-l 1000`, `--minlength 25` versus the WORKFLOW default `30`) are recorded so they are not blended into a new default. The WORKFLOW already warns against mixing script values with literature settings.

`dsdna_preprocess.sh` line 12 uses `--minlength 30`, which matches the WORKFLOW default; the generator uses `--minlength 25`.

No file listed here has been deleted, moved or renamed in this update.
