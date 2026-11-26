# grapevine-adna

English | [中文](README.zh.md)

<!-- PROSE:INTRO -->
This repository is a methods catalogue for *Vitis* ancient DNA, covering sampling, clean-room practice, extraction, library preparation, capture or shotgun sequencing, preprocessing, mapping, damage authentication, contamination, low-coverage genotyping, dating, and downstream analyses alongside modern grapes. Overlap with [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen) is expected and retained.
<!-- /PROSE:INTRO -->

It contains no unpublished genotypes or private site coordinates, and no demo data.

<!-- PROSE:STATUS -->
Status: this repository already contains capture scripts under `scripts/` and notes under `notes/` (added on `main` in the 2026-10-21 commit; see section 14). Those files are a bioinformatics workflow for a capture test, not a full plant-specific wet-lab protocol.
<!-- /PROSE:STATUS -->

## Out of scope

- The modern 167K product: [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)
- Chip design: [grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip)
- Plastid assembly: [grapevine-plastid](https://github.com/Xuzhen-Li/grapevine-plastid)
- Theory dossiers: [genomics-theory-book](https://github.com/Xuzhen-Li/genomics-theory-book)
- Modern population-genetics catalogue (overlaps on purpose): [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen)

<!-- PROSE:CATALOG_NOTE -->
**2026-11-14 catalogue, v3.2.** Follows the same conventions as vitis-popgen: clusters, newest stable version only, [待确认] for unchecked items (with qualifiers written after the tag), and a workflow in [`docs/WORKFLOW.md`](docs/WORKFLOW.md). This repository already includes files under `scripts/` and `notes/` (a bioinformatics workflow for a capture test; see section 14).
<!-- /PROSE:CATALOG_NOTE -->

---

## Contents

1. [Sampling and archaeobotanical material](#section-1) (10)
2. [Clean-room and contamination control](#section-2) (8)
3. [Extraction protocols](#section-3) (6)
4. [Library preparation](#section-4) (7)
5. [Capture versus shotgun](#section-5) (8)
6. [Sequencing](#section-6) (1)
7. [Preprocessing](#section-7) (4)
8. [Mapping](#section-8) (14)
9. [Damage authentication](#section-9) (8)
10. [Contamination estimation](#section-10) (5)
11. [Low-coverage genotyping and imputation](#section-11) (4)
12. [Dating](#section-12) (7)
13. [Downstream popgen with modern samples](#section-13) (11)
14. [Workflows and pipelines](#section-14) (4)
15. [Plant- and grape-specific issues](#section-15) (6)
16. [Key studies, public data and simulation](#section-16) (7)
17. [Shared tools also catalogued in vitis-popgen](#section-17) (18)

This page lists 128 entries (57 tools; the rest are workflows, protocols, papers, resources or ideas). The table form is [`ADDITIONS.tsv`](ADDITIONS.tsv) and [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv).

<a id="section-1"></a>
## 1. Sampling and archaeobotanical material

<!-- PROSE:SECTION:A01 -->
Published grape aDNA derives primarily from seeds. A seed is a composite of tissues: the seed coat is maternal (sharing the mother plant's genotype, and thus the cultivar clone), the embryo is a sexual progeny, and the endosperm is triploid with two maternal genomes and one paternal genome in the common angiosperm case [待确认]. Li and Berger 2012 (doi:10.1111/j.1469-8137.2012.04182.x) provides a general review of endosperm development. Which tissue contributes the majority of DNA in archaeological pips has not been directly verified. The embryo originates from the L2 (germ) layer [待确认], while whether seed-coat DNA is predominantly L1-derived remains [待确认]. Layer-specific somatic variants in chimeric cultivars must not serve as diagnostic sites for a same-clone call (see also the L1/L2 entry in vitis-popgen). Wood, residues, and herbarium specimens serve as secondary sources, carrying distinct inhibitor profiles and ages.
<!-- /PROSE:SECTION:A01 -->

**Clusters:**
- *Key grape seed studies (complementary)*: Cohen et al. 2023, Inanli et al. 2026, Noraz et al. 2026, Pérez-Jordà et al. 2026, Ramos-Madrigal et al. 2019, Cappellini et al. 2010 waterlogged grape seeds, Wales et al. 2016 grape paleogenomics.
- *Material types (complementary)*: Archaeological grape seeds (pips), Wood, fruit residues and herbarium sheets, Le et al. 2026 seed tissue ploidy.

- **Cohen et al. 2023** (paper) — Ancient DNA from Negev Highlands desert grape pips, a Late Antiquity wine lineage. Input: n/a. Output: n/a. Version: n/a (Crossref title match, 2026-11-14 CST). [doi:10.1073/pnas.2213563120](https://doi.org/10.1073/pnas.2213563120) · [link](https://doi.org/10.1073/pnas.2213563120)  
  Note: Includes radiocarbon dating of pips. Ancient reads: ENA PRJNA887039 (Ancient Negev grape DNA, 20 runs). Modern panels cited in the literature review: PRJNA887737, PRJNA647155.
- **Inanli et al. 2026** (paper) — Cetamura del Chianti wells: multiproxy aDNA, morphometrics and NIR. 80 seeds from two wells; over a quarter belong to one clone kept for centuries, likely white-berried; two pips were consistent with dark berries. Input: n/a. Output: n/a. Version: n/a (Crossref title match, 2026-11-14 CST). [doi:10.1016/j.jas.2026.106605](https://doi.org/10.1016/j.jas.2026.106605) · [link](https://doi.org/10.1016/j.jas.2026.106605)  
  Note: Data: ENA PRJEB89110 (title matches the paper; DS14). Wording follows the abstract: it does not say that most seeds were white-berry like.
- **Noraz et al. 2026** (paper) — 49 archaeological pips spanning about 4000 years, mostly from France, plus Ibiza and nearby areas; clonal continuity includes a medieval match to Pinot Noir and a medieval Ibiza match to Folha de Figueira. Input: n/a. Output: n/a. Version: n/a (Crossref title match, 2026-11-14 CST). [doi:10.1038/s41467-026-70166-z](https://doi.org/10.1038/s41467-026-70166-z) · [link](https://doi.org/10.1038/s41467-026-70166-z)  
  Note: Data: ENA PRJEB94459, titled ancient grapevine genomes from France and Ibiza (DS14). The paper focuses primarily on France; sample V156 is from medieval Ibiza (1027-1160 CE). Do not call the set '49 French pips'.
- **Pérez-Jordà et al. 2026** (paper) — 28 seeds from Iberia and Sardinia; eastern introductions, local wild hybridisation, and long clonal persistence of Heben and Pasa Valenciana. Input: n/a. Output: n/a. Version: n/a (Crossref title match, 2026-11-14 CST). [doi:10.1016/j.cub.2026.08.039](https://doi.org/10.1016/j.cub.2026.08.039) · [link](https://doi.org/10.1016/j.cub.2026.08.039)  
  Note: ENA accession for this paper was not confirmed in the literature review. PRJEB104344 ('Shotgun sequencing of two Iberian grapevine cultivar founders') is a candidate only and is not recorded here as the paper's dataset [待确认] (accession). Do not treat that project ID as verified.
- **Ramos-Madrigal et al. 2019** (paper) — 28 archaeological grape seeds (France), target-enriched around about 10,000 SNPs (10,207) selected from the 18K grape array (Laucou et al. 2018); one medieval seed matched living Savagnin Blanc. Input: n/a. Output: n/a. Version: n/a (Crossref title match, 2026-11-14 CST). [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  Note: Data: PRJNA489970 and figshare 10.6084/m9.figshare.7610987 (DS14). The 10,207 SNP count is from Laucou et al. 2018 and from Cohen 2023 / Noraz 2026 descriptions of this design. Capture with myBaits is reported as myBaits protocol v3.0 in Cohen 2023's account of the same panel, not from the Ramos-Madrigal 2019 Methods (paywalled in the literature review) [待确认] (in the original Methods). The abstract says 28 archaeological grape seeds; the title and PRJNA489970 point to France, but the abstract does not itself say that every seed is French [待确认].
- **Cappellini et al. 2010 waterlogged grape seeds** (paper) — Waterlogged grape seeds: DNA (five SSRs), proteins and carbohydrates. Five SSRs cannot identify a cultivar, and apparent homozygosity may be allelic dropout. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1007/s00114-009-0629-3](https://doi.org/10.1007/s00114-009-0629-3) · [link](https://doi.org/10.1007/s00114-009-0629-3)
- **Wales et al. 2016 grape paleogenomics** (paper) — Tests of palaeogenomic methods on archaeological grape seeds. The literature review retrieved the title and DOI but not the abstract; summary is therefore limited [待确认] (abstract). Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.jas.2016.05.014](https://doi.org/10.1016/j.jas.2016.05.014) · [link](https://doi.org/10.1016/j.jas.2016.05.014)
- **Archaeological grape seeds (pips)** (resource) — Preferred tissue in published grape aDNA studies: waterlogged or desiccated seeds, sometimes with a split reserved for radiocarbon. Tissue origin of the recovered DNA (seed coat, embryo or endosperm) has not been directly verified. Input: excavated pips. Output: subsampled tissue. Version: n/a (literature below; DS14).  
  Note: Charred seeds usually yield little DNA. Combine with morphometrics (Terral school) when possible. Published grape pip studies that describe sampling used whole-seed grinding or drilling (Cohen 2023; Bolognesi 2025). No published grape pip study reviewed here reported allele-ratio evidence for the contributing tissue. See section 1 of the README and decision point 1 in docs/WORKFLOW.md.
- **Wood, fruit residues and herbarium sheets** (resource) — Secondary tissues: waterlogged wood, fruit remains, and historical herbarium leaves or pips, each with different inhibitor and damage profiles. Input: wood, residues, herbarium. Output: subsampled tissue. Version: n/a (methods papers in section 3).  
  Note: Herbarium sheets often have a known collection year, which is a dating prior. Mercuric chloride treatments damage DNA.
- **Le et al. 2026 seed tissue ploidy** (paper) — Compared embryo and leaf DNA from herbarium specimens; the introduction summarises seed-coat (2n, maternal), endosperm (3n) and embryo (2n) ploidy. The study is on rice and wild barley, not grape, and is cited only for this general tissue genetics. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1111/1755-0998.70210](https://doi.org/10.1111/1755-0998.70210) · [link](https://doi.org/10.1111/1755-0998.70210)

<a id="section-2"></a>
## 2. Clean-room and contamination control

<!-- PROSE:SECTION:A02 -->
Dedicated pre-PCR space, unidirectional workflow, and sequenced blanks. A wine or grape laboratory poses a high contamination risk from modern cultivar DNA.
<!-- /PROSE:SECTION:A02 -->

**Clusters:**
- *Lab practice (in order)*: Dedicated pre-PCR aDNA laboratory, Extraction and library blanks.
- *Key lab-practice references (complementary)*: Cooper and Poinar 2000 authenticity criteria, Gilbert et al. 2005 authenticity critique, Llamas et al. 2017 contamination control, Fulton and Shapiro 2019 lab setup, Knapp et al. 2012 lab setup, Korlević et al. 2015 bleach pretreatment.

- **Dedicated pre-PCR aDNA laboratory** (protocol) — All extraction and library setup in a dedicated, physically separated pre-amplification space, with PPE, bleach or equivalent cleaning, and unidirectional workflow. Input: samples. Output: controlled extracts. Version: n/a (standard aDNA practice, summarised in Latorre et al. 2020). [doi:10.1002/cppb.20121](https://doi.org/10.1002/cppb.20121) · [link](https://doi.org/10.1002/cppb.20121)  
  Note: DOI is Latorre et al. 2020, which states these requirements for plant aDNA.
- **Extraction and library blanks** (protocol) — Run extraction blanks and library blanks in every batch and sequence them. A grape-wine laboratory is a high-risk modern-DNA environment. Input: blank reactions. Output: blank libraries, contamination metrics. Version: n/a (standard aDNA practice).  
  Note: Modern cultivar DNA in a viticulture institute can look like a true ancient match. Treat unexpected clone matches with extra contamination checks.
- **Cooper and Poinar 2000 authenticity criteria** (paper) — Classic authenticity criteria for aDNA work. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1126/science.289.5482.1139b](https://doi.org/10.1126/science.289.5482.1139b) · [link](https://doi.org/10.1126/science.289.5482.1139b)
- **Gilbert et al. 2005 authenticity critique** (paper) — Critique and refinement of aDNA authenticity criteria. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.tree.2005.07.005](https://doi.org/10.1016/j.tree.2005.07.005) · [link](https://doi.org/10.1016/j.tree.2005.07.005)
- **Llamas et al. 2017 contamination control** (paper) — Field-to-lab contamination control, written for human aDNA; the laboratory rules still transfer. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1080/20548923.2016.1258824](https://doi.org/10.1080/20548923.2016.1258824) · [link](https://doi.org/10.1080/20548923.2016.1258824)
- **Fulton and Shapiro 2019 lab setup** (paper) — How to set up and run a dedicated aDNA clean laboratory. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1007/978-1-4939-9176-1_1](https://doi.org/10.1007/978-1-4939-9176-1_1) · [link](https://doi.org/10.1007/978-1-4939-9176-1_1)
- **Knapp et al. 2012 lab setup** (paper) — Practical design and workflow of an aDNA laboratory. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.aanat.2011.03.008](https://doi.org/10.1016/j.aanat.2011.03.008) · [link](https://doi.org/10.1016/j.aanat.2011.03.008)
- **Korlević et al. 2015 bleach pretreatment** (paper) — Bleach and pre-digestion to reduce surface contamination; tested on bone, so plant use needs testing. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.2144/000114320](https://doi.org/10.2144/000114320) · [link](https://doi.org/10.2144/000114320)

<a id="section-3"></a>
## 3. Extraction protocols

<!-- PROSE:SECTION:A03 -->
PTB-DTT plus silica extraction for aged or archaeological plant remains; benchmark against the 2025 grape-pip S-PDE protocol rather than adopting a single method uncritically.
<!-- /PROSE:SECTION:A03 -->

**Clusters:**
- *Inhibitor-rich grape pips (alternatives)*: S-PDE extraction on archaeological grape pips (Bolognesi et al. 2025).
- *Silica and cross-link methods (alternatives)*: Dabney silica binding for ultra-short DNA, PTB-DTT plant extraction (Gutaker / Latorre), Wales and Kistler plant-remains extraction.
- *Key extraction references (complementary)*: Wales et al. 2014 archaeobotanical extraction, Rohland et al. 2018 extraction protocol.

- **S-PDE extraction on archaeological grape pips (Bolognesi et al. 2025)** (protocol) — Soil-optimised extraction plus aDNA silica binding on ancient grape pips; higher library-success rate than CTAB or DNeasy in two archaeological contexts. Input: archaeological grape pips. Output: libraries. Version: 2025 paper (Crossref title match, 2026-11-14 CST). [doi:10.1038/s41598-025-21743-7](https://doi.org/10.1038/s41598-025-21743-7) · [link](https://doi.org/10.1038/s41598-025-21743-7)  
  Note: The paper supports a higher library-success rate for S-PDE than for CTAB or DNeasy in two archaeological contexts, with sample-size limits: the library comparison used n = 8 for CTAB and DNeasy and n = 30 for S-PDE (Fig. 2 legend). The fourth method, phenol-chloroform, yielded no detectable DNA in any of eight extracts in their hands, so it was not a direct comparison with earlier phenol-chloroform grape-pip protocols that had worked elsewhere.
- **Dabney silica binding for ultra-short DNA** (protocol) — Silica binding buffer that retains very short fragments, widely reused for plant remains. Input: lysate. Output: short-fragment DNA extract. Version: 2013 paper (Crossref title match, 2026-11-14 CST). [doi:10.1073/pnas.1314445110](https://doi.org/10.1073/pnas.1314445110) · [link](https://doi.org/10.1073/pnas.1314445110)  
  Note: The paper is a cave bear mitogenome demonstration; the binding buffer is the widely used method.
- **PTB-DTT plant extraction (Gutaker / Latorre)** (protocol) — PTB and DTT release DNA from cross-links, then silica binding. Latorre et al. 2020 recommend it for old herbarium and archaeological remains. Input: herbarium or archaeological tissue. Output: extract. Version: Gutaker 2017; Latorre 2020 (Crossref title match, 2026-11-14 CST). [doi:10.2144/000114517](https://doi.org/10.2144/000114517) · [link](https://doi.org/10.2144/000114517)  
  Note: Gutaker et al. 2017 doi:10.2144/000114517. Protocol compilation: Latorre et al. 2020 doi:10.1002/cppb.20121. Marinček et al. 2022 (doi:10.1002/aps3.11477) found PTB-DTT better than a standard kit for old herbarium, while a kit may suffice for young sheets.
- **Wales and Kistler plant-remains extraction** (protocol) — Methods in Molecular Biology chapter on extracting ancient DNA from plant remains, including SDS versus CTAB choices. Input: plant remains. Output: extract. Version: 2019 chapter (Crossref title match, 2026-11-14 CST). [doi:10.1007/978-1-4939-9176-1_6](https://doi.org/10.1007/978-1-4939-9176-1_6) · [link](https://doi.org/10.1007/978-1-4939-9176-1_6)  
  Note: Earlier Kistler 2012 chapter: doi:10.1007/978-1-61779-516-9_10. A separate catalogue row covers Wales et al. 2014 (doi:10.1371/journal.pone.0086827), which reported SDS often outperforming CTAB on non-charred (mainly desiccated) archaeobotanical remains; no charred remains were tested.
- **Wales et al. 2014 archaeobotanical extraction** (paper) — Extraction tests on non-carbonised archaeobotanical remains, including grape seeds; used by Cohen et al. 2023. Bolognesi 2025 retells that an SDS / proteinase K / DTT plus phenol-chloroform protocol outperformed alternatives in that earlier work. The 2014 material was primarily desiccated and not charred, so results do not automatically transfer to charred pips. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1371/journal.pone.0086827](https://doi.org/10.1371/journal.pone.0086827) · [link](https://doi.org/10.1371/journal.pone.0086827)
- **Rohland et al. 2018 extraction protocol** (paper) — Updated silica extraction protocol (bones, teeth, sediments); a basis of many later plant adaptations. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1038/s41596-018-0050-5](https://doi.org/10.1038/s41596-018-0050-5) · [link](https://doi.org/10.1038/s41596-018-0050-5)

<a id="section-4"></a>
## 4. Library preparation

<!-- PROSE:SECTION:A04 -->
Select a double-stranded or single-stranded library protocol, and register the UDG treatment (none, half, or full) in advance, as expected damage profiles depend on this choice (see section 9). Full UDG treatment does not remove thymines resulting from the deamination of methylated plant cytosines in CG, CHG, or CHH contexts.
<!-- /PROSE:SECTION:A04 -->

**Clusters:**
- *Damage treatment (alternatives)*: Partial UDG (UDG-half) treatment.
- *Double-stranded libraries (alternatives)*: Meyer and Kircher double-stranded library.
- *Single-stranded libraries (alternatives)*: Gansauge single-stranded library (ssDNA2 and later automated versions), Santa Cruz reaction (SCR).
- *Key damage-treatment references (complementary)*: Briggs et al. 2010 USER/UDG.
- *Key library references (complementary)*: Carøe et al. 2018 single-tube library, Wales et al. 2015 ss versus ds libraries.

- **Partial UDG (UDG-half) treatment** (protocol) — Removes most internal uracils but leaves terminal damage for authentication. Input: extract or pre-library DNA. Output: UDG-half DNA. Version: Rohland et al. 2015 (Crossref title match, 2026-11-14 CST). [doi:10.1098/rstb.2013.0624](https://doi.org/10.1098/rstb.2013.0624) · [link](https://doi.org/10.1098/rstb.2013.0624)  
  Note: Choose UDG-half, full UDG, or no UDG in advance. No-UDG keeps more damage for authentication but complicates transition sites. Full UDG is cleaner for genotyping but weaker for damage evidence.
- **Meyer and Kircher double-stranded library** (protocol) — Classic blunt-end double-stranded aDNA library with single or dual indexing. Input: extract. Output: ds library. Version: 2010 (Crossref title match, 2026-11-14 CST). [doi:10.1101/pdb.prot5448](https://doi.org/10.1101/pdb.prot5448) · [link](https://doi.org/10.1101/pdb.prot5448)  
  Note: Pair with unique dual indexes (Kircher et al. 2012, doi:10.1093/nar/gkr771). The existing repo notes describe a dsDNA batch.
- **Gansauge single-stranded library (ssDNA2 and later automated versions)** (protocol) — Single-stranded libraries recover molecules with single-strand breaks or blocked ends, often better when endogenous content is low. Input: extract. Output: ss library. Version: 2013 / 2017 / 2020 (Crossref title matches, 2026-11-14 CST). [doi:10.1038/s41596-020-0338-0](https://doi.org/10.1038/s41596-020-0338-0) · [link](https://doi.org/10.1038/s41596-020-0338-0)  
  Note: 2013 Nature Protocols doi:10.1038/nprot.2013.038; 2017 NAR doi:10.1093/nar/gkx033; 2020 Nat Protoc doi:10.1038/s41596-020-0338-0.
- **Santa Cruz reaction (SCR)** (protocol) — Faster single-stranded library method used widely in aDNA labs; a 2025 protocols.io update also exists. Input: extract. Output: ss library. Version: Kapp 2021 (Crossref title match, 2026-11-14 CST). [doi:10.1093/jhered/esab012](https://doi.org/10.1093/jhered/esab012) · [link](https://doi.org/10.1093/jhered/esab012)  
  Note: Kapp et al. 2021. Protocol updates on protocols.io were seen in search results but not used as a substitute for the paper.
- **Briggs et al. 2010 USER/UDG** (paper) — Full UDG plus endonuclease VIII (USER) treatment of aDNA libraries. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1093/nar/gkp1163](https://doi.org/10.1093/nar/gkp1163) · [link](https://doi.org/10.1093/nar/gkp1163)
- **Carøe et al. 2018 single-tube library** (paper) — Blunt-end single-tube (BEST) double-stranded library; cited by Cohen et al. 2023 for part of its libraries. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1111/2041-210x.12871](https://doi.org/10.1111/2041-210x.12871) · [link](https://doi.org/10.1111/2041-210x.12871)
- **Wales et al. 2015 ss versus ds libraries** (paper) — Compares single-stranded and double-stranded library preparation on aDNA extracts. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.2144/000114364](https://doi.org/10.2144/000114364) · [link](https://doi.org/10.2144/000114364)

<a id="section-5"></a>
## 5. Capture versus shotgun

<!-- PROSE:SECTION:A05 -->
Shallow shotgun sequencing can screen a library; deeper shotgun or in-solution capture can then increase coverage. Published grape-pip capture targeted roughly 10,000 SNPs (10,207) selected from the 18K grape array (Laucou et al. 2018), rather than the full 18k site set. Organelle reads can inform genus-level assignment, subject to the caveats noted in the plastid entry.
<!-- /PROSE:SECTION:A05 -->

**Clusters:**
- *Strategy (alternatives)*: In-solution target enrichment (myBaits / similar), Shallow shotgun screening then deeper shotgun.
- *Strategy (complementary)*: Plastid, mitochondrion and rDNA as authentication and species ID, Organelle-to-nuclear read ratio (idea).
- *Key capture references (complementary)*: Maricic et al. 2010 homemade capture, Carpenter et al. 2013 whole-genome capture, Cruz-Dávalos et al. 2017 capture conditions, Laucou et al. 2018 10K grape SNP panel.

- **In-solution target enrichment (myBaits / similar)** (protocol) — In-solution capture around a grape SNP panel. Ramos-Madrigal et al. and later grape papers used about 10,000 SNPs (10,207) selected from the 18K grape array (Laucou et al. 2018). Input: libraries, bait set. Output: enriched libraries. Version: [待确认] kit version (used in Ramos-Madrigal 2019 and later grape studies; kit version not pinned here). [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  Note: Do not call the capture panel an 18k-site panel. The 10,207 figure is from Laucou et al. 2018 (10.1371/journal.pone.0192540). Cohen 2023 reports capturing this set with the myBaits protocol version 3.0; that kit version is Cohen's description [待确认] (against Ramos-Madrigal 2019 Methods). Kit version in general remains [待确认].
- **Shallow shotgun screening then deeper shotgun** (idea) — Screen libraries shallowly, then sequence deeper only those with usable endogenous content and authentic damage. Input: libraries. Output: screening metrics, deeper data. Version: n/a (standard palaeogenomics practice).  
  Note: Good when fragments are very short or bait design would miss variation.
- **Plastid, mitochondrion and rDNA as authentication and species ID** (idea) — Organelle and rDNA reads can support authentication and genus-level identification. Vitis plastids are essentially maternally inherited, but sequence differences among Vitis species are small and chloroplast capture can occur, so plastid data are not enough for within-genus species or cultivar identification. Heteroplasmy-like patterns often come from nuclear plastid or mitochondrial insertions (NUPT, NUMT) and from plastid-derived tracts in the mitochondrial genome. Input: libraries. Output: organelle coverage, species ID. Version: n/a (standard plant aDNA practice).  
  Note: Use organelle-to-nuclear read ratios only as a secondary preservation or authenticity indicator, and compete-map to reduce NUPT/NUMT confusion. See also grapevine-plastid.
- **Organelle-to-nuclear read ratio (idea)** (idea) — Compare plastid and mitochondrial versus nuclear read ratios with a modern grape baseline as a secondary preservation or authenticity indicator. Nuclear plastid insertions (NUPT) can interfere; use competitive mapping. Input: BAM. Output: organelle-to-nuclear ratio. Version: n/a (methods review, 2026-11-14 CST).
- **Maricic et al. 2010 homemade capture** (paper) — Low-cost homemade capture baits for multiplexed aDNA libraries. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1371/journal.pone.0014004](https://doi.org/10.1371/journal.pone.0014004) · [link](https://doi.org/10.1371/journal.pone.0014004)
- **Carpenter et al. 2013 whole-genome capture** (paper) — Whole-genome in-solution capture (WISC) to raise endogenous content. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.ajhg.2013.10.002](https://doi.org/10.1016/j.ajhg.2013.10.002) · [link](https://doi.org/10.1016/j.ajhg.2013.10.002)
- **Cruz-Dávalos et al. 2017 capture conditions** (paper) — Tests of capture conditions (temperature, bait, rounds) for aDNA in solution. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1111/1755-0998.12595](https://doi.org/10.1111/1755-0998.12595) · [link](https://doi.org/10.1111/1755-0998.12595)
- **Laucou et al. 2018 10K grape SNP panel** (paper) — The 10K grape SNP set (783 genotypes, 10,207 SNPs from an 18K array) used for pip capture. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1371/journal.pone.0192540](https://doi.org/10.1371/journal.pone.0192540) · [link](https://doi.org/10.1371/journal.pone.0192540)

<a id="section-6"></a>
## 6. Sequencing

<!-- PROSE:SECTION:A06 -->
Unique dual indexes and short-insert paired-end sequencing. Record the instrument actually used; do not invent a default machine.
<!-- /PROSE:SECTION:A06 -->

**Clusters:**
- *Sequencing practice (in order)*: Unique dual indexing and short-insert PE sequencing.

- **Unique dual indexing and short-insert PE sequencing** (protocol) — Use unique dual indexes to limit index hopping. Paired-end 75 or 100 bp usually covers typical aDNA insert lengths. Input: indexed libraries. Output: FASTQ. Version: Kircher et al. 2012 plus current Illumina practice (Kircher DOI verified; instrument versions not pinned). [doi:10.1093/nar/gkr771](https://doi.org/10.1093/nar/gkr771) · [link](https://doi.org/10.1093/nar/gkr771)  
  Note: Demultiplex conservatively. Do not invent a preferred instrument model; record the one actually used.

<a id="section-7"></a>
## 7. Preprocessing

<!-- PROSE:SECTION:A07 -->
Adapter trimming and merging (collapsing) of overlapping short inserts. The default minimum collapsed length is 30 bp due to the repetitive and highly heterozygous nature of the grape genome; 25 bp is reserved strictly for sensitivity analyses.
<!-- /PROSE:SECTION:A07 -->

**Clusters:**
- *Adapter trimming and collapsing (alternatives)*: AdapterRemoval, Cutadapt, leeHom.
- *Complexity and QC (complementary)*: preseq.

- **AdapterRemoval** (tool) — Trims adapters, collapses overlapping pairs, and applies a minimum length. Default in the existing repo notes. Input: paired FASTQ. Output: collapsed and singleton FASTQ. Version: 3.0.2 (GitHub MikkelSchubert/adapterremoval + Bioconda, 2026-11-14 CST (release 2026-08-20)). [doi:10.1186/s13104-016-1900-2](https://doi.org/10.1186/s13104-016-1900-2) · [link](https://github.com/MikkelSchubert/adapterremoval)  
  Note: The verified DOI is AdapterRemoval v2 (Schubert 2016). Newest software is 3.0.2. Existing notes use --trimqualities --minquality 2 --trimns --minlength 25 --collapse (dsDNA batch --minlength 30). Re-check flags if you move from v2 to v3. The catalogue version is the newest tool line (v2 paper already cited). The first AdapterRemoval paper is Lindgreen 2012, 10.1186/1756-0500-5-337, and is not a second tool entry.
- **Cutadapt** (tool) — General adapter trimmer; usable, but aDNA pipelines more often use AdapterRemoval or leeHom because of collapsing. Input: FASTQ. Output: trimmed FASTQ. Version: 5.2 (Bioconda/PyPI cutadapt 5.2; GitHub tags are stale (v4.0)). [link](https://github.com/marcelm/cutadapt)
- **leeHom** (tool) — Bayesian adapter trimming and merging, an alternative used in some aDNA pipelines. Input: paired FASTQ. Output: merged FASTQ. Version: 1.2.18 (GitHub grenaud/leeHom + Bioconda, 2026-11-14 CST). [doi:10.1093/nar/gku699](https://doi.org/10.1093/nar/gku699) · [link](https://github.com/grenaud/leeHom)  
  Note: Method paper: 10.1093/nar/gku699 (Crossref-verified in the literature review).
- **preseq** (tool) — Library-complexity curves, used in nf-core/eager to decide whether deeper sequencing is worthwhile. Input: BAM or reads. Output: complexity curve. Version: 3.2.0 (GitHub smithlabcode/preseq + Bioconda, 2026-11-14 CST). [link](https://github.com/smithlabcode/preseq)

<a id="section-8"></a>
## 8. Mapping

<!-- PROSE:SECTION:A08 -->
Default alignment uses bwa aln with the seed disabled. Document each parameter and its source separately, and quote existing repository scripts verbatim. For collapsed reads, DeDup is the default duplicate marker. See the workflow for the distinction between Schubert 2012 and ancient-human mapping parameters.
<!-- /PROSE:SECTION:A08 -->

**Clusters:**
- *Competitive mapping and composition (complementary)*: FastQ Screen, Kraken2, MALT, HOPS.
- *Graph mapping for ancient seeds (complementary)*: vg Giraffe.
- *Post-mapping filters (in order)*: samtools + Picard MarkDuplicates or DeDup.
- *Short aDNA alignment (alternatives)*: CircularMapper, bowtie2.
- *Short aDNA alignment (default route)*: bwa aln (disabled seeding).
- *Key mapping references (complementary)*: Oliva et al. 2021 mapping benchmark, Schubert et al. 2012 bwa aln parameters.
- *Reference bias (complementary)*: Dolenz et al. 2024 reference bias, Günther and Nettelblad 2019 reference bias, Martiniano et al. 2020 graph mapping.

- **FastQ Screen** (tool) — Screens reads against grape, human, microbes and other plants to catch swaps and contamination. Input: FASTQ, multiple references. Output: composition tables. Version: 0.16.0 (GitHub StevenWingett/FastQ-Screen + Bioconda, 2026-11-14 CST). [link](https://github.com/StevenWingett/FastQ-Screen)  
  Note: Competitive mapping against several Vitis references or a graph is the natural next step (project 20).
- **Kraken2** (tool) — Taxonomic composition of unmapped or all reads. Input: FASTQ or unmapped BAM. Output: taxonomic report. Version: 2.17.2 (Bioconda kraken2 2.17.2 (latest stable); GitHub also has v2.18.0-RC2, not used here). [link](https://github.com/DerrickWood/kraken2)  
  Note: A 2.18.0 release candidate exists (2026-11-06) and is not used as the catalog version.
- **MALT** (tool) — Alignment-based metagenomic binning, used inside nf-core/eager. Input: reads, MALT database. Output: rma, taxon tables. Version: 0.5.2 (GitHub husonlab/malt + Bioconda, 2026-11-14 CST). [link](https://github.com/husonlab/malt)
- **HOPS** (tool) — MALT plus MaltExtract for damage-aware screening of microbes. On grape pips it is for microbial or pathogen composition, not for authenticating endogenous grape DNA. Input: reads, MALT database. Output: taxon list and damage statistics. Version: 0.35 (GitHub rhuebler/HOPS release 0.35, checked 2026-11-14 CST; Bioconda reported in the methods review). [doi:10.1186/s13059-019-1903-0](https://doi.org/10.1186/s13059-019-1903-0) · [link](https://github.com/rhuebler/HOPS)
- **vg Giraffe** (tool) — Map ancient reads to a Vitis pangenome graph and compare allele balance with linear mapping (project 20). Input: FASTQ, graph. Output: GAM/BAM, VCF. Version: 1.78.0 (see vitis-popgen section 11; also AM17). [link](https://github.com/vgteam/vg)  
  Note: Test on downsampled modern grapes before ancient seeds.
- **samtools + Picard MarkDuplicates or DeDup** (tool) — Post-mapping BAM filters. For collapsed single-end aDNA reads, DeDup is the default duplicate marker because it uses both endpoints; Picard MarkDuplicates uses only the 5-prime coordinate and can over-remove. Keep MarkDuplicates as a comparison. Input: SAM/BAM. Output: deduplicated BAM, flagstat. Version: samtools 1.25; Picard 3.5.0; DeDup 0.12.9 (versions checked 2026-11-14 CST). [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/samtools)  
  Note: Default for collapsed reads: DeDup. Quote the reason when the other tool is used. samtools 1.25; Picard 3.5.0; DeDup 0.12.9 (versions from the v1 check).
- **CircularMapper** (tool) — Improves mapping to circular organelle references (plastid, mitochondrion). Input: FASTQ, circular FASTA. Output: BAM. Version: 1.93.5 (GitHub apeltzer/CircularMapper + Bioconda, 2026-11-14 CST). [link](https://github.com/apeltzer/CircularMapper)  
  Note: Complementary to nuclear bwa aln, not a replacement.
- **bowtie2** (tool) — Alternative local aligner offered by nf-core/eager. Input: FASTQ, reference. Output: BAM. Version: 2.5.5 (GitHub BenLangmead/bowtie2 + Bioconda, 2026-11-14 CST). [link](https://github.com/BenLangmead/bowtie2)  
  Note: Use only if a comparison against bwa aln is pre-registered. Not the default in the existing repo scripts.
- **bwa aln (disabled seeding)** (tool) — Default short-read aligner for damaged aDNA. Write each parameter and its source separately; do not mix script values with literature values. Input: collapsed FASTQ, reference FASTA. Output: BAM. Version: 0.7.19 (GitHub lh3/bwa + Bioconda, 2026-11-14 CST; parameter sources listed in the note). [doi:10.1186/1471-2164-13-178](https://doi.org/10.1186/1471-2164-13-178) · [link](https://github.com/lh3/bwa)  
  Note: Parameter sources, checked against Schubert et al. 2012 (10.1186/1471-2164-13-178): `-l 1024` disables the seed on Illumina data (Schubert 2012); Schubert kept the default `-n` 0.04 for Illumina. The Helicos setting in that paper is `-l 1024 -i 0 -o 2 -n 0.03`, not the Illumina setting. The combination `-n 0.01 -o 2` is common in ancient human studies (often with `-l 16500`) and is cited by Dolenz et al. 2024 as coming from Green et al. 2010; the original source remains [待确认]. For a benchmark of parameterised BWA-aln, BWA-mem and NovoAlign on simulated human reads, see the Oliva et al. 2021 row; that paper does not establish a single preferred aligner.
- **Oliva et al. 2021 mapping benchmark** (paper) — Benchmark of 30 aDNA mapping strategies on simulated human reads: specific BWA-aln, BWA-mem and NovoAlign settings gave high precision and low reference bias, especially after MAPQ filtering; unbiased NovoAlign needed an IUPAC reference. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature and methods reviews, 2026-11-14 CST). [doi:10.1093/bib/bbab076](https://doi.org/10.1093/bib/bbab076) · [link](https://doi.org/10.1093/bib/bbab076)
- **Schubert et al. 2012 bwa aln parameters** (paper) — Source for disabling the seed with `-l 1024` on Illumina data. The Helicos command line is different. See the bwa aln note for what this paper did and did not show. Input: n/a. Output: n/a. Version: n/a (already the DOI on the bwa aln row; restated as a source note). [doi:10.1186/1471-2164-13-178](https://doi.org/10.1186/1471-2164-13-178) · [link](https://doi.org/10.1186/1471-2164-13-178)
- **Dolenz et al. 2024 reference bias** (paper) — Assesses reference bias in ancient DNA datasets across mappers and MAPQ thresholds; test data include plant (maize) examples. Useful when mapping pips to PN40024. Input: n/a. Output: n/a. Version: n/a (EuropePMC PMID 38960861 and Crossref, 2026-11-14 CST). [doi:10.1093/bioinformatics/btae436](https://doi.org/10.1093/bioinformatics/btae436) · [link](https://doi.org/10.1093/bioinformatics/btae436)  
  Note: Title: Unravelling reference bias in ancient DNA datasets. Crossref issued 2024-07-01.
- **Günther and Nettelblad 2019 reference bias** (paper) — Reference bias in low-coverage aDNA; relevant to mapping pips to PN40024. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1371/journal.pgen.1008302](https://doi.org/10.1371/journal.pgen.1008302) · [link](https://doi.org/10.1371/journal.pgen.1008302)
- **Martiniano et al. 2020 graph mapping** (paper) — Graph-genome mapping to reduce reference bias in aDNA. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1186/s13059-020-02160-7](https://doi.org/10.1186/s13059-020-02160-7) · [link](https://doi.org/10.1186/s13059-020-02160-7)

<a id="section-9"></a>
## 9. Damage authentication

<!-- PROSE:SECTION:A09 -->
Damage profiles authenticate ancient DNA and govern how residual damage is handled prior to genotyping. Establish the expected pattern from the library type and UDG treatment first: double-stranded libraries typically exhibit C-to-T substitutions at the 5-prime end and G-to-A at the 3-prime end; single-stranded libraries exhibit C-to-T at both ends; and UDG-half treatment typically leaves residual damage in the terminal one or two bases.
<!-- /PROSE:SECTION:A09 -->

**Clusters:**
- *Damage profiles (alternatives)*: DamageProfiler, mapDamage2.
- *Damage-read filters (complementary)*: PMDtools, pyDamage.
- *Damage-read handling (in order, after profiling)*: bamUtil trimBam, Damage pattern by library type and UDG (idea).
- *Key damage-profile references (complementary)*: Briggs et al. 2007 damage pattern, Sawyer et al. 2012 damage versus age.

- **DamageProfiler** (tool) — Faster damage-pattern calculation, the nf-core/eager alternative to mapDamage2. Input: BAM, reference. Output: damage plots, tables. Version: 1.1 (GitHub Integrative-Transcriptomics/DamageProfiler + Bioconda, 2026-11-14 CST). [doi:10.1093/bioinformatics/btab190](https://doi.org/10.1093/bioinformatics/btab190) · [link](https://github.com/Integrative-Transcriptomics/DamageProfiler)  
  Note: Last tagged release remains 1.1 (2020). Still the current Bioconda version.
- **mapDamage2** (tool) — Default damage and fragmentation profile in AM17 and in scripts/run_mapdamage.sh. Input: BAM, reference. Output: misincorporation plots, optional rescaled BAM. Version: 2.2.3 (GitHub ginolhac/mapDamage + Bioconda, 2026-11-14 CST (also AM17)). [doi:10.1093/bioinformatics/btt193](https://doi.org/10.1093/bioinformatics/btt193) · [link](https://github.com/ginolhac/mapDamage)  
  Note: Existing wrapper: mapDamage -i BAM -r REF -d OUT --merge-reference-sequences. Use this, not a later untested flag set, unless you re-validate. Cite with the original mapDamage paper (Ginolhac et al. 2011, 10.1093/bioinformatics/btr347) when describing damage plots. --rescale can downweight likely damaged bases as an alternative to hard trimming; compare the two on downsampled data.
- **PMDtools** (tool) — Scores and filters reads by post-mortem damage, separating endogenous from modern-like reads. Input: BAM. Output: PMD-filtered BAM, scores. Version: 0.60 (GitHub pontussk/PMDtools + Bioconda, 2026-11-14 CST). [doi:10.1073/pnas.1318934111](https://doi.org/10.1073/pnas.1318934111) · [link](https://github.com/pontussk/PMDtools)  
  Note: Skoglund et al. 2014 DOI verified.
- **pyDamage** (tool) — Per-contig damage estimation, useful when many references are involved (metagenomes or competitive mapping). Input: BAM. Output: per-contig damage. Version: 1.0 (GitHub maxibor/pydamage + Bioconda/PyPI, 2026-11-14 CST). [doi:10.7717/peerj.11845](https://doi.org/10.7717/peerj.11845) · [link](https://github.com/maxibor/pydamage)
- **bamUtil trimBam** (tool) — Trims N bases from each end of reads according to library type and UDG treatment, for example 2 nt each end after UDG-half, before pseudo-haploid calling. Input: BAM. Output: trimmed BAM. Version: v1.0.15 (GitHub statgen/bamUtil release v1.0.15, checked 2026-11-14 CST). [link](https://github.com/statgen/bamUtil)  
  Note: Method DOI [待确认]. This is the default terminal-trim tool named in the methods review.
- **Damage pattern by library type and UDG (idea)** (idea) — Set the expected damage pattern before interpreting mapDamage plots: double-stranded libraries, C-to-T at 5-prime and G-to-A at 3-prime; single-stranded libraries, C-to-T at both ends; UDG-half, residual damage mostly in the last 1-2 terminal bases; full UDG removes most of that damage, but T from deamination of methylated plant cytosines (CG/CHG/CHH) remains. Input: damage profiles. Output: trim or filter plan. Version: n/a (genetics and methods reviews, 2026-11-14 CST).
- **Briggs et al. 2007 damage pattern** (paper) — Defines the terminal C-to-T damage pattern used for authentication. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1073/pnas.0704665104](https://doi.org/10.1073/pnas.0704665104) · [link](https://doi.org/10.1073/pnas.0704665104)
- **Sawyer et al. 2012 damage versus age** (paper) — Damage and fragment length versus age; damage is not a simple clock. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1371/journal.pone.0034131](https://doi.org/10.1371/journal.pone.0034131) · [link](https://doi.org/10.1371/journal.pone.0034131)

<a id="section-10"></a>
## 10. Contamination estimation

<!-- PROSE:SECTION:A10 -->
Prioritise plant-appropriate contamination checks: sequenced blanks, composition, and comparison of results before and after PMD filtering. AuthentiCT applies solely to single-stranded libraries, while hapCon and other male-X methods do not apply to grape. Unusual heterozygosity or allele ratios in a pip can also come from a maternal-plus-embryo or endosperm-containing mixture rather than contamination alone. Allele ratios alone cannot distinguish a tissue mixture from present-day contamination, nor can they identify which component is maternal. The primary evidence separating tissue mixing from modern contamination comes from damage-stratified reads and fragment-length distributions; a parent-offspring test can only exclude an unrelated source (see the section 13 concept and the workflow).
<!-- /PROSE:SECTION:A10 -->

**Clusters:**
- *Model-based tools with caveats (alternatives)*: AuthentiCT, hapCon, schmutzi.
- *Plant-appropriate checks (complementary)*: Blanks, species composition and excess heterozygosity, PMD-filter drift check (idea).

- **AuthentiCT** (tool) — Estimates present-day contamination from damage patterns. Applies to any species with a reference, but only to single-stranded libraries. Input: BAM or damage patterns. Output: contamination fraction. Version: v1.0.1 (GitHub StephanePeyregne/AuthentiCT tag and release v1.0.1 (2023-03-10), checked 2026-11-14 CST). [doi:10.1186/s13059-020-02123-y](https://doi.org/10.1186/s13059-020-02123-y) · [link](https://github.com/StephanePeyregne/AuthentiCT)  
  Note: Single-stranded libraries only. Do not use it on UDG-treated data or after PMD filtering (official README). The repository exists (https://github.com/StephanePeyregne/AuthentiCT); it is not a 404. Do not run it on the default double-stranded branch of this workflow.
- **hapCon** (tool) — Human contamination estimator that uses the male X chromosome. Listed only to prevent misuse; it does not apply to grape. Input: haploid calls, reference panel. Output: contamination estimate. Version: [待确认] (Huang et al. 2022 paper verified; software tag not checked). [doi:10.1093/bioinformatics/btac390](https://doi.org/10.1093/bioinformatics/btac390) · [link](https://github.com/hringbauer/hapROH)  
  Note: hapCon requires a hemizygous male X chromosome (Huang and Ringbauer 2022). Grape has no such chromosome, so this is not a tool that can be tested into applicability. Keep the entry as a warning, like schmutzi.
- **schmutzi** (tool) — Mitochondrial contamination estimator written for humans. Not a grape nuclear contamination tool. Input: mt BAM. Output: contamination estimate. Version: 1.5.7 (GitHub grenaud/schmutzi + Bioconda, 2026-11-14 CST). [doi:10.1186/s13059-015-0776-0](https://doi.org/10.1186/s13059-015-0776-0) · [link](https://github.com/grenaud/schmutzi)  
  Note: Listed so that it is not used by mistake for nuclear grape data. Written for human mtDNA; grape use would need testing. Listed to prevent uncritical reuse. DOI 10.1186/s13059-015-0776-0.
- **Blanks, species composition and excess heterozygosity** (idea) — Plant-appropriate contamination checks: sequenced blanks, competitive mapping and species composition, and excess heterozygosity. A mixture of maternal and embryo DNA can also shift allele ratios away from 0.5 and can be misread as contamination. Input: BAMs, blanks. Output: QC decision. Version: n/a (methods practice; no single software DOI).  
  Note: Treat a maternal-plus-embryo tissue mixture and present-day DNA contamination as competing explanations when allele ratios or heterozygosity look unusual. Allele ratios alone cannot separate the two. See the pre-registered two-genotype mixture test in section 13.
- **PMD-filter drift check (idea)** (idea) — Compare PCA projections and f4 before and after PMDtools filtering. A clear shift suggests modern grape DNA contamination. This check is usable in plants; hapCon is not. Input: BAM. Output: two projection results to compare. Version: n/a (uses PMDtools already in this catalogue). [doi:10.1073/pnas.1318934111](https://doi.org/10.1073/pnas.1318934111) · [link](https://github.com/pontussk/PMDtools)

<a id="section-11"></a>
## 11. Low-coverage genotyping and imputation

<!-- PROSE:SECTION:A11 -->
Begin with genotype likelihoods or pseudo-haploid calls. A pseudo-haploid call randomly samples one read per site; while unbiased toward either allele, it discards within-individual heterozygosity and must not be used as a direct heterozygosity estimate. At low coverage, majority-rule calling at heterozygous sites introduces bias; rely on random read draws or genotype likelihoods instead, which is especially critical in highly heterozygous grape compared with human data. Apply GLIMPSE2 only after a pre-registered accuracy benchmark on modern samples downsampled to ancient depths. For single-stranded libraries, run pileupCaller with `--singleStrandMode`.
<!-- /PROSE:SECTION:A11 -->

**Clusters:**
- *Imputation after a modern-downsample test (alternatives)*: GLIMPSE2.
- *Low-coverage calling (alternatives)*: ANGSD haploid calls and genotype likelihoods, ATLAS, sequenceTools pileupCaller.

- **GLIMPSE2** (tool) — Impute ancient grape genomes only after measuring accuracy on modern samples downsampled to the same depth (AM17, project 20). Input: low-coverage BAM or GLs, modern haplotype panel. Output: imputed VCF. Version: 2.0.0 (GitHub odelaneau/GLIMPSE tag v2.0.0 (latest stable), 2026-11-14 CST; v2.0.1 is a GitHub pre-release and is not used as the catalogue version). [doi:10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3) · [link](https://github.com/odelaneau/GLIMPSE)  
  Note: For aDNA, test accuracy on modern grapes downsampled to ancient depths first (AM17, project 20). GitHub v2.0.1 is marked pre-release (checked 2026-11-14 CST); Bioconda glimpse-bio may still list 2.0.1. This catalogue pins the latest stable tag, 2.0.0, consistent with not using RC or beta tags as the catalogue version.
- **ANGSD haploid calls and genotype likelihoods** (tool) — Preferred likelihood route: do not force diploid GT at very low coverage. Random haploid draws or genotype likelihoods for structure. Input: BAM, sites list. Output: haploid calls, genotype likelihoods. Version: 0.940 (see vitis-popgen section 2). [doi:10.1186/s12859-014-0356-4](https://doi.org/10.1186/s12859-014-0356-4) · [link](https://github.com/ANGSD/angsd)  
  Note: For no-UDG data, consider transversion-only analyses. Grapevine heterozygosity makes naive majority-call genotypes noisy.
- **ATLAS** (tool) — Damage-aware aDNA caller. Bioconda version 2.0.4 was seen; confirm the bitbucket source before pinning. Input: BAM. Output: likelihoods or VCF. Version: 2.0.4 (Bioconda atlas) (Bioconda atlas 2.0.4; expected Wegmann-lab source not resolved on GitHub in this check). [link](https://bitbucket.org/wegmannlab/atlas)  
  Note: URL and exact upstream tag [待确认].
- **sequenceTools pileupCaller** (tool) — Pseudo-haploid calls from pileup, widely used to place aDNA on modern SNP panels. Input: BAM, SNP list. Output: EIGENSTRAT or haploid VCF. Version: 1.6.0.0 (GitHub stschiff/sequenceTools + Bioconda, 2026-11-14 CST). [link](https://github.com/stschiff/sequenceTools)  
  Note: For single-stranded libraries use `--singleStrandMode` (available since v1.4.0). For no-UDG data, drop transition sites or otherwise account for damage. Keep the SNP set matched to the modern panel. Version v1.6.0.0 matches the GitHub release (2026-01-28).

<a id="section-12"></a>
## 12. Dating

<!-- PROSE:SECTION:A12 -->
Prioritise radiocarbon dating on the same seed or a paired seed, alongside herbarium collection dates. Molecular tip-dating should rely on transversions or UDG-treated data. A tip date reflects the seed's death date, whereas the clonal genotype itself may be older; if an ancient pip belongs to the same clone as a living cultivar, molecular tip-dating carries virtually no temporal signal.
<!-- /PROSE:SECTION:A12 -->

**Clusters:**
- *Molecular tip dating (alternatives, use transversions)*: BEAST 2, LSD2, TreeTime, Separate seed death date from clone origin (idea).
- *Radiocarbon and calibration (complementary)*: AMS radiocarbon on the same seed or a paired seed, Bchron, rcarbon.

- **BEAST 2** (tool) — Tip-dating of ancient grape sequences. Restrict to transversions or UDG-treated data, and randomise tips as a test. Input: alignment, dates. Output: dated trees. Version: 2.7.8 (see vitis-popgen section 3). [link](https://www.beast2.org/)  
  Note: Herbarium sheets with a collection year are safer tips than poorly dated seeds. Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **LSD2** (tool) — Least-squares dating of trees with dated tips. Input: tree, dates. Output: dated tree. Version: 2.4.1 (GitHub tothuhien/lsd2 + Bioconda, 2026-11-14 CST). [link](https://github.com/tothuhien/lsd2)  
  Note: Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **TreeTime** (tool) — Fast time-tree placement, mainly a sanity check rather than a grape domestication clock. Input: tree, dates. Output: time tree. Version: 0.12.1 (GitHub neherlab/treetime + Bioconda, 2026-11-14 CST). [link](https://github.com/neherlab/treetime)  
  Note: Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **Separate seed death date from clone origin (idea)** (idea) — A radiocarbon or tip date is the seed's death date. The clonal genotype may be older. Tip-dating is uninformative when the pip is the same clone as a living cultivar, because the molecular branch length is essentially zero. Input: AMS dates and, if used, molecular alignments. Output: model settings that keep the two times distinct. Version: n/a (methods and genetics reviews, 2026-11-14 CST).
- **AMS radiocarbon on the same seed or a paired seed** (protocol) — Date the same biological individual when tissue allows, or a tightly associated seed from the same context. Input: tissue or associated seed. Output: radiocarbon date. Version: n/a (used in Cohen et al. 2023 and Inanli et al. 2026 among others). [doi:10.1073/pnas.2213563120](https://doi.org/10.1073/pnas.2213563120) · [link](https://doi.org/10.1073/pnas.2213563120)  
  Note: Cohen et al. 2023 is one grape example that combined aDNA and radiocarbon. Calibration curve choice (IntCal) belongs in the lab report.
- **Bchron** (tool) — Bayesian radiocarbon calibration and chronology in R. Input: radiocarbon determinations. Output: calibrated dates. Version: 4.7.8 (CRAN Bchron, 2026-11-14 CST). [link](https://cran.r-project.org/package=Bchron)
- **rcarbon** (tool) — Calibration, SPD and demographic-sum tools for radiocarbon dates. Input: dates. Output: calibrated distributions. Version: 1.5.2 (CRAN rcarbon, 2026-11-14 CST). [link](https://cran.r-project.org/package=rcarbon)  
  Note: OxCal is widely used but is a vendor application; version was not checked in this build [待确认].

<a id="section-13"></a>
## 13. Downstream popgen with modern samples

<!-- PROSE:SECTION:A13 -->
Project samples onto a clone-pruned modern PCA, compute f-statistics, and test identity against living cultivars. Report same-clone and first-degree conclusions separately, as both rely on an unverified tissue-origin assumption. Overlap with vitis-popgen is expected. Apply low-coverage kinship tools following calibration rather than KING hard-call thresholds. Seeds from the same archaeological unit may be siblings and should be screened first. The pre-registered mixture test in this section distinguishes a single genotype from a mixture; if endosperm is present, a two-parameter model is required, and allele ratios alone cannot separate tissue mixing from modern contamination or identify the maternal component.
<!-- /PROSE:SECTION:A13 -->

**Clusters:**
- *Clone matching through time (complementary)*: Identity to living cultivars, READv2, KIN (KINgaroo), BREADR, Pre-registered allele-ratio test for seed-tissue mixture (idea).
- *Projecting onto moderns (in order)*: ADMIXTOOLS 2 f-statistics and qpAdm, hapROH on ancient cultivars, smartpca lsqproject, Process modern samples on the same footing (idea).
- *ROH and heterozygosity at low coverage (alternatives)*: ROHan.
- *Relatedness within an archaeological unit (complementary)*: Sibling check among seeds from the same unit (idea).

- **Identity to living cultivars** (idea) — Test whether an ancient pip is the same clone as a living cultivar, a first-degree relative of one, or only from the same broader group. These outcomes depend on an unverified tissue-origin assumption and on contamination controls. Input: ancient and modern genotypes. Output: kinship or IBS, with contamination checks. Version: n/a (results reported in Ramos-Madrigal 2019, Noraz 2026, Pérez-Jordà 2026). [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://doi.org/10.1038/s41477-019-0437-5)  
  Note: Same-clone language is only straightforward if the DNA mainly represents maternal seed-coat tissue. If it mainly represents the embryo, a parent-offspring relationship is the expected match to the mother cultivar. Distinguish same-clone from first-degree results in the write-up. Use low-coverage kinship tools (READv2, KIN, BREADR; calibrate on modern pairs downsampled to the same depth), not a generic 'kinship or IBS' cutoff and not KING hard-call thresholds. Molecular tip-dating is uninformative if the pip is the same clone as a living cultivar.
- **READv2** (tool) — Relatedness from pairwise mismatch rates on pseudo-haploid low-coverage data (up to third degree). Developed on human data; calibrate on modern grape clone and relative pairs downsampled to the same depth. Noraz et al. 2026 (doi:10.1038/s41467-026-70166-z) recalibrated it for grape clones against VIVC, as confirmed against that paper in the 2026-11-14 literature re-review. Input: pseudo-haploid PLINK or EIGENSTRAT. Output: relatedness class. Version: 2.1.1 (GitHub GuntherLab/READv2 release 2.1.1, checked 2026-11-14 CST). [doi:10.1186/s13059-024-03350-3](https://doi.org/10.1186/s13059-024-03350-3) · [link](https://github.com/GuntherLab/READv2)  
  Note: This is the current READ lineage; the original READ paper (10.1371/journal.pone.0195491) is not a second tool entry.
- **KIN (KINgaroo)** (tool) — HMM of IBD segments from low coverage (down to about 0.05x in the human tests), with optional contamination correction and an ROH model. Grape use needs calibration. Input: BAM via KINgaroo. Output: relatedness class and IBD segments. Version: v3.1.4 (GitHub DivyaratanPopli/Kinship_Inference release v3.1.4, checked 2026-11-14 CST). [doi:10.1186/s13059-023-02847-7](https://doi.org/10.1186/s13059-023-02847-7) · [link](https://github.com/DivyaratanPopli/Kinship_Inference)
- **BREADR** (tool) — Posterior probabilities of identical/twins, first-degree, second-degree or unrelated on ultra-low-coverage pseudo-haploid data. The identical class can be used for clone matching between ancient pips and living cultivars after calibration. Input: EIGENSTRAT. Output: relatedness-class posteriors. Version: 1.1.0 (CRAN BREADR 1.1.0, checked 2026-11-14 CST). [doi:10.32614/CRAN.package.BREADR](https://doi.org/10.32614/CRAN.package.BREADR) · [link](https://cran.r-project.org/package=BREADR)
- **Pre-registered allele-ratio test for seed-tissue mixture (idea)** (idea) — If a high-depth ancient pip is available, pre-register a mixture test at sites that are heterozygous in at least one of the inferred genotypes. A seed-coat plus embryo mixture is two diploid genotypes with a maternal DNA fraction m (seed-coat contribution); expected minor-allele fractions vary continuously with m: for a maternal AA / embryo AB site the B fraction is about (1−m)/2; for a maternal AB / embryo AA site it is about m/2; sites heterozygous in both stay near 0.5. A single peak at 0.5 is consistent with one diploid genotype; extra components away from 0.5 are consistent with a mixture. A 1/3 (or 2/3) peak is only the special case of pure endosperm at sites such as maternal AA plus a paternal B (endosperm AAB). When endosperm DNA is also present, the seed is still a mix of maternal and paternal-derived haplotypes (the egg and the polar nuclei come from the same megaspore; the two sperm of one pollen grain share a genotype), but a single m is no longer the seed-coat fraction and a two-parameter, three-haplotype model is needed. Allele ratios alone cannot tell which component is maternal, and they cannot separate a tissue mixture from present-day contamination, because both are genotype mixtures. Triallelic sites are only an auxiliary indicator. To separate tissue mixing from modern contamination, the main evidence is (i) damage-stratified analysis: whether the minor genotype persists when only reads with terminal C-to-T substitutions are kept, and (ii) fragment-length distributions. A parent-offspring check is only supporting: it can rule out an unrelated modern contaminant, but it cannot rule out contamination from a related living cultivar, and the constraint itself must include selfing (the father is the same plant as the mother). Pre-registration thresholds remain [待确认] and must be locked before any ancient sample is analysed; this catalogue does not invent those numbers. Input: high-depth BAM or VCF. Output: mixture-model fit, allele-ratio histogram, auxiliary triallelic count. Version: n/a (catalogue revision, 2026-11-14 CST).  
  Note: Design note, with all numerical thresholds left [待确认] and not published here: restrict the primary analysis to transversion sites; compare a single-genotype model, an unconstrained mixture model, and a parent-offspring-constrained mixture model (the constraint must include selfing, in which the father is the same plant as the mother) using a likelihood-ratio test with a parametric bootstrap (a Bayesian version, if used, is only a sensitivity analysis). A second-tier decision on tissue mixture versus modern contamination should rest mainly on PMD- or damage-stratified reads and fragment-length distributions. A parent-offspring likelihood ratio can only rule out an unrelated source; related-cultivar modern contamination can still pass that test. Simulated negative controls (modern samples downsampled and given damage) and positive controls (in silico mixtures of parent-offspring pairs, a selfing scenario, endosperm scenarios, and both unrelated and related-cultivar contamination) should be completed, and the thresholds locked, before any ancient data are seen. Published grape pip studies reviewed here did not report this test. Li and Berger 2012 (10.1111/j.1469-8137.2012.04182.x) is a general review of endosperm development. The two-maternal, one-paternal endosperm genome ratio is stated here as the common angiosperm case [待确认]. Le et al. 2026 (10.1111/1755-0998.70210) mention seed-tissue ploidy only as background in rice and barley.
- **ADMIXTOOLS 2 f-statistics and qpAdm** (tool) — f3, f4 and qpAdm with ancient and modern groups, after a pre-registered grouping. Input: genotype blocks. Output: f-statistics, admixture models. Version: 2.0.1 (see vitis-popgen section 6). [doi:10.7554/elife.85492](https://doi.org/10.7554/elife.85492) · [link](https://github.com/uqrmaie1/admixtools)  
  Note: Overlap with vitis-popgen is intentional.
- **hapROH on ancient cultivars** (tool) — ROH from low-coverage data using a haplotype reference panel. Designed and tested on human data (1240k / 1000 Genomes panels). Not a clonal-history method: clonal propagation does not create ROH. Input: haploid calls, modern panel. Output: ROH. Version: 0.70 (see vitis-popgen section 8). [doi:10.1038/s41467-021-25289-w](https://doi.org/10.1038/s41467-021-25289-w) · [link](https://github.com/hringbauer/hapROH)  
  Note: Human-specific as distributed. Use on Vitis only after building a Vitis phased haplotype panel and validating on modern grapes downsampled to the target depth; unvalidated results must not be reported. ROH reflects inbreeding at the sexual origin of the sampled genotype, not centuries of clonal propagation. Prefer species-general ROHan, or bcftools roh when depth is sufficient. Newest is 0.70 on GitHub/PyPI; Bioconda lagged at 0.64.
- **smartpca lsqproject** (tool) — Project ancient samples onto a modern, clone-pruned grape PCA without letting them define the axes. Input: modern EIGENSTRAT, ancient genotypes. Output: projected PCs. Version: see vitis-popgen section 2 (EIGENSOFT, version caveat unchanged). [link](https://github.com/DReichLab/EIG)  
  Note: Missingness and damage can still shift projections; report coverage and transition/transversion choices.
- **Process modern samples on the same footing (idea)** (idea) — Before PCA projection or f-statistics, process modern samples on the same SNP set, with the same pseudo-haploidisation and the same transversion filter, and downsample to ancient depth when needed, so technical differences are not read as population differences. Input: modern BAM or VCF. Output: matched genotype matrix. Version: n/a (methods review, 2026-11-14 CST).
- **ROHan** (tool) — Joint estimate of heterozygosity and ROH from a single BAM, with optional damage correction, and without a human haplotype panel. A species-general alternative to hapROH. The paper reports usable depth as low as 5−6x on modern samples and 7−8x on ancient samples with moderate DNA damage. Input: BAM. Output: heterozygosity and ROH tracts. Version: v1.0.7 (GitHub grenaud/ROHan release v1.0.7, checked 2026-11-14 CST). [doi:10.1534/genetics.119.302057](https://doi.org/10.1534/genetics.119.302057) · [link](https://github.com/grenaud/ROHan)  
  Note: ROH still reflects inbreeding at sexual origin, not clonal history.
- **Sibling check among seeds from the same unit (idea)** (idea) — Seeds from the same layer or even the same bunch may be full or half siblings. Check relatedness and then prune or model it before allele frequencies, PCA or f-statistics, as in the modern-sample workflow. Input: low-coverage genotypes from co-located pips. Output: relatedness table and a pruned or modelled set. Version: n/a (genetics review, 2026-11-14 CST).

<a id="section-14"></a>
## 14. Workflows and pipelines

<!-- PROSE:SECTION:A14 -->
nf-core/eager 2.5.3 is the default community workflow (AM17), subject to a Nextflow 22.10.6 version ceiling. This repository already includes capture scripts added on 2026-10-21.
<!-- /PROSE:SECTION:A14 -->

**Clusters:**
- *Community workflows (alternatives)*: EAGER (legacy Java pipeline), PALEOMIX, nf-core/eager.
- *This repository (complementary)*: Existing capture scripts and notes.

- **EAGER (legacy Java pipeline)** (workflow) — Original EAGER pipeline. Keep only to understand older papers; use nf-core/eager for new runs. Input: FASTQ. Output: BAM, QC. Version: see Peltzer 2016; superseded by nf-core/eager for new work (Peltzer et al. 2016 DOI verified). [doi:10.1186/s13059-016-0918-z](https://doi.org/10.1186/s13059-016-0918-z) · [link](https://doi.org/10.1186/s13059-016-0918-z)
- **PALEOMIX** (workflow) — Alternative pipeline for aDNA mapping, filtering and phylogenetic downstream steps. Input: FASTQ, reference. Output: BAM, phylogenetic inputs. Version: 1.4.1 (GitHub MikkelSchubert/paleomix, 2026-11-14 CST). [doi:10.1038/nprot.2014.063](https://doi.org/10.1038/nprot.2014.063) · [link](https://github.com/MikkelSchubert/paleomix)  
  Note: Schubert et al. 2014 Nature Protocols DOI verified.
- **nf-core/eager** (workflow) — Default end-to-end aDNA workflow in AM17: AdapterRemoval, bwa aln, DamageProfiler or mapDamage, DeDup or MarkDuplicates, Qualimap, preseq, optional PMDtools, Kraken2/MALT. Input: FASTQ, reference. Output: BAM, damage, QC MultiQC. Version: 2.5.3 (GitHub nf-core/eager 2.5.3 (2025-03-18); 3.0 Augsburg is not released (open milestone, 2026-11-14 CST)). [doi:10.7717/peerj.10947](https://doi.org/10.7717/peerj.10947) · [link](https://nf-co.re/eager)  
  Note: This is DSL1 and requires Nextflow >=20.07.1 and <=22.10.6. Version 3.0 is not released. Human contamination modules (ANGSD X-chromosome) must be turned off or ignored for grape.
- **Existing capture scripts and notes** (workflow) — Already in this repository: AdapterRemoval, bwa aln, samtools q30, Picard MarkDuplicates, Qualimap, mapDamage, and mapping-stat collection. Input: paired FASTQ, VS1.final.fa (path is a placeholder in the notes). Output: per-sample BAM, damage, stats.all.tsv. Version: GitHub main fe75e89e, 2026-10-21 22:19 CST (Xuzhen-Li/grapevine-adna main, read-only audit 2026-11-14). [link](https://github.com/Xuzhen-Li/grapevine-adna/tree/main/scripts)  
  Note: Files: scripts/adna_capture_pipeline_generator.sh, dsdna_preprocess.sh, collect_mapping_stats.sh, run_mapdamage.sh; notes/cap_test.md, check_pcrbias.md, mergeBAM.md. These files are existing material in the repository: a bioinformatics workflow for a capture test.

<a id="section-15"></a>
## 15. Plant- and grape-specific issues

<!-- PROSE:SECTION:A15 -->
Inhibitors and polyphenols, absence of a mammalian X-chromosome contamination estimator, a small sex-determining region on chromosome 2 rather than heteromorphic sex chromosomes, PN40024 reference bias, and clonal identity spanning centuries. Plastid sequences are maternal but have low resolution within *Vitis*, while NUPT and NUMT insertions can mimic heteroplasmy.
<!-- /PROSE:SECTION:A15 -->

**Clusters:**
- *Reviews and plant-specific issues (complementary)*: Grape-specific analytical issues, Latorre et al. 2020 plant aDNA protocols, Ramos-Madrigal et al. 2026 plant palaeogenomics review, Kistler et al. 2020 plant aDNA review, Gutaker and Burbano 2017 plant aDNA, Meiri 2024 fruit paleogenomics.

- **Grape-specific analytical issues** (idea) — Plant and grape caveats: inhibitors and polyphenols; no mammalian X-chromosome dose method for contamination; a small sex-determining region on chromosome 2 rather than heteromorphic sex chromosomes; most cultivars are hermaphroditic; plastid data are maternal but have low resolution within Vitis and can be misread because of NUPT/NUMT insertions; PN40024 reference bias; clone identity across centuries. Input: n/a. Output: n/a. Version: n/a (synthesis of DS14, project 20, and this audit).  
  Note: Human X-chromosome contamination modules, including hapCon, do not transfer. See also grapevine-plastid for plastid assembly, and vitis-open-directions item 22 for sex-determining-region genotypes.
- **Latorre et al. 2020 plant aDNA protocols** (paper) — End-to-end plant aDNA isolation, library preparation and bioinformatics protocol. Input: n/a. Output: n/a. Version: n/a (Crossref title match). [doi:10.1002/cppb.20121](https://doi.org/10.1002/cppb.20121) · [link](https://doi.org/10.1002/cppb.20121)
- **Ramos-Madrigal et al. 2026 plant palaeogenomics review** (paper) — Short review of plant palaeogenomics: the shift to genome-wide data, changing views of domestication, plant-microbe coevolution, sedimentary DNA, and lost diversity for crop improvement. Input: n/a. Output: n/a. Version: n/a (Crossref title match; journal year 2026, DOI has 2025 suffix). [doi:10.1016/j.pbi.2025.102856](https://doi.org/10.1016/j.pbi.2025.102856) · [link](https://doi.org/10.1016/j.pbi.2025.102856)  
  Note: Wording follows the abstract (EuropePMC PMID 41610813). The abstract does not mention polyphenols, PCR inhibitors, single-stranded libraries, authentication, or grape tannins. Those topics should be cited from the Gansauge ss-library series and from Bolognesi 2025 / Wales 2014, not from this review, unless someone has read the full text [待确认].
- **Kistler et al. 2020 plant aDNA review** (paper) — Review of plant aDNA in archaeology, herbaria and sediments. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1146/annurev-arplant-081519-035837](https://doi.org/10.1146/annurev-arplant-081519-035837) · [link](https://doi.org/10.1146/annurev-arplant-081519-035837)
- **Gutaker and Burbano 2017 plant aDNA** (paper) — Short review of plant aDNA for evolutionary genomics. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.pbi.2017.01.002](https://doi.org/10.1016/j.pbi.2017.01.002) · [link](https://doi.org/10.1016/j.pbi.2017.01.002)
- **Meiri 2024 fruit paleogenomics** (paper) — Review of fruit-crop palaeogenomics, including grape. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1016/j.tig.2024.02.003](https://doi.org/10.1016/j.tig.2024.02.003) · [link](https://doi.org/10.1016/j.tig.2024.02.003)

<a id="section-16"></a>
## 16. Key studies, public data and simulation

<!-- PROSE:SECTION:A16 -->
Published grape aDNA datasets already listed in DS14, along with simulation tools for pipeline benchmarking. Contains no unpublished genotypes.
<!-- /PROSE:SECTION:A16 -->

**Clusters:**
- *Public grape aDNA datasets (complementary)*: DS14 archaeological grape seed sequencing, Cohen 2023 ancient pip reads, Inanli 2026 reads.
- *Simulation of aDNA reads (complementary)*: gargammel, ngsngs.
- *Related ancient-plant studies (complementary)*: Mascher et al. 2016 ancient barley, Kistler et al. 2017 DNA decay model.

- **DS14 archaeological grape seed sequencing** (resource) — PRJNA489970 (French capture), PRJEB89110 (Cetamura), PRJEB94459 (France 4000 years), PRJNA999173 (Grotte di Pertosa, linked paper [待确认]). Input: ENA. Output: FASTQ. Version: accessions listed 2026-11-14 in vitis-open-directions (DS14 README, sizes from ENA on 2026-11-14). [doi:10.1038/s41477-019-0437-5](https://doi.org/10.1038/s41477-019-0437-5) · [link](https://www.ebi.ac.uk/ena/browser/view/PRJNA489970)  
  Note: No unpublished genotypes. figshare 10.6084/m9.figshare.7610987 licence [待确认].
- **Cohen 2023 ancient pip reads** (resource) — ENA PRJNA887039, titled Ancient Negev grape DNA (20 runs). Modern panels recorded in the literature review: PRJNA887737, PRJNA647155. Input: n/a. Output: n/a. Version: n/a (ENA accession checked in the literature review, 2026-11-14 CST). [link](https://www.ebi.ac.uk/ena/browser/view/PRJNA887039)  
  Note: This is an accession, not a DOI.
- **Inanli 2026 reads** (resource) — ENA PRJEB89110; the title matches the Inanli et al. 2026 paper (first public 2026-05-31). Input: n/a. Output: n/a. Version: n/a (ENA accession checked in the literature review, 2026-11-14 CST). [link](https://www.ebi.ac.uk/ena/browser/view/PRJEB89110)  
  Note: This is an accession, not a DOI.
- **gargammel** (tool) — Simulates aDNA reads with damage, fragment length and contamination, for pipeline tests. Input: reference, parameters. Output: FASTQ. Version: 1.2.0 (GitHub grenaud/gargammel + Bioconda, 2026-11-14 CST). [link](https://github.com/grenaud/gargammel)  
  Note: Use before trusting project-20 imputation thresholds.
- **ngsngs** (tool) — Flexible NGS read simulator that can include aDNA-like features. Input: reference, profile. Output: FASTQ. Version: 0.9.2 (GitHub/Bioconda ngsngs, 2026-11-14 CST). [link](https://github.com/rbaumannhansen/ngsngs)  
  Note: Confirm aDNA parameters against the manual before using numbers in a preregistration.
- **Mascher et al. 2016 ancient barley** (paper) — Example of whole-genome sequencing of ancient plant grains. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1038/ng.3611](https://doi.org/10.1038/ng.3611) · [link](https://doi.org/10.1038/ng.3611)
- **Kistler et al. 2017 DNA decay model** (paper) — DNA decay model from 185 palaeogenomic datasets, mostly mammal bone, so plant seeds may differ. Input: n/a. Output: n/a. Version: n/a (Crossref-verified in the literature review, 2026-11-14 CST). [doi:10.1093/nar/gkx361](https://doi.org/10.1093/nar/gkx361) · [link](https://doi.org/10.1093/nar/gkx361)

<a id="section-17"></a>
## 17. Shared tools also catalogued in vitis-popgen

<!-- PROSE:SECTION:A17 -->
These tools are intentionally shared across both catalogues with identical details and versions; use this list as a cross-reference rather than a separate variant-calling pipeline. The low-coverage kinship and ROH tools shared with vitis-popgen (READv2, KIN, BREADR, ROHan) appear in section 13 and are not duplicated here.
<!-- /PROSE:SECTION:A17 -->

**Clusters:**
- *BAM processing (complementary)*: samtools.
- *Phasing and imputation of modern data (in order)*: GLIMPSE2.
- *Read QC (complementary)*: fastp.
- *Sample identity, before structure (complementary)*: KING.
- *BAM hygiene / post-mapping (complementary)*: Picard.
- *VCF QC and manipulation (complementary)*: bcftools.
- *Global ancestry (alternatives)*: ADMIXTURE.
- *Low-coverage genotype-likelihood methods (alternatives)*: ANGSD, PCAngsd.
- *PCA (alternatives)*: smartpca (EIGENSOFT).
- *Bayesian or dated trees (alternatives)*: BEAST 2.
- *tsinfer then tsdate (in order)*: tsinfer.
- *SMC-style histories (alternatives)*: SMC++.
- *f-statistics and graphs (alternatives)*: ADMIXTOOLS 2, Dsuite.
- *ROH callers (alternatives)*: bcftools roh.
- *ROH callers, low coverage (alternatives)*: hapROH.
- *Kinship, IBD and clonality (complementary)*: ngsRelate.

- **samtools** (tool) — Sort, index, mark duplicates, filter and report alignment statistics. Input: SAM/BAM/CRAM. Output: BAM/CRAM, stats. Version: 1.25 (GitHub samtools/samtools + Bioconda, 2026-11-14 CST). [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/samtools)  
  Note: Same 1.25 line as bcftools and htslib. samtools is not a mapper; it belongs with BAM processing, not under Mapping.
- **GLIMPSE2** (tool) — Imputes low-coverage genomes from a haplotype reference panel. Input: low-coverage BAM or genotype likelihoods, reference panel. Output: imputed VCF. Version: 2.0.0 (GitHub odelaneau/GLIMPSE tag v2.0.0 (latest stable), 2026-11-14 CST; v2.0.1 is a GitHub pre-release and is not used as the catalogue version). [doi:10.1038/s41588-023-01438-3](https://doi.org/10.1038/s41588-023-01438-3) · [link](https://github.com/odelaneau/GLIMPSE)  
  Note: For aDNA, test accuracy on modern grapes downsampled to ancient depths first (AM17, project 20). GitHub v2.0.1 is marked pre-release (checked 2026-11-14 CST); Bioconda glimpse-bio may still list 2.0.1. This catalogue pins the latest stable tag, 2.0.0, consistent with not using RC or beta tags as the catalogue version.
- **fastp** (tool) — Trims adapters and low-quality bases and writes a QC report. Input: FASTQ. Output: trimmed FASTQ, HTML/JSON QC. Version: 1.4.0 (GitHub OpenGene/fastp + Bioconda, checked 2026-11-14 CST). [link](https://github.com/OpenGene/fastp)  
  Note: GitHub release 2026-10-07. Also in vitis-open-directions AM02.
- **KING** (tool) — Robust kinship for clones or duplicates versus first-degree relatives. Clones and duplicates (kinship above 0.354) are reduced to one sample per group; first-degree relatives (0.177-0.354) are registered, not dropped as the same genotype. Not the default for low-coverage ancient pips. Input: hard-called diploid genotypes (BED). Output: kinship tables. Version: 2.3.2 (Bioconda king, 2026-11-14 CST). [doi:10.1093/bioinformatics/btq559](https://doi.org/10.1093/bioinformatics/btq559) · [link](https://www.kingrelatedness.com/)  
  Note: Thresholds follow the KING manual (https://www.kingrelatedness.com/manual.shtml): kinship above 0.354 is the duplicate/MZ class; 0.177-0.354 is first-degree. Paper: Manichaikul et al. 2010, 10.1093/bioinformatics/btq559. AM26 used 0.177 as the first-degree lower cutoff. Input should be hard-called diploid genotypes (BED). For low-coverage or ancient samples use ngsRelate, READv2, KIN or BREADR instead. Handling of first-degree relatives is analysis-specific; see docs/WORKFLOW.md.
- **Picard** (tool) — MarkDuplicates, read groups, CleanSam and related BAM hygiene. Input: BAM/SAM. Output: BAM, metrics. Version: 3.5.0 (GitHub broadinstitute/picard + Bioconda, 2026-11-14 CST). [link](https://github.com/broadinstitute/picard)  
  Note: Picard works on BAM (MarkDuplicates, read groups, CleanSam), not on VCF. GitHub release 2026-07-31 CST-relative: 2026-08-01 02:56 CST. For collapsed aDNA reads, DeDup is the default duplicate marker; see section 8.
- **bcftools** (tool) — Filter, normalise, annotate, compute statistics, and call ROH (see section 8). Input: VCF/BCF or BAM. Output: VCF/BCF, tables. Version: 1.25 (GitHub samtools/bcftools + Bioconda, 2026-11-14 CST). [doi:10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008) · [link](https://github.com/samtools/bcftools)
- **ADMIXTURE** (tool) — Maximum-likelihood ancestry proportions; default in AM13. Input: BED, LD-pruned SNPs. Output: Q and P matrices. Version: 1.3.0 (Bioconda admixture, 2026-11-14 CST). [doi:10.1101/gr.094052.109](https://doi.org/10.1101/gr.094052.109) · [link](https://dalexander.github.io/admixture/)  
  Note: Clone-prune first (one sample per clone or duplicate group). First-degree relatives should not be dropped as if they were the same genotype; for ADMIXTURE use an unrelated subset or report a sensitivity analysis (see docs/WORKFLOW.md). Choose K with cross-validation and inspect fit with evalAdmix.
- **ANGSD** (tool) — Genotype likelihoods, allele frequencies, SFS, association and haploid calls from BAM. Input: BAM, reference. Output: genotype likelihoods, SFS, MAF, haploid calls. Version: 0.940 (GitHub ANGSD/angsd + Bioconda, 2026-11-14 CST). [doi:10.1186/s12859-014-0356-4](https://doi.org/10.1186/s12859-014-0356-4) · [link](https://github.com/ANGSD/angsd)  
  Note: Central for aDNA and low-coverage modern data. Human X-chromosome contamination utilities do not transfer to grape.
- **PCAngsd** (tool) — PCA and admixture-style structure from genotype likelihoods, including low coverage. Input: ANGSD-style genotype likelihoods. Output: principal components, admixture. Version: 1.37.0 (GitHub Rosemeis/pcangsd 2026-10-23; Bioconda/PyPI 1.36.4). [doi:10.1534/genetics.118.301336](https://doi.org/10.1534/genetics.118.301336) · [link](https://github.com/Rosemeis/pcangsd)  
  Note: Newest GitHub tag is 1.37.0; Bioconda lagged at 1.36.4.
- **smartpca (EIGENSOFT)** (tool) — PCA with shrinkage and lsqproject, the usual way to project aDNA onto a modern PCA. Input: EIGENSTRAT. Output: eigenvectors, projected PCs. Version: 9.0.0 (Bioconda); GitHub tag v8.0.0 [待确认] (numbering) (Bioconda eigensoft 9.0.0; DReichLab/EIG GitHub tag v8.0.0). [doi:10.1371/journal.pgen.0020190](https://doi.org/10.1371/journal.pgen.0020190) · [link](https://github.com/DReichLab/EIG)  
  Note: Pin the exact binary. Bioconda and GitHub numbers disagree.
- **BEAST 2** (tool) — Bayesian trees and tip-dating when time calibrations exist. Input: alignment, priors. Output: trees, dates. Version: 2.7.8 (GitHub CompEvol/beast2 + Bioconda, 2026-11-14 CST). [link](https://www.beast2.org/)  
  Note: For aDNA tip-dating use transversions or UDG-treated data. Tip dates equal the seed's death date; the clonal genotype may already have existed for centuries. Molecular tip-dating has essentially no information when an ancient pip is the same clone as a living cultivar; use it only for samples separated by sexual generations. Prefer transversions or UDG-treated data.
- **tsinfer** (tool) — Infers a tree sequence (ARG approximation) from phased large samples. Input: phased genotypes. Output: tree sequence. Version: 0.5.1 (conda-forge tsinfer, 2026-11-14 CST (also AM14)). [doi:10.1038/s41588-019-0483-y](https://doi.org/10.1038/s41588-019-0483-y) · [link](https://github.com/tskit-dev/tsinfer)  
  Note: Pair with tsdate. Clone-prune and deal with close kinship first (AM14, project 10).
- **SMC++** (tool) — Effective-size history from many unphased genomes. Input: VCF, population labels. Output: Ne trajectory. Version: 1.15.2 (GitHub popgenmethods/smcpp + Bioconda, 2026-11-14 CST). [doi:10.1038/ng.3748](https://doi.org/10.1038/ng.3748) · [link](https://github.com/popgenmethods/smcpp)  
  Note: Reduce clones and duplicates to one sample per group. For recent Ne, also remove or model first-degree relatives (see docs/WORKFLOW.md).
- **ADMIXTOOLS 2** (tool) — f2, f3, f4, qpAdm and qpGraph in R, with block jackknife. Input: genotype or f2 blocks. Output: f-statistics, admixture graphs. Version: 2.0.1 (GitHub uqrmaie1/admixtools v2.0.1, 2026-11-14 CST (also AM13)). [doi:10.7554/elife.85492](https://doi.org/10.7554/elife.85492) · [link](https://github.com/uqrmaie1/admixtools)  
  Note: Default alternative in AM13. Maier et al. 2023 eLife DOI verified.
- **Dsuite** (tool) — Fast D, f4-ratio and f-branch statistics with block jackknife. Input: VCF, tree or trio file. Output: D, f4, f-branch tables. Version: [待确认] (no tagged release) (GitHub millanek/Dsuite; no tag or Bioconda package in this check (same as AM13)). [doi:10.1111/1755-0998.13265](https://doi.org/10.1111/1755-0998.13265) · [link](https://github.com/millanek/Dsuite)  
  Note: Version remains [待确认], as in AM13. The 2021 paper DOI was verified.
- **bcftools roh** (tool) — HMM runs of homozygosity. AM12 uses population allele frequencies after clone removal, not a default AF file. Input: VCF, population AF file. Output: ROH tables. Version: 1.25 (same bcftools 1.25 as section 1; also AM12). [doi:10.1093/bioinformatics/btw044](https://doi.org/10.1093/bioinformatics/btw044) · [link](https://github.com/samtools/bcftools)  
  Note: Default ROH tool in AM12. ROH method paper: Narasimhan et al. 2016, 10.1093/bioinformatics/btw044. The samtools/bcftools suite DOI 10.1093/gigascience/giab008 still applies to the package.
- **hapROH** (tool) — ROH from low-coverage data using a haplotype reference panel. Designed and tested on human data (1240k / 1000 Genomes panels). Not a clonal-history method: clonal propagation does not create ROH. Input: pseudo-haploid or low-coverage genotypes, reference panel. Output: ROH, inbreeding. Version: 0.70 (GitHub/PyPI hapROH 0.70; Bioconda 0.64). [doi:10.1038/s41467-021-25289-w](https://doi.org/10.1038/s41467-021-25289-w) · [link](https://github.com/hringbauer/hapROH)  
  Note: Human-specific as distributed. Use on Vitis only after building a Vitis phased haplotype panel and validating on modern grapes downsampled to the target depth; unvalidated results must not be reported. ROH reflects inbreeding at the sexual origin of the sampled genotype, not centuries of clonal propagation. Prefer species-general ROHan, or bcftools roh when depth is sufficient. Newest is 0.70 on GitHub/PyPI; Bioconda lagged at 0.64.
- **ngsRelate** (tool) — Relatedness from genotype likelihoods, including low-coverage data. Input: ANGSD genotype likelihoods. Output: relatedness. Version: 2.3.1 (GitHub ANGSD/NgsRelate + Bioconda, 2026-11-14 CST). [doi:10.1093/gigascience/giz034](https://doi.org/10.1093/gigascience/giz034) · [link](https://github.com/ANGSD/NgsRelate)


## Teaching chapters added on 2026-11-15

The lines above are the live repository homepage (commit b6e4302e, 2026-11-15 17:29 CST). This section is appended and does not replace that homepage. Every line above is unchanged.

This addition appends material to the live `README.md`, `README.zh.md`, and `catalog/CATALOG.tsv`; it also adds new teaching files. It does not modify the live `scripts/02_map_adna.sh` or `scripts/03_dedup.sh`. Every existing live line in the README files and the catalogue is unchanged.

### Errata for live homepage lines (pointers only; live lines unchanged)

Two live homepage claims are superseded, as teaching, by the chapters and catalogue errata below. The live lines themselves are not edited.

- Live L286 (`schmutzi`: “Mitochondrial contamination estimator written for humans. Not a grape nuclear contamination tool.”) — see [docs/03_contamination.md](docs/03_contamination.md) and catalogue row E001. The official schmutzi README Nuclear section says that contDeam can be used on nuclear data at the user's own risk under stated conditions; DICE is recommended for nuclear samples.
- Live L264 (`pyDamage`: “useful when many references are involved (metagenomes or competitive mapping)”) — see [docs/02_authentication_damage.md](docs/02_authentication_damage.md) and catalogue row E004. Per-contig damage estimation is described for metagenomic use; it is not taught as a competitive-mapping tool.

The live hapCon note (L285) and the live catalogue hapCon row (CATALOG L40) say “Keep the entry as a warning, like schmutzi.” That comparison is covered by the extended E001 note; those live lines are not edited.

### Manifests

The live `SHA256SUMS` file (not edited in this addition) covers the original files (`README.md`, `README.zh.md`, `ADDITIONS.tsv`, `catalog/CATALOG.tsv`, `docs/WORKFLOW.md`, and `docs/WORKFLOW.zh.md`). After the appended README and catalogue in this addition, the README and CATALOG hashes in that earlier manifest will no longer match. `SHA256SUMS.v2` covers the files added or extended later. `ADDITIONS.tsv` is a frozen earlier copy of the live catalogue (the same hash as the live CATALOG before these appended rows) and is not updated here.

### New or revised teaching files

- `CHANGELOG.md` — public summary of the teaching-file revisions
- `SHA256SUMS.v2` — hashes for the files added or appended later (the current extra manifest)
- `DOI_CHECKS.tsv`, `DOI_CHECKS.NOTES.md`
- `SOURCES_READ.tsv`
- `REMOVALS.md`, `REMOVALS.zh.md` — retirement proposal only; option B is recommended; nothing is deleted here
- `docs/01_published_grape_adna.md` and `.zh.md`
- `docs/02_authentication_damage.md` and `.zh.md`
- `docs/03_contamination.md` and `.zh.md`
- `docs/04_capture_shotgun_lowcov.md` and `.zh.md`
- `figures/F1_damage_patterns_by_library.svg`, `figures/F2_adna_decision_route.svg`
- `scripts/02_map_adna.v2.sh`, `scripts/03_dedup.v2.sh` — help / `--dry-run` wrappers under new filenames
- `scripts/figures/copy_adna_schematics.py` — copies the two SVG files; it does not generate the drawings

The live `scripts/README.md` is not edited. Its “Tested?” table therefore still lists `02_map_adna.sh` and `03_dedup.sh`, and does not list `02_map_adna.v2.sh` or `03_dedup.v2.sh`. Those `.v2.sh` wrappers are help / `--dry-run` documentation only; they do not replace the live scripts. They are listed in this section and in [CHANGELOG.md](CHANGELOG.md).

See [CHANGELOG.md](CHANGELOG.md) for the revision history of these teaching files.
