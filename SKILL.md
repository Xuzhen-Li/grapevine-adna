---
name: grapevine-adna
description: >
  Ancient DNA processing and authentication for plants (grapevine-oriented).
  Use for aDNA FASTQ→BAM, damage, contamination, capture, or projecting
  ancient samples onto a modern panel. Not for modern GATK WGS.
---

# grapevine-adna

Plant aDNA is short, damaged, and lossy. Do not run a modern WGS recipe.

Canonical folders in this repo: [`damage/`](damage/), [`capture/`](capture/), [`projection/`](projection/).

## Red lines

1. Authenticate before popgen. No C→T / length / contamination check → do not interpret ancestry.
2. Expect 60–95% read loss from raw FASTQ to final BAM. Quote each step's yield.
3. Do not hard-filter rare alleles when the sample will be a reference-panel query.
4. Modern GATK HaplotypeCaller defaults are the wrong first tool.

## Pipeline order

```
FASTQ
  → AdapterRemoval --collapse
  → BWA aln -l 1024 -n 0.01
  → samtools view -q 30
  → fixmate + markdup
  → mapDamage2 (plot; rescale only if you understand the bias)
  → authenticate (damage + contamination + endogenous %)
  → call or genotype against a panel (ANGSD / pileup, not naive GATK)
  → project onto modern PCA / ADMIXTURE (do not rebuild the panel from n=1 ancient)
```

## Decisions

| Question | Default |
|----------|---------|
| SE vs PE collapse | collapse overlapping aDNA pairs |
| Seed length | disable seed (`-l 1024`) so damaged ends still map |
| Dupes | optical + PCR; aDNA duplication is usually extreme |
| Capture vs shotgun | capture if endogenous is tiny; still report off-target |
| Panel | project onto an existing grape panel; do not design a new chip here |

## Do not

- Treat mapDamage rescale as mandatory cleanup.
- Mix ancient and modern samples in one ADMIXTURE run without a projection design.
- Dump unpublished sample IDs or site coordinates into issues / README.

Related: `grapeancestry`, `vitis-popgen`, `bioinfo-pitfalls`.
