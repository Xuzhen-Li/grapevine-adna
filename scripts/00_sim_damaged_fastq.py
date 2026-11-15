#!/usr/bin/env python3
"""Simulate tiny paired FASTQ with 5-prime C-to-T damage on a known reference.

Inputs:  --ref FASTA, --out-prefix, --n-reads, --seed, --damage-rate (end 3 bases)
Outputs: prefix_R1.fastq, prefix_R2.fastq, prefix_truth.tsv
Tested:  Python 3.13 + numpy.
This is a simulator, not gargammel. It is not real ancient grape data.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

COMP = str.maketrans("ACGTNacgtn", "TGCANtgcan")


def read_fa(path: Path) -> str:
    seq = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.strip().upper())
    return "".join(seq)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ref", required=True)
    ap.add_argument("--out-prefix", required=True)
    ap.add_argument("--n-reads", type=int, default=400)
    ap.add_argument("--len", type=int, default=40)
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--damage-rate", type=float, default=0.4)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    ref = read_fa(Path(args.ref))
    if len(ref) < args.len + 5:
        raise SystemExit("reference too short")
    r1_path = Path(args.out_prefix + "_R1.fastq")
    r2_path = Path(args.out_prefix + "_R2.fastq")
    tr_path = Path(args.out_prefix + "_truth.tsv")
    with r1_path.open("x", encoding="utf-8") as f1, r2_path.open("x", encoding="utf-8") as f2, tr_path.open("x", encoding="utf-8") as ft:
        ft.write("read_id\tstart\tstrand\tdamaged_sites\n")
        for i in range(args.n_reads):
            start = int(rng.integers(0, len(ref) - args.len))
            frag = list(ref[start:start + args.len])
            damaged = []
            # 5' C->T on first 3 positions of the sequenced fragment (R1)
            for k in range(min(3, len(frag))):
                if frag[k] == "C" and rng.random() < args.damage_rate:
                    frag[k] = "T"
                    damaged.append(str(k))
            seq = "".join(frag)
            # simple reverse complement R2 of the same fragment, no extra 3' G>A for this toy
            rc = seq.translate(COMP)[::-1]
            qual = "I" * args.len
            rid = f"r{i+1}"
            f1.write(f"@{rid}/1\n{seq}\n+\n{qual}\n")
            f2.write(f"@{rid}/2\n{rc}\n+\n{qual}\n")
            ft.write(f"{rid}\t{start}\t+\t{','.join(damaged) if damaged else 'none'}\n")
    print("reads", args.n_reads, "ref_len", len(ref))


if __name__ == "__main__":
    main()
