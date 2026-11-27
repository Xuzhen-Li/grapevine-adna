# Changelog

This is the public summary of changes to the teaching files in `grapevine-adna`. Detailed logs are not part of this repository.

## 2026-11-27

- Removed an earlier catalogue snapshot, the earlier short checksum list, and three capture-test scripts. The record of those scripts is in `REMOVALS.md`. The remaining checksum manifest is `SHA256SUMS.v2`. Pointers in the README files, chapter 4, `scripts/README.md`, `catalog/CATALOG.tsv`, and `notes/cap_test.md` were updated so they no longer treat those files as present.

## 2026-11-15 — teaching chapters and catalogue errata

- Additive only: the existing `scripts/02_map_adna.sh` and `scripts/03_dedup.sh` are not shipped in this tree and are not modified. New help / `--dry-run` wrappers are `scripts/02_map_adna.v2.sh` and `scripts/03_dedup.v2.sh`. The existing README.md, README.zh.md and catalog/CATALOG.tsv are included starting from commit b6e4302e, with new material appended; every existing line is unchanged.
- Short earlier README titles and a dead earlier changes-file link are not used. New teaching files are listed in an appended README section and in this changelog. That earlier changes file is not part of this tree.
- schmutzi: wording follows the official README Nuclear section (contDeam can be used on nuclear data at the user’s own risk under the listed conditions; DICE is recommended for nuclear samples; default candidate library of 197 human mitogenomes). Chapters, F2 and an appended catalogue erratum replace the old “not a grape nuclear contamination tool” teaching; the existing A10 row itself is not edited.
- KIN `-N 22` is cited verbatim from the KIN README under “Running KINgaroo” (“N: Total number of chromosome pairs. Default=22”), not as a KIN parameter and not as an unsourced “human autosome” fact. Grape 19 chromosome sequences (chr01–chr19, plus chr00) are cited from Canaguier et al. 2017 (PMC5612791). Setting `-N 19` remains a repository judgement [待确认] as a Vitis tool default.
- AdapterRemoval’s length default of 15 and the 2.3.4 `--minlength` / 3.0.2 `--min-length` option names are taken from the v2.3.4 man page and the 3.0.2 manpage (https://adapterremoval.readthedocs.io/en/v3.0.2/manpage.html), and are documented in `scripts/02_map_adna.v2.sh` and chapter 4.
- mapDamage quality-score rescaling is cited from the Jónsson et al. 2013 abstract, not from the README. The mapDamage wrapper comparison in chapter 2 is to `scripts/run_mapdamage.sh` line 6. A DamageProfiler row was added to the chapter 2 claim–source table.
- Schubert et al. 2012 full text (PMC3468387) is the source for `-l 1024` and for BWA `-n` default 0.04. A former dsDNA preprocess script (removed; see REMOVALS.md) already used `--minlength 30` at line 12 (WORKFLOW default); the former generator used `--minlength 25`.
- 10,207 SNPs: cited from Cohen et al. 2023 Methods only in the 2026-11-15 teaching; not found in Noraz 2026. An appended catalogue erratum records this; existing rows are unchanged.
- READv2 “originally developed for human data” is restored from Noraz 2026 Methods. KIN README is registered once in SOURCES_READ. DOI_CHECKS.NOTES cites only primary sources directly.
- The figure script is `scripts/figures/copy_adna_schematics.py`. Preflight treats a dangling symlink as a collision and checks both targets before writing any file.
- REMOVALS.md records the capture-test scripts later removed from the tree, including the tested-steps note, the verbatim run_mapdamage command, the placeholder partition, flagstat-wording fragility, and the `#SBATCH --cpus-per-task=40` header with 35 threads in every step (lines 12-27 of the former preprocess script).
- F1 captions remain as updated in the earlier wording listed below ([待确认] marks). F2’s schmutzi caption follows the README Nuclear wording.

## 2026-11-15 — earlier wording later superseded

- Author citations: Wales et al. (2016); Meiri and Bar-Oz (2024).
- pyDamage is not taught as a competitive-mapping tool. schmutzi wording in the earlier 2026-11-15 wording below is superseded by the README Nuclear wording above.
- Library-type damage patterns (including terminal 1–2 bases and plant CG/CHG/CHH) are marked [待确认]; opened Briggs and Rohland abstracts support damage at molecule ends. Rohland is cited as 2015. DamageProfiler is no longer called “the faster” calculator.
- “Do not force diploid hard calls” and “pseudo-haploid is not a heterozygosity estimate” are labelled as this repository’s judgements.
- Relatedness wording in the earlier 2026-11-15 wording below is superseded by the KINgaroo / Canaguier / Noraz Methods wording above.
- `--minlength 30` is attributed to WORKFLOW, not to REMOVALS. mapDamage wrapper commands are labelled as templates. REMOVALS records replacement gaps for the capture-test scripts later removed from the tree.
- The figure script copies existing SVG files; it does not generate the drawings. F1 and F2 captions were updated to match the chapters.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — README errata and source-page updates

An earlier teaching-file addition left the appended README section without a pointer from the existing schmutzi and pyDamage claims to the teaching chapters. The appended README now includes that pointer. Existing rows and the two existing 02/03 scripts remain unedited.

- The appended README section (English and Chinese) now has an Errata subsection pointing existing L286 (schmutzi) to chapter 3 and E001, and existing L264 (pyDamage) to chapter 2 and E004. E001 is extended to cover the existing hapCon “like schmutzi” remarks (README L285, CATALOG L40). Existing rows stay unedited.
- Public `REMOVALS.md` and `REMOVALS.zh.md` line 5 omit local filesystem paths. The notes of the 52 appended catalogue rows C129–C180 are written as ordinary source notes. The sentence in `docs/04_capture_shotgun_lowcov.md` line 39 places the [待确认] marker at the end of the clause. `scripts/02_map_adna.v2.sh` line 37 names AdapterRemoval 2.3.4 and 3.0.2. Option A’s broken-link list cites chapter 4 L23 (not L19), plus L55, `SOURCES_READ.tsv` L88, and CHANGELOG L13. The appended README states that the README files and the catalogue are themselves appended, rather than claiming only new files are added.
- Following the additive-only approach, the earlier short checksum list and the earlier catalogue snapshot were left unedited in that addition. A 2026-11-15 addition first added a file named `SHA256SUMS.v2`, listing hashes for the files that addition added or appended. The extra manifest shipped in this tree is a later regeneration under the same filename; see the checksum-manifest section below.
- The existing `scripts/README.md` is not edited. The appended README section states that the existing “Tested?” table does not list the `.v2.sh` wrappers, and that those wrappers are help / `--dry-run` documentation only.
- AdapterRemoval 3.0.2: the versioned manpage https://adapterremoval.readthedocs.io/en/v3.0.2/manpage.html was first opened 2026-11-15 CST (73,940 bytes, sha256 72a82265…). The “latest” manpage opened 2026-11-15 CST (73,938 bytes, sha256 cd3ac4e7…) has the HTML title “AdapterRemoval 3.0.2 documentation”. Both document `--min-length` with “Defaults to 15.”
- Existing lines are left untouched. Wording left as-is is listed under “needs approval before editing existing text”. Nothing in that list is edited here.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — public wording cleanup

- The Chinese README errata quote ending “like schmutzi” now uses a half-width period.
- Version headings in this changelog use dates and short topic labels. The same dating style is used in the DOI check notes and in chapters 2 and 4.
- The versioned AdapterRemoval 3.0.2 manpage URL is cited consistently in chapter 4 (English and Chinese), in this changelog, and in the mapping-script header.
- The 3.0.2 manpage is recorded as first opened (not re-opened) in `SOURCES_READ.tsv` and in the mapping-script header. Canaguier 2017 and the other sources in chapter 4 are recorded with their 2026-11-15 CST open dates.
- Public `REMOVALS` wording now matches the appended README: the existing README files and catalogue are appended, and new teaching files are added.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — source-date wording

- Date entries in chapters 2–4, `SOURCES_READ.tsv`, this changelog, and related notes use the plain read date 2026-11-15 CST, with all facts, numbers, and DOIs unchanged.
- AdapterRemoval option names in this changelog are written as 2.3.4 and 3.0.2, not as unspecific major-version labels.
- Checksum-manifest arrangements from earlier copies of these teaching files are superseded by the single extra manifest described below.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — checksum manifest

- This tree ships one extra manifest, `SHA256SUMS.v2`, regenerated for the current teaching files added or appended relative to the existing repository. It is a new list for those current files, not the earlier list that first used the same filename. Intermediate extra manifests from earlier copies of these teaching files are not included.
- The appended README describes those two manifests and no longer lists a checksum file that is not shipped.
- Chinese REMOVALS no longer repeats the inventory-copy phrase in the sentence about how that copy was read.
- The paragraph introducing the README errata pointer uses plain date wording.

Claims without an opened source remain cut or marked [待确认].
