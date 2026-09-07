# aDNA-specific capture

Use capture when shotgun endogenous fraction is tiny. Still report off-target.

## Scope

- When to prefer capture vs shotgun for plant / Vitis aDNA
- Capture vs modern 167K panel design (different jobs)
- Off-target reporting and bait-set notes (public resources only)

## Out of scope

- Modern 167K SNP / probe selection → [grapeancestry/chip](https://github.com/Xuzhen-Li/grapeancestry/tree/main/chip)
- Damage authentication → [`../damage/`](../damage/)
- PCA / ADMIXTURE projection → [`../projection/`](../projection/)

## Starter checklist

1. Lock the scientific question (authentication only vs projection onto a named modern panel).
2. Prefer published bait / probe resources; do not commit unpublished coordinates.
3. Report endogenous %, on-target fraction, and off-target briefly — not only “capture worked.”
4. After capture, still run the full [`../damage/`](../damage/) authentication path.

## Split

| Path | Job |
|------|-----|
| `grapeancestry/chip` | modern panel site / probe design |
| `grapevine-adna/capture` | aDNA-oriented capture decisions |
| `grapevine-adna/damage` | authenticate the library |
