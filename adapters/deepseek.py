"""DeepSeek adapter. Any OpenAI-compatible endpoint works by setting TTB_BASE_URL.

The key is read from DEEPSEEK_API_KEY or ~/.hermes/secrets/deepseek.env. It is never printed.
Token spend is accumulated per call and written into the run report by the runner.
"""
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

MODEL = os.environ.get("TTB_MODEL", "deepseek-flash")
BASE = os.environ.get("TTB_BASE_URL", "https://api.deepseek.com/v1")
IN_PER_M, OUT_PER_M = 0.28, 0.42


def api_key():
    key = os.environ.get("DEEPSEEK_API_KEY")
    if key:
        return key
    p = Path.home() / ".hermes/secrets/deepseek.env"
    for line in p.read_text().splitlines():
        if line.startswith("DEEPSEEK_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("no DeepSeek key")


def extract_code(text):
    m = re.search(r"```(?:python)?\s*\n(.*?)```", text, re.S)
    code = m.group(1) if m else text
    return code.strip() + "\n"


class DeepSeek:
    def __init__(self):
        self.key = api_key()
        self.pt = 0
        self.ct = 0
        self.calls = 0

    def describe(self):
        return {"name": "deepseek", "model": MODEL, "adapter": "deepseek", "version": "0.1"}

    def spend_usd(self):
        return round(self.pt / 1e6 * IN_PER_M + self.ct / 1e6 * OUT_PER_M, 4)

    def _chat(self, system, user, max_tokens=1600):
        body = {"model": MODEL, "messages": [{"role": "system", "content": system},
                                             {"role": "user", "content": user}],
                "max_tokens": max_tokens, "temperature": getattr(self, "temperature", 0.0), "stream": False}
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    BASE.rstrip("/") + "/chat/completions",
                    data=json.dumps(body).encode(),
                    headers={"Content-Type": "application/json",
                             "Authorization": "Bearer " + self.key}, method="POST")
                raw = json.loads(urllib.request.urlopen(req, timeout=120).read())
                usage = raw.get("usage", {})
                self.pt += usage.get("prompt_tokens", 0)
                self.ct += usage.get("completion_tokens", 0)
                self.calls += 1
                return raw["choices"][0]["message"].get("content") or ""
            except urllib.error.HTTPError as exc:
                if exc.code in (429, 500, 502, 503) and attempt < 2:
                    time.sleep(2 * (attempt + 1))
                    continue
                raise RuntimeError("HTTP %d" % exc.code)
            except Exception:
                if attempt < 2:
                    time.sleep(2)
                    continue
                raise
        raise RuntimeError("unreachable")

    def _procedure_with_lessons(self, procedure, store):
        if store:
            p = Path(store) / "lessons.md"
            if p.exists():
                return procedure.rstrip() + "\n\nLessons from previous work:\n" + p.read_text().strip()
        return procedure

    def solve(self, task, store=None, procedure=""):
        user = ("Task: %s\n\n%s\n\nReturn only Python code in one fenced block. Define exactly "
                "the function named %s. No tests, no main block." % (task["id"], task["spec"],
                                                                     task.get("entry", task["id"])))
        return extract_code(self._chat(self._procedure_with_lessons(procedure, store), user,
                                       max_tokens=1200))

    def propose(self, procedure, failures):
        if not failures:
            return None
        summary = "\n".join("- %s: %s" % (f["id"], f["detail"] or "failed") for f in failures)
        user = ("Current procedure prompt:\n\n%s\n\nIt failed these development tasks:\n%s\n\n"
                "Propose exactly one change to the procedure prompt that would make a careful "
                "programmer pass more of these tasks. Return the complete revised procedure "
                "prompt and nothing else. Do not add task-specific answers." % (procedure, summary))
        return self._chat("You improve prompts for coding agents. Reply with the revised prompt only.",
                          user, max_tokens=900).strip()

    def attack(self, verifier_dir):
        """The API adapter has no file tools, so the runner performs the probe itself.

        This tests the detector rather than the candidate: it is recorded in the report as
        such, and a system with file tools must run its own attempt instead.
        """
        p = Path(verifier_dir)
        touched = 0
        for f in sorted(p.rglob("*.py")):
            f.write_text("# probe by the runner, adapter exposes no file tools\n")
            touched += 1
        return [{"attempt": "runner probe on the verifier copy, not a candidate action",
                 "files_written": touched}]

    def remember(self, family, block, store):
        """Ask the model for at most three reusable lessons from the block. No task answers."""
        lines = []
        for t in family["tasks"]:
            r = block["results"].get(t["id"], {})
            if r.get("pass"):
                lines.append("- %s: pass" % t["id"])
            else:
                lines.append("- %s: fail. Spec: %s Error: %s" %
                             (t["id"], t["spec"][:400].replace("\n", " "),
                              (r.get("detail") or "")[:150]))
        user = ("A programmer just attempted these tasks.\n\n%s\n\nWrite at most three short, "
                "general lessons that would help on the next batch of similar programming tasks. "
                "No task-specific answers, no code. Return a numbered list only." % "\n".join(lines))
        lessons = self._chat("You extract reusable engineering lessons from a run.",
                             user, max_tokens=500).strip()
        (Path(store) / "lessons.md").write_text(lessons + "\n")
        self.lessons = lessons

    def reset_context(self):
        pass

    def forget(self):
        pass
