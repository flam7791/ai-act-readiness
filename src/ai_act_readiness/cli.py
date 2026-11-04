"""Command line: `ai-act-readiness classify` for one use case, `report` for the portfolio pack."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from .classify import classify
from .readiness import build
from .render import as_json, markdown


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="ai-act-readiness")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("classify", help="classify the use cases in a portfolio file and print the proposals")
    c.add_argument("--portfolio", required=True, type=Path)

    r = sub.add_parser("report", help="build the executive readiness pack")
    r.add_argument("--portfolio", required=True, type=Path)
    r.add_argument("--evidence", required=True, type=Path)
    r.add_argument("--literacy", required=True, type=Path)
    r.add_argument("--as-of", required=True, type=date.fromisoformat)
    r.add_argument("--literacy-target", type=float, default=0.8,
                   help="internal coverage target for AI literacy (a policy choice, not a legal threshold)")
    r.add_argument("--out", type=Path, default=Path("out"))

    a = ap.parse_args(argv)
    data = json.loads(a.portfolio.read_text(encoding="utf-8"))
    org = data.get("organisation", "Organisation")

    if a.cmd == "classify":
        for uc in data["use_cases"]:
            res = classify(uc)
            print(f"{res.use_case_id:6} {res.category}")
            for reason in res.reasons:
                print(f"       - {reason}")
        return 0

    p = build(a.portfolio, a.evidence, a.literacy, a.as_of, a.literacy_target)
    a.out.mkdir(parents=True, exist_ok=True)
    md = a.out / f"readiness-{a.as_of.isoformat()}.md"
    md.write_text(markdown(p, org), encoding="utf-8")
    (a.out / f"readiness-{a.as_of.isoformat()}.json").write_text(as_json(p, org), encoding="utf-8")
    print(f"written {md} and its JSON twin: {len(p.use_cases)} use cases, {len(p.data_issues)} data issue(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
