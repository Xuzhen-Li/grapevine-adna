#!/usr/bin/env python3
"""Build a toy pileup TSV by exact placement of collapsed reads on a reference.

Inputs:  --collapsed-fa --ref
Outputs: --pileup-tsv (chrom, pos, bases)
Tested:  toy data.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
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
    ap.add_argument("--pileup-tsv", required=True)
    args = ap.parse_args()
    ref_recs = read_fa(Path(args.ref))
    chrom, ref = next(iter(ref_recs.items()))
    reads = read_fa(Path(args.collapsed_fa))
    columns = defaultdict(list)
    for seq in reads.values():
        start = ref.find(seq)
        if start < 0:
            start = ref.find(seq[3:])
            if start < 0:
                continue
            start = start - 3
            if start < 0:
                continue
        for k, b in enumerate(seq):
            columns[start + k].append(b)
    with Path(args.pileup_tsv).open("x", encoding="utf-8") as f:
        f.write("chrom\tpos\tbases\n")
        n = 0
        for pos in range(len(ref)):
            bases = "".join(columns.get(pos, []))
            if bases:
                f.write(f"{chrom}\t{pos+1}\t{bases}\n")
                n += 1
    print("pileup_sites", n)


if __name__ == "__main__":
    main()
