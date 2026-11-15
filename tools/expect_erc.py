"""Exit non-zero unless a kicad-cli ERC JSON report holds exactly the expected findings.

usage: python3 tools/expect_erc.py <erc.json> [type=count ...]

Every finding type must appear exactly as often as given, and no other type may
appear at all, so a new warning fails the check as surely as a new error.
"""
import collections
import json
import sys

report, expected = sys.argv[1], dict(a.split("=") for a in sys.argv[2:])
expected = {k: int(v) for k, v in expected.items()}
found = collections.Counter(v["type"] for s in json.load(open(report))["sheets"] for v in s["violations"])
if found != collections.Counter(expected):
    print(f"expected {dict(sorted(expected.items()))}, found {dict(sorted(found.items()))}")
    sys.exit(1)
