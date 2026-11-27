#!/usr/bin/env python3
"""Self-check adapter: solve, generate its own edge-case assertions, run them, repair once.

This is a capability change, not a prompt tweak. The model never sees the task's real tests or
its reference solution. It writes assertions from the spec alone, executes them against its own
code, and gets one repair round on failure.

Wrapping an inner adapter keeps the spend accounting honest.
"""
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


class SelfCheck:
    def __init__(self, inner):
        self.inner = inner

    def describe(self):
        d = self.inner.describe()
        d["adapter"] = "selfcheck"
        return d

    def spend_usd(self):
        return self.inner.spend_usd()

    def forget(self):
        if hasattr(self.inner, "forget"):
            self.inner.forget()

    def reset_context(self):
        if hasattr(self.inner, "reset_context"):
            self.inner.reset_context()

    def remember(self, family, block, store):
        return self.inner.remember(family, block, store)

    def solve(self, task, store=None, procedure=""):
        entry = task.get("entry") or task["id"]
        code = self.inner.solve(task, store, procedure)
        try:
            tests = self._write_tests(task, entry, code)
        except Exception:
            return code
        if not tests.strip():
            return code
        bad = self._run(code, entry, tests)
        if not bad:
            return code
        try:
            return self._repair(task, entry, code, tests, bad)
        except Exception:
            return code

    def _write_tests(self, task, entry, code):
        user = ("Specification:\n%s\n\nA candidate implementation:\n```python\n%s\n```\n\n"
                "Write at most four assert statements that test the specification's stated edge "
                "cases, especially empty input and input that must raise. Use only `%s` and "
                "builtins. Output only the assert lines, no prose, no imports, no function "
                "definitions." % (task["spec"], code, entry))
        out = self.inner._chat("You write terse, correct Python assertions.", user, max_tokens=400)
        lines = [l.strip() for l in out.splitlines()
                 if l.strip().startswith("assert ") or l.strip().startswith("with ")]
        return "\n".join(lines[:6])

    def _run(self, code, entry, tests):
        with tempfile.TemporaryDirectory(prefix="selfcheck-") as tmp:
            f = Path(tmp) / "probe.py"
            f.write_text(code + "\n\n" + tests + "\n")
            try:
                p = subprocess.run([sys.executable, str(f)], capture_output=True, text=True,
                                   timeout=10, cwd=tmp)
            except subprocess.TimeoutExpired:
                return "timeout"
            if p.returncode == 0:
                return ""
            return (p.stderr or p.stdout).strip()[-600:]

    def _repair(self, task, entry, code, tests, failure):
        user = ("Specification:\n%s\n\nYour implementation:\n```python\n%s\n```\n\nYour own "
                "assertions:\n%s\n\nThey failed with:\n%s\n\nReturn only corrected Python code in "
                "one fenced block, defining `%s`. Keep the behaviour the spec asks for."
                % (task["spec"], code, tests, failure, entry))
        out = self.inner._chat("You fix Python code against a failing assertion.", user,
                               max_tokens=1600)
        m = re.search(r"```(?:python)?\s*\n(.*?)```", out, re.S)
        fixed = (m.group(1) if m else out).strip()
        return fixed + "\n" if fixed else code
