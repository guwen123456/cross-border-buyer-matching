#!/usr/bin/env python3
"""One-click buyer/supplier matching check for the cross-border buyer matching skill.

Reads buyers.csv and suppliers.csv (headers from templates/), then prints a
Markdown report:
  - qualified buyers (match_score >= threshold), sorted by score
  - blocked buyers: score >= threshold but missing score_basis,
    personalization_detail, or a public contact (not cleared for outreach)
  - supplier candidates: suppliers not marked eliminated whose certification
    files have been checked

Stdlib only. Exit code 0 when nothing is blocked, 2 when blocked rows exist,
1 on usage or file errors.
"""
import csv
import sys

CHECKED_VALUES = {"yes", "y", "true", "1", "checked", "verified", "已核对", "是", "已验"}


def read_rows(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 1
    buyers_path, suppliers_path = argv[1], argv[2]
    threshold = 60
    if "--min-score" in argv:
        threshold = int(argv[argv.index("--min-score") + 1])

    buyers = read_rows(buyers_path)
    suppliers = read_rows(suppliers_path)

    qualified, blocked, below = [], [], []
    for b in buyers:
        if not (b.get("company_name") or "").strip():
            continue
        try:
            score = int(float(b.get("match_score") or 0))
        except ValueError:
            score = 0
        if score < threshold:
            below.append(b)
            continue
        problems = []
        if not (b.get("score_basis") or "").strip():
            problems.append("missing score_basis")
        if not (b.get("personalization_detail") or "").strip():
            problems.append("missing personalization_detail (the {Detail} anchor)")
        if not (b.get("public_contact") or "").strip():
            problems.append("missing public_contact")
        (blocked if problems else qualified).append((b, problems))

    qualified.sort(key=lambda x: -int(float(x[0].get("match_score") or 0)))

    candidates, eliminated = [], []
    for s in suppliers:
        if not (s.get("company_name") or "").strip():
            continue
        status = (s.get("status") or "").strip()
        cert_checked = (s.get("cert_files_checked") or "").strip().lower() in CHECKED_VALUES
        if "淘汰" in status or status.lower() == "eliminated":
            eliminated.append(s)
        elif cert_checked:
            candidates.append(s)

    print("# Matching report")
    print()
    print(f"Qualified buyers (>={threshold}, cleared for outreach): {len(qualified)}")
    for b, _ in qualified:
        print(f"- [{b.get('match_score')}] {b.get('company_name')} ({b.get('country', '')}) — {b.get('personalization_detail', '')}")
    print()
    print(f"Blocked buyers (>={threshold} but incomplete): {len(blocked)}")
    for b, problems in blocked:
        print(f"- {b.get('company_name')}: {'; '.join(problems)}")
    print()
    print(f"Below-threshold buyers kept on file: {len(below)}")
    print()
    print(f"Supplier candidates (cert files checked, not eliminated): {len(candidates)}")
    for s in candidates:
        print(f"- {s.get('company_name')} ({s.get('city', '')}) — {s.get('main_products', '')} / {s.get('model', '')}")
    print()
    print(f"Eliminated suppliers: {len(eliminated)}")
    return 2 if blocked else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
