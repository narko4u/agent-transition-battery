#!/usr/bin/env python3
"""Build the Zenodo deposit metadata from PAPER.md.

The abstract is extracted from the paper so the record and the PDF cannot drift.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
paper = (ROOT / "PAPER.md").read_text()
m = re.search(r"## Abstract\n\n(.+?)\n\n## 1\.", paper, re.S)
if not m:
    raise SystemExit("abstract not found")
abstract = " ".join(m.group(1).split())

meta = {
    "metadata": {
        "title": "Turning your AI Agent into an AGI Agent: a transition contract and a five-loop test battery",
        "upload_type": "publication",
        "publication_type": "preprint",
        "description": "<p>%s</p>" % abstract,
        "creators": [{"name": "Empire Labs Pty Ltd"}],
        "license": "cc-by-4.0",
        "keywords": ["AGI", "agents", "self-improvement", "evaluation", "verification",
                     "benchmark", "retention", "transfer"],
        "version": "0.1",
        "language": "eng",
        "related_identifiers": [{
            "relation": "isSupplementedBy",
            "identifier": "https://github.com/narko4u/agent-transition-battery",
            "resource_type": "software"}],
        "notes": ("Paper and specification CC BY 4.0. Code Apache-2.0. The battery is a "
                  "measurement instrument, not a product. Results in runs/ are executed "
                  "artefacts with hashes and spend.")
    }
}
(ROOT / "zenodo.json").write_text(json.dumps(meta, indent=1) + "\n")
print("wrote zenodo.json, abstract %d words" % len(abstract.split()))
