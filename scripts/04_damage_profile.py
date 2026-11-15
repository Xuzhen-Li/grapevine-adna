#!/usr/bin/env python3
"""Count C-to-T substitutions in the first N bases of collapsed reads vs a reference.

Inputs:  --collapsed-fa --ref --end-bases (default 3)
Outputs: --summary-tsv
Tested:  toy damaged reads (python alignment by first exact start search).
This toy counter only tallies 5-prime C-to-T. It does not count 3-prime G-to-A
(typical of double-stranded libraries) or 3-prime C-to-T (typical of
single-stranded libraries), and it has no UDG parameter. The simulator
(00_sim_damaged_fastq.py) also plants only 5-prime C-to-T, so the toy
damage pattern does not represent any real library type.
Production: mapDamage2 or DamageProfiler after bwa aln and DeDup, then
mitigate residual damage by library type and UDG (docs/WORKFLOW.md
decision 6). See 04b_damage_mitigation.sh for the documented commands.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def read_fa(path: Path):
    recs = {}
    name, seq = None, []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith(">"):
                if name is not None:
                    recs[name] = "".join(seq).upper()
                name = line[1:].strip().split()[0]
                seq = []
            else:
                seq.append(line.strip())
    if name is not None:
        recs[name] = "".join(seq).upper()
    return recs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--collapsed-fa", required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--summary-tsv", required=True)
    ap.add_argument("--end-bases", type=int, default=3)
    args = ap.parse_args()
    ref = next(iter(read_fa(Path(args.ref)).values()))
    reads = read_fa(Path(args.collapsed_fa))
    c_sites = ct = 0
    mapped = unmapped = 0
    for rid, seq in reads.items():
        start = ref.find(seq)  # exact, may fail if damaged
        if start < 0:
            # try ignoring first end-bases for location
            start = ref.find(seq[args.end_bases:])
            if start < 0:
                unmapped += 1
                continue
            start = start - args.end_bases
            if start < 0:
                unmapped += 1
                continue
        mapped += 1
        for k in range(min(args.end_bases, len(seq))):
            if start + k >= len(ref) or start + k < 0:
                continue
            if ref[start + k] == "C":
                c_sites += 1
                if seq[k] == "T":
                    ct += 1
    rate = (ct / c_sites) if c_sites else float("nan")
    with Path(args.summary_tsv).open("x", encoding="utf-8") as f:
        f.write("mapped\tunmapped\tc_sites_5prime\tct_changes\tct_rate\n")
        f.write(f"{mapped}\t{unmapped}\t{c_sites}\t{ct}\t{rate if rate == rate else 'NA'}\n")
    print("mapped", mapped, "ct_rate", rate)


if __name__ == "__main__":
    main()
