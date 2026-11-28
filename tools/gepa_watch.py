#!/usr/bin/env python3
"""A tiny live view of a running GEPA optimisation.

  python3 tools/gepa_watch.py --run-dir /home/vault/work/gepa-practice60 --port 8077

Serves one auto-refreshing page. No dependencies, reads files only.
"""
import argparse
import html
import json
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ARGS = None


def tail(path, n=45):
    try:
        lines = Path(path).read_text(errors="replace").splitlines()
    except FileNotFoundError:
        return "(no file yet: %s)" % path
    return "\n".join(lines[-n:]) or "(empty, the run has not flushed yet)"


def candidate_table(run_dir):
    rows = []
    cj = Path(run_dir) / "candidates.json"
    if cj.exists():
        try:
            cands = json.loads(cj.read_text())
        except Exception:
            cands = []
        for i, c in enumerate(cands if isinstance(cands, list) else []):
            text = c.get("instruction", "") if isinstance(c, dict) else str(c)
            rows.append((i, c.get("score", "") if isinstance(c, dict) else "", text[:220]))
        if rows:
            return rows
    for p in sorted(Path(run_dir).glob("**/gepa_state.json")):
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        cands = d.get("program_candidates") or d.get("candidates") or []
        scores = d.get("prog_candidate_val_subscores") or {}
        for i, c in enumerate(cands):
            text = c.get("instruction") if isinstance(c, dict) else str(c)
            sc = scores.get(str(i)) or scores.get(i)
            if isinstance(sc, dict):
                vals = [v for v in sc.values() if isinstance(v, (int, float))]
                sc = round(sum(vals) / len(vals), 4) if vals else ""
            rows.append((i, sc, (text or "")[:220]))
    return rows


def page():
    run_dir = ARGS.run_dir
    log = Path(run_dir) / "run_log.txt"
    size = log.stat().st_size if log.exists() else 0
    age = int(time.time() - log.stat().st_mtime) if log.exists() else -1
    rows = candidate_table(run_dir)
    body = ["<meta http-equiv='refresh' content='5'>"]
    body.append("<h2>GEPA live: %s</h2>" % html.escape(str(run_dir)))
    body.append("<p>log %d bytes, last write %ss ago, refreshed %s</p>"
                % (size, age, time.strftime("%H:%M:%S")))
    if rows:
        body.append("<table border=1 cellpadding=4><tr><th>#</th><th>score</th>"
                    "<th>instruction (first 220 chars)</th></tr>")
        for i, sc, text in rows:
            body.append("<tr><td>%s</td><td>%s</td><td><pre>%s</pre></td></tr>"
                        % (i, html.escape(str(sc)), html.escape(text)))
        body.append("</table>")
    else:
        body.append("<p>No candidate state written yet. GEPA writes it on the first accepted proposal.</p>")
    body.append("<h3>Run log</h3><pre>%s</pre>" % html.escape(tail(log)))
    return ("<html><head><title>GEPA live</title></head><body style='background:#111;"
            "color:#ddd;font-family:monospace;padding:16px'>" + "".join(body) + "</body></html>")


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        out = page().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

    def log_message(self, *a):
        pass


def main():
    global ARGS
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-dir", default="/home/vault/work/gepa-practice60")
    ap.add_argument("--port", type=int, default=8077)
    ARGS = ap.parse_args()
    print("serving http://0.0.0.0:%d for %s" % (ARGS.port, ARGS.run_dir), flush=True)
    ThreadingHTTPServer(("0.0.0.0", ARGS.port), H).serve_forever()


if __name__ == "__main__":
    main()
