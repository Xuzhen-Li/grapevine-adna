# scripts (new files)

These files are **added** alongside the existing capture scripts. This update does not modify:

- `adna_capture_pipeline_generator.sh`
- `collect_mapping_stats.sh`
- `dsdna_preprocess.sh`
- `run_mapdamage.sh`

or any file under `notes/`. If a published parameter string is compared against those scripts, quote the existing script values verbatim. Citations for production tools are in the README catalogue rows. DeDup is described in Peltzer et al. 2016 Genome Biology (doi:10.1186/s13059-016-0918-z).

The Python toy chain starts from `testdata/toy_ref.fa` (a 2 kb random sequence, not ancient grape data):

```bash
bash scripts/run_toy_pipeline.sh testdata/toy_ref.fa OUTDIR
```

The simulator plants only 5-prime C-to-T damage, so the toy damage pattern does not represent a double-stranded, single-stranded, or UDG-treated library.

| File | Purpose | Tested? |
|------|---------|---------|
| `00_sim_damaged_fastq.py` | Simulate paired reads with 5-prime C-to-T damage only | Yes |
| `01_trim_collapse.py` | Collapse overlapping toy pairs; default minimum length 30; count R1/R2 disagreements | Yes |
| `02_map_adna.sh` | Document `bwa aln -l 1024` for collapsed and unmerged reads, plus sort, MAPQ and length filters. Length 30 bp is WORKFLOW decision 5, not the AdapterRemoval default (15; `--minlength` in 2.x, `--min-length` in 3.x). Do not mix in `-n` / `-o` values that remain [待确认] in `docs/WORKFLOW.md`. | No, `--dry-run` exits 2 |
| `03_dedup.sh` | Document DeDup on collapsed reads, including M_/F_/R_ prefixes; MAPQ 25 or 30 | No, `--dry-run` exits 2 |
| `04_damage_profile.py` | Toy 5-prime C-to-T counter; not mapDamage2 | Yes |
| `04b_damage_mitigation.sh` | Document trim/rescale/PMD steps by `--library` and `--udg` | No, `--dry-run` exits 2 |
| `05_contamination_checks.sh` | Reminders: modern grape DNA is the main hazard; no hapCon; AuthentiCT only for untreated ss libraries; sequence blanks; PCA or f-statistics before and after PMD filtering | No, `--dry-run` exits 2 |
| `06b_make_toy_pileup.py` | Build a toy pileup from exact placements | Yes |
| `06_pseudohaploid.py` | Random-draw pseudo-haploid calls; `--transversions-only` skips transition sites using `--alleles-tsv`, and keeps alt reads at transversion sites; `--ref` requires `--alleles-tsv`; not a heterozygosity estimate | Yes (defaults off, same toy behaviour) |
| `06_test_transversions.py` | Site-level transversion test: transitions skipped; alt reads kept; off-panel bases, missing sites, A/G, multiallelic, ref mismatch, ref==alt, N/indel, `--ref` without a panel, duplicate rows, and unchanged default path | Yes |
| `07_authentication_summary.py` | Restate toy counts; does not declare a sample authentic | Yes |
| `run_toy_pipeline.sh` | Driver for the tested Python scripts only | Yes |

Mixture-test numerical thresholds remain [待确认]; this code does not invent them.
