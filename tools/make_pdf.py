#!/usr/bin/env python3
"""Render PAPER.md to PDF with the Windows Chrome binary.

Chrome is a Windows process, so the HTML and PDF are staged under C:\\VaultSentinel\\tmp and
copied back into WSL. No LaTeX, no pandoc.
"""
import shutil
import subprocess
import sys
from pathlib import Path

import markdown

CHROME = "/mnt/c/Program Files/Google/Chrome/Application/chrome.exe"
STAGE = Path("/mnt/c/VaultSentinel/tmp")

CSS = """
@page { size: A4; margin: 20mm 18mm 20mm 18mm; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.4pt; line-height: 1.42;
       color: #111; max-width: 100%; }
h1 { font-size: 19pt; line-height: 1.2; margin: 0 0 4mm 0; }
h1 + p em { font-size: 11.5pt; color: #333; }
h2 { font-size: 12.6pt; margin: 7mm 0 2mm 0; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 5mm 0 1.5mm 0; page-break-after: avoid; }
p { margin: 0 0 2.6mm 0; text-align: justify; hyphens: auto; }
ul, ol { margin: 0 0 2.6mm 0; padding-left: 6mm; }
li { margin-bottom: 1mm; }
table { border-collapse: collapse; width: 100%; font-size: 8.2pt; margin: 3mm 0 4mm 0;
        page-break-inside: auto; }
th, td { border: 0.4pt solid #999; padding: 1.1mm 1.6mm; vertical-align: top; text-align: left; }
th { background: #eee; }
tr { page-break-inside: avoid; }
blockquote { margin: 3mm 0 3mm 4mm; padding-left: 4mm; border-left: 1.6pt solid #bbb; color: #333; }
code, pre { font-family: 'Consolas', monospace; font-size: 8.6pt; }
pre { background: #f6f6f6; padding: 2mm; white-space: pre-wrap; }
a { color: #111; text-decoration: none; word-break: break-word; }
hr { border: none; border-top: 0.4pt solid #bbb; margin: 5mm 0; }
"""

TEMPLATE = """<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head>
<body>{body}</body></html>"""


def main() -> int:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("PAPER.md")
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("PAPER.pdf")
    text = src.read_text()
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    title = text.splitlines()[0].lstrip("# ").strip()
    STAGE.mkdir(parents=True, exist_ok=True)
    html = STAGE / "ttb-paper.html"
    pdf = STAGE / "ttb-paper.pdf"
    html.write_text(TEMPLATE.format(title=title, css=CSS, body=body), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf=%s" % str(pdf).replace("/mnt/c", "C:"),
                    "file:///%s" % str(html).replace("/mnt/c/", "C:/")],
                   check=True, capture_output=True, timeout=180)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(pdf, out)
    print("wrote", out, out.stat().st_size, "bytes")
    subprocess.run(["pdfinfo", str(out)])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
