#!/usr/bin/env python3
"""Prove site-level transversion filtering and allele-table validation.

Writes tiny pileups and panel tables, runs 06_pseudohaploid.py, and checks
the calls. Exit 0 on pass. Inputs: --out-dir (must already exist).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "06_pseudohaploid.py"


def write_x(path: Path, text: str):
    data = text if text.endswith("\n") else text + "\n"
    with path.open("x", encoding="utf-8") as f:
        f.write(data)


def parse_calls(path: Path):
    rows = {}
    with path.open(encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        for line in f:
            cols = line.rstrip("\n").split("\t")
            rec = dict(zip(header, cols))
            rows[(rec["chrom"], rec["pos"])] = rec
    return rows


def run_caller(args_list):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args_list],
        check=False,
        env={**dict(**{k: v for k, v in __import__("os").environ.items()}),
             "PYTHONDONTWRITEBYTECODE": "1"},
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    out = Path(args.out_dir)
    if not out.is_dir():
        raise SystemExit(f"--out-dir does not exist: {out}")
    errors = []

    # --- main transversion cases, plus off-panel base, missing site, A/G ---
    pileup = out / "tv_pileup.tsv"
    alleles = out / "tv_alleles.tsv"
    calls = out / "tv_calls.tsv"
    ref_fa = out / "tv_ref.fa"
    write_x(pileup, (
        "chrom\tpos\tbases\n"
        "chrT\t10\tCTTTT\n"
        "chrT\t20\tAAAAA\n"
        "chrT\t30\tCCACC\n"
        "chrT\t40\tCCAGC\n"
        "chrT\t50\tGGGGG\n"
        "chrT\t60\tACACA\n"
    ))
    write_x(alleles, (
        "chrom\tpos\tref\talt\n"
        "chrT\t10\tC\tT\n"
        "chrT\t20\tC\tA\n"
        "chrT\t30\tC\tA\n"
        "chrT\t40\tC\tA\n"
        "chrT\t50\tA\tG\n"
    ))
    # 60-base toy ref: 1-based positions 10,20,30,40,50,60 are C,C,C,C,A,A.
    # Position 60 is in the reference and the pileup, but not in the panel.
    seq = ["N"] * 60
    seq[9] = "C"
    seq[19] = "C"
    seq[29] = "C"
    seq[39] = "C"
    seq[49] = "A"
    seq[59] = "A"
    write_x(ref_fa, ">chrT\n" + "".join(seq) + "\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(alleles),
        "--ref", str(ref_fa),
        "--transversions-only",
        "--calls-tsv", str(calls),
        "--seed", "3",
    ])
    if proc.returncode != 0:
        errors.append(f"main transversion run exited {proc.returncode}")
    else:
        rows = parse_calls(calls)
        ts = rows.get(("chrT", "10"))
        if ts is None or ts["call"] != "." or ts["n_reads"] != "0":
            errors.append(f"C/T transition should be skipped, got {ts}")
        tv_alt = rows.get(("chrT", "20"))
        if tv_alt is None or tv_alt["call"] != "A" or tv_alt["n_reads"] != "5":
            errors.append(f"all-alt transversion should call A with 5 reads, got {tv_alt}")
        tv_mix = rows.get(("chrT", "30"))
        if tv_mix is None or tv_mix["n_reads"] != "5" or tv_mix["call"] not in {"C", "A"}:
            errors.append(f"mixed transversion should keep all 5 panel alleles, got {tv_mix}")
        off = rows.get(("chrT", "40"))
        if off is None or off["n_reads"] != "4" or off["call"] not in {"C", "A"}:
            errors.append(f"off-panel G at C/A site should be dropped (n_reads=4), got {off}")
        ag = rows.get(("chrT", "50"))
        if ag is None or ag["call"] != "." or ag["n_reads"] != "0":
            errors.append(f"A/G transition should be skipped, got {ag}")
        missing = rows.get(("chrT", "60"))
        if missing is None or missing["call"] != "." or missing["n_reads"] != "0":
            errors.append(f"site missing from the panel should be skipped, got {missing}")

    # --- default path unchanged: no transversions-only, transition is called ---
    default_calls = out / "default_calls.tsv"
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--calls-tsv", str(default_calls),
        "--seed", "3",
    ])
    if proc.returncode != 0:
        errors.append(f"default-path run exited {proc.returncode}")
    else:
        rows = parse_calls(default_calls)
        ts = rows.get(("chrT", "10"))
        if ts is None or ts["n_reads"] != "5" or ts["call"] not in {"C", "T"}:
            errors.append(f"default path should still call the C/T site, got {ts}")
        ag = rows.get(("chrT", "50"))
        if ag is None or ag["n_reads"] != "5" or ag["call"] != "G":
            errors.append(f"default path should call the all-G A/G site as G, got {ag}")
        missing = rows.get(("chrT", "60"))
        if missing is None or missing["n_reads"] != "5" or missing["call"] not in {"A", "C"}:
            errors.append(f"default path should call the unlisted site, got {missing}")

    # --- multiallelic row rejected ---
    bad_alleles = out / "bad_alleles.tsv"
    bad_calls = out / "bad_calls.tsv"
    write_x(bad_alleles, "chrom\tpos\tref\talt\nchrT\t20\tC\tA,G\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(bad_alleles),
        "--transversions-only",
        "--calls-tsv", str(bad_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("multiallelic alleles-tsv row should have been rejected")
    if bad_calls.exists():
        errors.append("multiallelic run should not have written calls")

    # --- biallelic global pair must not override alleles-tsv ---
    conflict_calls = out / "conflict_calls.tsv"
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(alleles),
        "--biallelic-ref", "C",
        "--biallelic-alt", "A",
        "--transversions-only",
        "--calls-tsv", str(conflict_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("--biallelic-ref/alt plus --alleles-tsv should have been rejected")
    if conflict_calls.exists():
        errors.append("conflicting --biallelic-ref/alt run should not have written calls")

    # --- --ref base disagrees with panel ref ---
    mismatch_ref = out / "mismatch_ref.fa"
    mismatch_calls = out / "mismatch_calls.tsv"
    bad_seq = ["N"] * 60
    bad_seq[9] = "T"
    bad_seq[19] = "C"
    bad_seq[29] = "C"
    bad_seq[39] = "C"
    bad_seq[49] = "A"
    bad_seq[59] = "A"
    write_x(mismatch_ref, ">chrT\n" + "".join(bad_seq) + "\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(alleles),
        "--ref", str(mismatch_ref),
        "--transversions-only",
        "--calls-tsv", str(mismatch_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("--ref mismatch with panel ref should have been rejected")
    if mismatch_calls.exists():
        errors.append("--ref mismatch run should not have written calls")

    # --- ref == alt ---
    same_alleles = out / "same_alleles.tsv"
    same_calls = out / "same_calls.tsv"
    write_x(same_alleles, "chrom\tpos\tref\talt\nchrT\t20\tC\tC\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(same_alleles),
        "--transversions-only",
        "--calls-tsv", str(same_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("ref==alt alleles-tsv row should have been rejected")
    if same_calls.exists():
        errors.append("ref==alt run should not have written calls")

    # --- N and indel rows ---
    n_alleles = out / "n_alleles.tsv"
    n_calls = out / "n_calls.tsv"
    write_x(n_alleles, "chrom\tpos\tref\talt\nchrT\t20\tC\tN\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(n_alleles),
        "--transversions-only",
        "--calls-tsv", str(n_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("N allele row should have been rejected")
    if n_calls.exists():
        errors.append("N allele run should not have written calls")
    indel_alleles = out / "indel_alleles.tsv"
    indel_calls = out / "indel_calls.tsv"
    write_x(indel_alleles, "chrom\tpos\tref\talt\nchrT\t20\tC\tAT\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(indel_alleles),
        "--transversions-only",
        "--calls-tsv", str(indel_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("indel alleles-tsv row should have been rejected")
    if indel_calls.exists():
        errors.append("indel run should not have written calls")

    # --- --ref without --alleles-tsv must error ---
    ref_only_calls = out / "ref_only_calls.tsv"
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--ref", str(ref_fa),
        "--calls-tsv", str(ref_only_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("--ref without --alleles-tsv should have been rejected")
    if ref_only_calls.exists():
        errors.append("--ref without --alleles-tsv should not have written calls")

    # --- duplicate panel rows must error ---
    dup_alleles = out / "dup_alleles.tsv"
    dup_calls = out / "dup_calls.tsv"
    write_x(dup_alleles, "chrom\tpos\tref\talt\nchrT\t20\tC\tA\nchrT\t20\tC\tA\n")
    proc = run_caller([
        "--pileup-tsv", str(pileup),
        "--alleles-tsv", str(dup_alleles),
        "--transversions-only",
        "--calls-tsv", str(dup_calls),
        "--seed", "3",
    ])
    if proc.returncode == 0:
        errors.append("duplicate panel rows should have been rejected")
    if dup_calls.exists():
        errors.append("duplicate panel run should not have written calls")

    report = out / "tv_test_report.txt"
    if errors:
        write_x(report, "FAIL\n" + "\n".join(errors) + "\n")
        raise SystemExit("06_test_transversions.py FAIL: " + "; ".join(errors))
    write_x(report, (
        "PASS\n"
        "chrT:10 C/T transition skipped\n"
        "chrT:20 C/A all-alt calls A with n_reads=5\n"
        "chrT:30 C/A mixed keeps n_reads=5\n"
        "chrT:40 off-panel G dropped, n_reads=4\n"
        "chrT:50 A/G transition skipped\n"
        "chrT:60 missing panel site skipped\n"
        "default path still calls transition and unlisted sites\n"
        "multiallelic row rejected\n"
        "--biallelic-ref/alt cannot override --alleles-tsv\n"
        "--ref mismatch rejected and no calls written\n"
        "ref==alt row rejected\n"
        "N and indel rows rejected\n"
        "--ref without --alleles-tsv rejected\n"
        "duplicate panel rows rejected\n"
    ))
    print("transversion site-level test PASS")


if __name__ == "__main__":
    main()
