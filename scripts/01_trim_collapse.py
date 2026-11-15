#!/usr/bin/env python3
"""Collapse overlapping toy paired reads and drop reads shorter than a minimum length.

Inputs:  --r1 --r2 --min-length (default 30, matching docs/WORKFLOW.md)
Outputs: --collapsed-fa
Tested:  output of 00_sim_damaged_fastq.py (perfect overlap by construction).
Production: AdapterRemoval collapse, minimum length 30 (25 only in sensitivity analyses).
If R1 and the reverse complement of R2 disagree, the pair is counted and
skipped rather than silently taking R1.
"""
from __future__ import annotations

import argparse
from pathlib import Path

COMP = str.maketrans("ACGTNacgtn", "TGCANtgcan")


def iter_fq(path: Path):
    with path.open(encoding="utf-8") as f:
        while True:
            h = f.readline()
            if not h:
                break
            s = f.readline().strip()
            f.readline()
            f.readline()
            yield h.strip(), s


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--r1", required=True)
    ap.add_argument("--r2", required=True)
    ap.add_argument("--collapsed-fa", required=True)
    ap.add_argument("--min-length", type=int, default=30)
    args = ap.parse_args()
    n_keep = n_drop = n_disagree = 0
    with Path(args.collapsed_fa).open("x", encoding="utf-8") as out:
        for (h1, s1), (h2, s2) in zip(iter_fq(Path(args.r1)), iter_fq(Path(args.r2))):
            rc2 = s2.translate(COMP)[::-1]
            if s1 != rc2:
                n_disagree += 1
                continue
            seq = s1
            if len(seq) < args.min_length:
                n_drop += 1
                continue
            rid = h1[1:].split()[0].split("/")[0]
            out.write(f">{rid}\n{seq}\n")
            n_keep += 1
    print("kept", n_keep, "dropped_short", n_drop, "r1_r2_disagree", n_disagree)


if __name__ == "__main__":
    main()
