# 3. Contamination checks (and why hapCon is not a grape recipe)

In a viticulture laboratory, modern grape DNA is a contamination hazard as well as human DNA. The tools in this chapter were opened as papers or READMEs. Several of them were written for human data and must not be reused as if they were grape methods.

## hapCon is for male modern-human X chromosomes

Huang and Ringbauer (2022, full text, PMC9344841; doi:10.1093/bioinformatics/btac390) present hapCon as “a new method to estimate contamination in aDNA for male modern humans.” It “utilizes a Li&Stephens haplotype copying model for haploid X chromosomes, with mismatches modeled as errors or contamination.” The hapROH/hapCon GitHub README (https://github.com/hringbauer/hapROH, 2,332 bytes, opened 2026-11-15 CST) says: “hapCon is an extension of hapROH for estimating contamination rate for male aDNA samples.” There is no grape X-chromosome equivalent of that design in the sources we opened. This catalogue lists hapCon only to prevent misuse. We do not invent a grape hapCon recipe.

hapROH (Ringbauer et al. 2021, full text, PMC8440622) estimates runs of homozygosity from low-coverage data using a haplotype reference panel and was designed and tested on human data. It is not presented here as a ready-to-use grape clonal-history tool.

## AuthentiCT: single-stranded libraries, not UDG-treated or damage-filtered data

Peyrégne and Peter (2020, abstract; doi:10.1186/s13059-020-02123-y) present AuthentiCT “to estimate the proportion of present-day DNA contamination in ancient DNA datasets generated from single-stranded DNA libraries,” “based solely on the patterns of post-mortem damage,” with power “from as few as 10,000 mapped sequences.” The README (https://github.com/StephanePeyregne/AuthentiCT, 6,021 bytes) states, verbatim: “AuthentiCT only applies to sequences generated from single-stranded libraries and is not tailored for the more complex deamination patterns of sequences generated from double-stranded libraries. Also, it cannot estimate contamination from samples treated with Uracil-DNA Glycosylase (UDG) or other enzymes that alter the deamination patterns. For the same reason, it is not possible to estimate contamination in a filtered dataset of only deaminated sequences.” The same README says the method “assumes that the contaminant is not deaminated.”

## schmutzi: nuclear use is possible, at your own risk, under stated conditions

schmutzi (Renaud et al. 2015, doi:10.1186/s13059-015-0776-0) is a contamination toolkit. The official README was independently re-fetched 2026-11-15 CST (https://raw.githubusercontent.com/grenaud/schmutzi/master/README.md, 38,285 bytes, sha256 e85cb02b3697c85f716ecc823079a86b1671bd7972356d7a84bcf0e072d28f62, 2026-11-15 CST). The README says that contDeam’s default approach “is useful for all types of ancient DNA (nuclear and mitonchondrial)” [sic]. The Nuclear section says: “I recommend DICE (http://grenaud.github.io/dice) for nuclear samples. The only thing schmutzi can do for nuclear data is to estimate contamination rates using deamination patterns.” It then says “use this at your own risk” and lists conditions that lead to wrong estimates, including “at least 500M” molecules, endogenous deamination “upwards of 5%”, little or no deamination of the contaminant fragments, and independence of 5′ and 3′ deamination rates. “If you have a contaminant that is deaminated this will lead to an underestimate.” For mt, “we can at least cross-validate the contamination estimate using ‘mtCont’ but not for nuclear data.” This chapter does not teach “not a grape nuclear contamination tool” as a hard scope limit. Whether grape nuclear libraries meet those conditions was not tested here **[待确认]**. The README’s FAQ describes the default putative-contaminant database as “a very small putative contaminant database of 197 human mitogenomes using a worldwide sampling”; that library is human-oriented. A FAQ note also says USER/UDG treatment can explain a lack of deamination patterns.

The existing catalogue row for schmutzi (catalog/CATALOG.tsv, the A10 row in the existing b6e4302e table) still carries the older “not a grape nuclear contamination tool” wording; that existing row is not edited in this update. An appended erratum row records the README Nuclear wording above.

## Checks that do apply to plants, with limits

The PMDtools idea already in the catalogue—compare PCA or *f*-statistics before and after PMD filtering, and treat a clear shift as a warning of modern-like reads—remains a plant-applicable check, not a numerical threshold we invented. Extraction and library blanks should be processed and sequenced; Latorre et al. (2020, abstract; doi:10.1002/cppb.20121) is a plant aDNA isolation, library and bioinformatics protocol, not a generic “dedicated pre-PCR lab” paper under a wrong title. A grape-wine laboratory as a modern-grape DNA risk is a practical caution from the existing WORKFLOW, not a sentence we found in these papers; it stays a laboratory practice note, not a published rate.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| hapCon estimates contamination for male modern humans using haploid X chromosomes | doi:10.1093/bioinformatics/btac390 | Abstract / results sentences quoted above | Full text (PMC9344841) |
| README: hapCon estimates contamination for male aDNA samples | https://github.com/hringbauer/hapROH | README sentence quoted above | README (2,332 bytes) |
| A grape recipe based on hapCon | — | — | Not in the opened sources; **not claimed** |
| AuthentiCT: present-day contamination in ss-library aDNA from damage patterns; as few as 10,000 mapped sequences | doi:10.1186/s13059-020-02123-y | Abstract sentences quoted above | Abstract |
| AuthentiCT only for ss libraries; not for UDG-treated samples or deaminated-only filtered datasets; assumes contaminant is not deaminated | https://github.com/StephanePeyregne/AuthentiCT | README sentences quoted above | README (6,021 bytes) |
| Latorre et al. 2020 is a plant aDNA isolation, library and bioinformatics protocol | doi:10.1002/cppb.20121 | Title; abstract | Abstract |
| schmutzi contDeam can be used on nuclear as well as mitochondrial aDNA, at the user’s own risk, under the README Nuclear conditions; DICE is recommended for nuclear samples; the default candidate library is 197 human mitogenomes | doi:10.1186/s13059-015-0776-0 ; official README | Sentences quoted above, including “nuclear and mitonchondrial” [sic] and “use this at your own risk” | README re-fetched 2026-11-15 CST (38,285 bytes, sha256 e85cb02b…); EuropePMC abstract |
| Whether grape nuclear libraries meet the README conditions (molecule count, endogenous deamination, contaminant deamination, 5′/3′ independence) | — | — | Not tested in this update; **[待确认]** |
