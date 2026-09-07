# Projection onto modern panels

Project authenticated ancient samples onto an **existing** modern panel. Do not rebuild the panel from n=1 ancient.

## Scope

- ANGSD / pileup-style genotype likelihoods vs naive GATK calls
- Project onto a locked modern PCA / ADMIXTURE space
- Mixing rules: ancient as query, modern as reference

## Out of scope

- Building or redesigning the modern chip → [grapeancestry/chip](https://github.com/Xuzhen-Li/grapeancestry/tree/main/chip)
- Modern capture calling reports → [grapeancestry/analysis](https://github.com/Xuzhen-Li/grapeancestry/tree/main/analysis)
- Theory dossiers → [genomics-theory-mining](https://github.com/Xuzhen-Li/genomics-theory-mining)

## Starter checklist

1. Authenticate first ([`../damage/`](../damage/)). No pass → no projection claim.
2. Choose the modern panel explicitly (e.g. 167K or a published Vitis set); document the panel version.
3. Prefer genotype likelihoods / pileup for low-coverage ancients; avoid hard-calling as the only path.
4. Do not mix ancient and modern samples in one ADMIXTURE run without a projection design.
5. No unpublished sample matrices in this repo — methods and public demo IDs only.

## Pipeline sketch

```
authenticated BAM
  → genotype likelihoods vs locked panel sites
  → project onto modern PCA / ADMIXTURE
  → report with yield + authenticity metrics alongside ancestry
```
