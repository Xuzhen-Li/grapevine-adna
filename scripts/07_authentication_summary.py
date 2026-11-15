#!/usr/bin/env python3
"""Combine toy damage-profile and mapping counts into a one-row authentication note.

Inputs:  --damage-tsv from 04_damage_profile.py --min-mapped (default 10)
Outputs: --summary-txt
Tested:  toy tables.
Production: use blanks, damage profiles, and independent evidence
(docs/WORKFLOW.md). Do not use human X-chromosome contamination modules
(hapCon). Do not invent mixture-test thresholds; they stay [待确认].
This script only restates the toy counts. It does not declare a sample authentic.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--damage-tsv", required=True)
    ap.add_argument("--summary-txt", required=True)
    ap.add_argument("--min-mapped", type=int, default=10)
    args = ap.parse_args()
    with Path(args.damage_tsv).open(encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        rec = dict(zip(header, f.readline().rstrip("\n").split("\t")))
    mapped = int(rec["mapped"])
    lines = [
        "Toy authentication summary (not a real ancient-sample verdict)",
        f"mapped={rec['mapped']} unmapped={rec['unmapped']}",
        f"5prime_C_sites={rec['c_sites_5prime']} CtoT={rec['ct_changes']} rate={rec['ct_rate']}",
        f"mapped_below_demo_floor={mapped < args.min_mapped} (floor={args.min_mapped} is a toy check only)",
        "Mixture-test numerical thresholds: [待确认]",
        "Do not use hapCon or other human X-chromosome contamination modules on grape.",
        "",
    ]
    with Path(args.summary_txt).open("x", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("wrote", args.summary_txt)


if __name__ == "__main__":
    main()
