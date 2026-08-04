#!/usr/bin/env python3
"""Check C### and S### closure for one topic directory."""

from __future__ import annotations

import re
import sys
from pathlib import Path


CLAIM_RE = re.compile(r"\bC\d{3}\b")
SOURCE_RE = re.compile(r"\bS\d{3}\b")


def ids(path: Path, pattern: re.Pattern[str]) -> set[str]:
    return set(pattern.findall(path.read_text(encoding="utf-8")))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: audit_claims.py topics/active/<slug>", file=sys.stderr)
        return 2

    topic = Path(sys.argv[1])
    claims_file = topic / "04-claims.md"
    sources_file = topic / "03-sources.md"
    master_file = topic / "script" / "master.md"
    required = (claims_file, sources_file, master_file)
    missing_files = [str(path) for path in required if not path.is_file()]
    if missing_files:
        print("missing required files:")
        for path in missing_files:
            print(f"- {path}")
        return 2

    defined_claims = ids(claims_file, CLAIM_RE)
    defined_sources = ids(sources_file, SOURCE_RE)
    claim_sources = ids(claims_file, SOURCE_RE)
    master_claims = ids(master_file, CLAIM_RE)

    unknown_sources = sorted(claim_sources - defined_sources)
    unknown_master_claims = sorted(master_claims - defined_claims)
    unused_claims = sorted(defined_claims - master_claims)

    print(f"defined claims: {len(defined_claims)}")
    print(f"defined sources: {len(defined_sources)}")
    print(f"claims used in master: {len(master_claims)}")

    failed = False
    if unknown_sources:
        failed = True
        print("unknown S### referenced by claims: " + ", ".join(unknown_sources))
    if unknown_master_claims:
        failed = True
        print("unknown C### referenced by master: " + ", ".join(unknown_master_claims))
    if unused_claims:
        print("note: claims not used in master: " + ", ".join(unused_claims))

    if failed:
        return 1
    print("claim/source closure: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
