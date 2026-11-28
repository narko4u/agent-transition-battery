#!/usr/bin/env python3
"""Validate every report in runs/ and check its family hashes against the tree."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
bad = 0
for r in sorted((ROOT / "runs").glob("*.json")):
    try:
        rep = json.loads(r.read_text())
    except json.JSONDecodeError as e:
        print("FAIL %s: not JSON (%s)" % (r.name, e))
        bad += 1
        continue
    if rep.get("test") not in ("T1", "T2", "T3", "T5"):
        print("skip %s: not a run report (kind %r)" % (r.name, rep.get("kind")))
        continue
    p = subprocess.run([sys.executable, str(ROOT / "ttb.py"), "validate", str(r)],
                       capture_output=True, text=True)
    print(p.stdout.strip() or p.stderr.strip())
    bad += p.returncode
    for f in rep.get("families", []):
        if not isinstance(f, dict):
            print("  family entry is not an object: %r" % (f,))
            bad += 1
            continue
        d = ROOT / "families" / f["id"]
        if not d.exists():
            print("  missing family %s" % f["id"])
            bad += 1
            continue
        h = subprocess.run([sys.executable, str(ROOT / "ttb.py"), "hash-family", str(d)],
                           capture_output=True, text=True).stdout
        now = json.loads(h)["verifier_sha256"]
        if now != f["verifier_sha256"]:
            print("  family %s has changed since the report: %s -> %s"
                  % (f["id"], f["verifier_sha256"][:19], now[:19]))
            bad += 1
sys.exit(1 if bad else 0)
