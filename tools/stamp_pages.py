#!/usr/bin/env python3
"""Stamp 'n / N' page numbers at the bottom centre of a PDF, in place.

Usage: python stamp_pages.py PAPER.pdf
Requires pypdf and reportlab (see ~/.venvs/pdf).
"""
import io
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def main() -> int:
    path = Path(sys.argv[1])
    writer = PdfWriter(clone_from=str(path))
    total = len(writer.pages)
    for i, page in enumerate(writer.pages, start=1):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        c.setFont("Helvetica", 8)
        c.setFillGray(0.45)
        c.drawCentredString(A4[0] / 2, 12 * 2.83465, "%d / %d" % (i, total))
        c.save()
        buf.seek(0)
        page.merge_page(PdfReader(buf).pages[0])
    tmp = path.with_suffix(".stamped.pdf")
    with open(tmp, "wb") as fh:
        writer.write(fh)
    tmp.replace(path)
    print("stamped %d pages" % total)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
