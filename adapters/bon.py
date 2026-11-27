#!/usr/bin/env python3
"""Best-of-N with self-generated tests, the CodeT idea reduced to what this box can afford.

Chen et al., CodeT (arXiv 2207.10397): sample many programs, generate tests from the same spec,
execute, and select by agreement rather than by the model's own confidence. This version samples
N candidates at temperature, writes one test set from the spec, scores every candidate against
it, and returns the highest scorer. Ties go to the shorter program.

It never sees the task's real tests or reference.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RUNNER = '''import sys, traceback
{code}

TESTS = {tests!r}
passed = 0
total = 0
for line in TESTS.splitlines():
    line = line.strip()
    if not line:
        continue
    total += 1
    try:
        exec(line, globals())
        passed += 1
    except Exception:
        pass
print("%d/%d" % (passed, total))
'''


class BestOfN:
    def __init__(self, inner, n=3, temperature=0.8):
        self.inner = inner
        self.n = n
        self.inner.temperature = temperature

    def describe(self):
        d = self.inner.describe()
        d["adapter"] = "bon%d" % self.n
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
        cands = [self.inner.solve(task, store, procedure) for _ in range(self.n)]
        cands = [c for c in cands if c and c.strip()]
        if not cands:
            return ""
        if len(cands) == 1:
            return cands[0]
        try:
            tests = self._tests(task, entry)
        except Exception:
            return cands[0]
        if not tests.strip():
            return cands[0]
        scored = [(self._score(c, tests), -len(c), i, c) for i, c in enumerate(cands)]
        scored.sort(reverse=True)
        return scored[0][3]

    def _tests(self, task, entry):
        user = ("Specification:\n%s\n\nWrite at most five assert statements testing the "
                "specification, including empty input and any stated error case. Use only `%s` "
                "and builtins. Output only the assert lines." % (task["spec"], entry))
        out = self.inner._chat("You write terse, correct Python assertions.", user, max_tokens=400)
        lines = [l.strip() for l in out.splitlines() if l.strip().startswith("assert ")]
        return "\n".join(lines[:5])

    def _score(self, code, tests):
        with tempfile.TemporaryDirectory(prefix="bon-") as tmp:
            f = Path(tmp) / "probe.py"
            f.write_text(RUNNER.format(code=code, tests=tests))
            try:
                p = subprocess.run([sys.executable, str(f)], capture_output=True, text=True,
                                   timeout=10, cwd=tmp)
            except subprocess.TimeoutExpired:
                return 0
            m = re.search(r"(\d+)/(\d+)", p.stdout or "")
            return int(m.group(1)) if m else 0
