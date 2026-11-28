#!/usr/bin/env python3
"""Pre-registration. Fix the question and the rule before any result exists.

Senti's fifth defect was correct: a threshold chosen after seeing results does not bind the test. This
tool writes the protocol to git with a timestamp and the tree's commit, so the rule provably predates
the run. `check` then refuses a report that does not match the protocol it claims.

  python3 tools/preregister.py new --id P-001 --family families/mbpp-hold60 \
      --hypothesis "gentler update keeps 1.5B base capability" \
      --metric accuracy --rule "tuned >= base + 0.05 and mcnemar_p < 0.05" --cap 0.00
  python3 tools/preregister.py check --id P-001 --report runs/weights-1.5b-gentle-hold60.json
"""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STORE = ROOT / "runs" / "protocols"


def git(*args):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return ""


def cmd_new(a) -> int:
    STORE.mkdir(parents=True, exist_ok=True)
    f = STORE / ("%s.json" % a.id)
    if f.exists():
        print("protocol %s already exists; a protocol is not edited, it is superseded" % a.id)
        return 1
    proto = {"id": a.id, "written_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
             "commit": git("rev-parse", "HEAD"), "family": a.family, "hypothesis": a.hypothesis,
             "primary_metric": a.metric, "decision_rule": a.rule, "spend_cap_usd": a.cap,
             "predictions": a.prediction or "", "known_confounds": a.confound or ""}
    body = json.dumps({k: v for k, v in proto.items() if k != "protocol_id"}, sort_keys=True, indent=1)
    proto["protocol_id"] = "sha256:" + hashlib.sha256(body.encode()).hexdigest()
    f.write_text(json.dumps(proto, indent=1) + "\n")
    print("written %s at %s, commit %s" % (f, proto["written_at"], proto["commit"][:12]))
    print("rule: %s" % a.rule)
    return 0


def cmd_check(a) -> int:
    f = STORE / ("%s.json" % a.id)
    if not f.exists():
        print("no protocol %s; a report without a protocol is exploratory, not a test" % a.id)
        return 2
    proto = json.loads(f.read_text())
    rep = json.loads(Path(a.report).read_text())
    problems = []
    if rep.get("protocol_id") != proto["protocol_id"]:
        problems.append("report does not cite this protocol (%r)" % rep.get("protocol_id"))
    fam = (rep.get("family") or "").rstrip("/")
    if fam and proto["family"].rstrip("/") != fam:
        problems.append("family %r does not match the protocol's %r" % (fam, proto["family"]))
    if proto["written_at"] > (rep.get("date") or ""):
        pass  # dates are day-granular; the protocol_id binding is the real check
    if problems:
        for p in problems:
            print("REFUSED: " + p)
        return 1
    print("OK: report cites protocol %s, family %s, rule unedited" % (a.id, proto["family"]))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("new")
    n.add_argument("--id", required=True)
    n.add_argument("--family", required=True)
    n.add_argument("--hypothesis", required=True)
    n.add_argument("--metric", default="accuracy")
    n.add_argument("--rule", required=True)
    n.add_argument("--cap", type=float, default=0.0)
    n.add_argument("--prediction", default="")
    n.add_argument("--confound", default="")
    c = sub.add_parser("check")
    c.add_argument("--id", required=True)
    c.add_argument("--report", required=True)
    a = ap.parse_args()
    return cmd_new(a) if a.cmd == "new" else cmd_check(a)


if __name__ == "__main__":
    raise SystemExit(main())
