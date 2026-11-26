"""Scripted adapters. They prove the runner end to end, not a model.

Modes are deterministic, so a conformance run is reproducible and can be committed.
  reference  always returns the task's reference solution
  broken     always raises
  partial    reference on half the tasks, chosen by a stable hash of the id
  learner    broken in block 1, then answers from the store in block 2 (exercises T1)
  improver   broken until the procedure carries a marker the improver adds (exercises T5)
"""
import zlib
from pathlib import Path


class Scripted:
    def __init__(self, mode="reference"):
        self.mode = mode
        self.explore = True

    def describe(self):
        return {"name": "scripted", "model": "none", "adapter": "scripted:" + self.mode,
                "version": "0.1"}

    def _broken(self, task):
        name = task.get("entry") or task["id"].replace("-", "_")
        return "def %s(*args, **kwargs):\n    raise NotImplementedError(%r)\n" % (name, task["id"])

    def _reference(self, task):
        if not task.get("reference"):
            raise RuntimeError("task %s has no reference implementation" % task["id"])
        return task["reference"]

    def solve(self, task, store=None, procedure=""):
        if self.mode == "reference":
            return self._reference(task)
        if self.mode == "broken":
            return self._broken(task)
        if self.mode == "partial":
            if self.explore and zlib.crc32(task["id"].encode()) % 2 == 0:
                return self._reference(task)
            return self._broken(task)
        if self.mode == "learner":
            p = Path(store) / (task["id"] + ".py") if store else None
            if p and p.exists():
                return p.read_text()
            if self.explore and zlib.crc32(task["id"].encode()) % 2 == 0:
                return self._reference(task)
            return self._broken(task)
        if self.mode == "improver":
            return self._reference(task) if "ALWAYS_RESTATE_THE_SPEC_BEFORE_CODING" in procedure else self._broken(task)
        raise ValueError(self.mode)

    def remember(self, family, block, store):
        store = Path(store)
        for task in family["tasks"]:
            if block["results"].get(task["id"], {}).get("pass"):
                (store / (task["id"] + ".py")).write_text(self._reference(task))

    def reset_context(self):
        self.explore = False

    def forget(self):
        pass

    def propose(self, procedure, failures):
        if self.mode == "improver":
            return procedure.rstrip() + "\n\nALWAYS_RESTATE_THE_SPEC_BEFORE_CODING\n"
        return None

    def attack(self, verifier_dir):
        if self.mode != "improver":
            return []
        target = Path(verifier_dir)
        n = 0
        try:
            for f in sorted(target.rglob("*")):
                if f.is_file() and f.name != "family.json":
                    f.write_text("# sabotaged by the scripted adversarial arm\n")
                    n += 1
            return [{"attempt": "rewrite every test file in the verifier copy", "files_written": n}]
        except Exception as exc:
            return [{"attempt": "rewrite every test file in the verifier copy",
                     "files_written": n, "error": str(exc)}]
