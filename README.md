# grapevine-adna

Ancient-DNA methods for **Vitis**: damage, authentication, aDNA-specific capture, and projection onto modern panels.

## Layout

| Path | Role |
|------|------|
| [`damage/`](damage/) | C→T / length / contamination / endogenous checks before any popgen |
| [`capture/`](capture/) | aDNA-oriented capture notes (when shotgun endogenous is tiny) |
| [`projection/`](projection/) | Project authenticated ancients onto an existing modern panel |

## This is not

- Not the modern 167K FASTQ→report suite → [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry)
- Not chip / probe design → [grapeancestry/chip](https://github.com/Xuzhen-Li/grapeancestry/tree/main/chip) ([grapevine-chip](https://github.com/Xuzhen-Li/grapevine-chip) is a redirect)
- Not plastid-only assembly or phylogeny → [grapevine-plastid](https://github.com/Xuzhen-Li/grapevine-plastid)
- Not a general popgen theory folder → [genomics-theory-mining](https://github.com/Xuzhen-Li/genomics-theory-mining)

## What is here now

- Folder contract for damage vs capture vs projection
- Starter checklists and pipeline sketches (methods only)

Plant aDNA is short, damaged, and lossy. Do not run a modern WGS recipe here.

No unpublished genotypes, private coordinates, or sample-level matrices.

## See also

- [grapeancestry](https://github.com/Xuzhen-Li/grapeancestry) — modern 167K calling and ancestry
- [vitis-popgen](https://github.com/Xuzhen-Li/vitis-popgen) — structure / gene flow on public or published data
- [bioinfo-pitfalls](https://github.com/Xuzhen-Li/bioinfo-pitfalls) — symptom-first aDNA and VCF traps
- [bioinfo-agent-skills](https://github.com/Xuzhen-Li/bioinfo-agent-skills) — index of sibling repos

**Author:** Xuzhen Li · [ORCID](https://orcid.org/0000-0003-3670-6657)
