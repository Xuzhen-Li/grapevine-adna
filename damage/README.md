# Damage and authentication

Authenticate before any ancestry or structure claim.

## Scope

- C→T / G→A damage patterns and fragment-length distributions
- Endogenous fraction and contamination estimates
- mapDamage2 plots; rescale only when the bias is understood
- Yield accounting (raw FASTQ → final BAM): expect large loss

## Out of scope

- Probe design → [grapeancestry/chip](https://github.com/Xuzhen-Li/grapeancestry/tree/main/chip)
- Modern panel calling → [grapeancestry/analysis](https://github.com/Xuzhen-Li/grapeancestry/tree/main/analysis)
- Projection recipes → [`../projection/`](../projection/)

## Starter checklist

1. Collapse overlapping PE reads (AdapterRemoval or equivalent) before mapping.
2. Map with aDNA-aware settings (e.g. BWA `aln` with long/disabled seed); do not start from GATK HaplotypeCaller defaults.
3. Dedup aggressively; aDNA duplication rates are often extreme.
4. Run damage + contamination + endogenous % **before** interpreting ancestry.
5. Quote per-step yields; 60–95% read loss from raw FASTQ to usable BAM is normal, not a failure by itself.
6. Keep unpublished sample IDs and site coordinates out of this repo.

## Red lines

- No C→T / length / contamination check → do not interpret ancestry.
- Do not treat mapDamage rescale as mandatory “cleanup.”
- Do not hard-filter rare alleles when the sample will be a reference-panel query.
