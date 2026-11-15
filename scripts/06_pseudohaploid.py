#!/usr/bin/env python3
"""Random-draw pseudo-haploid calls from a toy pileup-like TSV.

Inputs:  --pileup-tsv with columns chrom,pos,bases and optional qual
         --seed
         optional --transversions-only, --min-base-quality,
         --alleles-tsv (chrom,pos,ref,alt), --ref FASTA (only with
         --alleles-tsv), --biallelic-ref and --biallelic-alt (a single
         pair for all sites; cannot be combined with --alleles-tsv)
Outputs: --calls-tsv with chrom,pos,call,n_reads
Tested:  synthetic pileup (defaults leave the toy behaviour unchanged);
         06_test_transversions.py checks site-level transversion filtering
         and allele-table validation.
Production: ANGSD or pileupCaller; for single-stranded libraries use
pileupCaller --singleStrandMode (docs/WORKFLOW.md). Other pileupCaller
parameter names for random-draw, transversion-only and BQ/MAPQ cuts
remain [待确认]. Production calls should use a minimum base quality and
MAPQ, keep only the two panel alleles, and, on non-UDG data, restrict
to transversions after terminal trimming or rescaling. Drawing a random
read at a damaged transition site will treat C-to-T or G-to-A as a real
allele. --transversions-only classifies each site from the panel ref/alt
in --alleles-tsv and skips transition sites entirely; it does not drop
individual alt reads that form a transition against the reference, which
would bias calls toward the reference. Alleles-tsv rows must be biallelic
single bases (A/C/G/T); multiallelic, indel, N, ref==alt, or duplicate
(chrom,pos) rows are rejected. --ref requires --alleles-tsv; --ref
without --alleles-tsv is an error. If both are given, the panel ref
must match the FASTA base at that position. Pseudo-haploid calls must not be used as a heterozygosity
estimate. Mixture-test thresholds stay [待确认].
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

TRANSITIONS = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
BASES = set("ACGT")


def read_ref(path: Path):
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


def read_alleles(path: Path):
    table = {}
    with path.open(encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        idx = {h: i for i, h in enumerate(header)}
        for need in ("chrom", "pos", "ref", "alt"):
            if need not in idx:
                raise SystemExit(f"--alleles-tsv missing column {need}")
        for lineno, line in enumerate(f, start=2):
            if not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            chrom = cols[idx["chrom"]]
            pos = cols[idx["pos"]]
            ref = cols[idx["ref"]].upper()
            alt = cols[idx["alt"]].upper()
            if ref not in BASES or alt not in BASES:
                raise SystemExit(
                    f"--alleles-tsv line {lineno} ({chrom}:{pos}): "
                    f"ref and alt must be single A/C/G/T bases, got ref={ref!r} alt={alt!r}"
                )
            if ref == alt:
                raise SystemExit(
                    f"--alleles-tsv line {lineno} ({chrom}:{pos}): ref and alt are the same"
                )
            key = (chrom, pos)
            if key in table:
                raise SystemExit(
                    f"--alleles-tsv line {lineno}: duplicate panel row for {chrom}:{pos}"
                )
            table[key] = (ref, alt)
    return table


def fasta_base(ref, chrom, pos):
    seq = ref.get(chrom)
    if seq is None:
        return None
    p = int(pos) - 1
    if p < 0 or p >= len(seq):
        return None
    return seq[p]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pileup-tsv", required=True)
    ap.add_argument("--calls-tsv", required=True)
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--ref", help="reference FASTA used only with --alleles-tsv; panel ref must match it")
    ap.add_argument("--transversions-only", action="store_true",
                    help="skip transition sites entirely; requires --alleles-tsv")
    ap.add_argument("--alleles-tsv",
                    help="panel alleles: chrom,pos,ref,alt; required with --transversions-only")
    ap.add_argument("--min-base-quality", type=int, default=None,
                    help="Phred cutoff if a qual column is present; otherwise ignored")
    ap.add_argument("--biallelic-ref")
    ap.add_argument("--biallelic-alt")
    args = ap.parse_args()
    if args.transversions_only and not args.alleles_tsv:
        raise SystemExit("--transversions-only requires --alleles-tsv with per-site ref and alt")
    if args.ref and not args.alleles_tsv:
        raise SystemExit("--ref requires --alleles-tsv; --ref without a panel is an error")
    if args.alleles_tsv and (args.biallelic_ref or args.biallelic_alt):
        raise SystemExit(
            "--biallelic-ref/--biallelic-alt cannot be combined with --alleles-tsv; "
            "per-site alleles must not be overridden"
        )
    if (args.biallelic_ref and not args.biallelic_alt) or (args.biallelic_alt and not args.biallelic_ref):
        raise SystemExit("--biallelic-ref and --biallelic-alt must be used together")
    ref = read_ref(Path(args.ref)) if args.ref else {}
    alleles = read_alleles(Path(args.alleles_tsv)) if args.alleles_tsv else {}
    if args.ref and args.alleles_tsv:
        for (chrom, pos), (ref_a, alt_a) in alleles.items():
            fb = fasta_base(ref, chrom, pos)
            if fb is None or fb not in BASES:
                raise SystemExit(f"--ref has no usable base for panel site {chrom}:{pos}")
            if fb != ref_a:
                raise SystemExit(
                    f"--ref base {fb} at {chrom}:{pos} does not match panel ref {ref_a}"
                )
    allowed_global = None
    if args.biallelic_ref and args.biallelic_alt:
        br, ba = args.biallelic_ref.upper(), args.biallelic_alt.upper()
        if br not in BASES or ba not in BASES:
            raise SystemExit("--biallelic-ref and --biallelic-alt must be single A/C/G/T bases")
        allowed_global = {br, ba}
    rng = np.random.default_rng(args.seed)
    rows = []
    with Path(args.pileup_tsv).open(encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        idx = {h: i for i, h in enumerate(header)}
        for line in f:
            cols = line.rstrip("\n").split("\t")
            chrom, pos = cols[idx["chrom"]], cols[idx["pos"]]
            bases = cols[idx["bases"]].upper()
            quals = cols[idx["qual"]] if "qual" in idx and idx["qual"] < len(cols) else ""
            site_alleles = alleles.get((chrom, pos))
            if args.transversions_only:
                if site_alleles is None:
                    rows.append([chrom, pos, ".", 0])
                    continue
                ref_a, alt_a = site_alleles
                if (ref_a, alt_a) in TRANSITIONS:
                    rows.append([chrom, pos, ".", 0])
                    continue
            if site_alleles is not None:
                allowed = {site_alleles[0], site_alleles[1]}
            else:
                allowed = allowed_global
            kept = []
            for i, b in enumerate(bases):
                if args.min_base_quality is not None and quals:
                    if i >= len(quals):
                        continue
                    if ord(quals[i]) - 33 < args.min_base_quality:
                        continue
                if allowed is not None and b not in allowed:
                    continue
                kept.append(b)
            if not kept:
                rows.append([chrom, pos, ".", 0])
                continue
            call = kept[int(rng.integers(0, len(kept)))]
            rows.append([chrom, pos, call, len(kept)])
    with Path(args.calls_tsv).open("x", encoding="utf-8") as f:
        f.write("chrom\tpos\tcall\tn_reads\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    print("sites", len(rows))


if __name__ == "__main__":
    main()
