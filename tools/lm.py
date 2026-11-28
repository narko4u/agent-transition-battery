"""Shared DeepSeek client. No third-party imports, so any tool can use it.

The key is read from DEEPSEEK_API_KEY or ~/.hermes/secrets/deepseek.env and is
never printed. Spend is accumulated from the usage block on every call.
"""
import json
import os
import re
import time
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


class Meter:
    def __init__(self, cap_usd):
        self.cap = cap_usd
        self.usd = 0.0
        self.calls = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
        self.empties = 0
        self.key = api_key()

    def chat(self, system, user, max_tokens=2500, temperature=0.0):
        """One completion. Retries once with a bigger budget when the model spends
        the whole allocation on internal reasoning and returns no content, which
        DeepSeek does at small max_tokens and which silently reads as a wrong answer."""
        if self.usd >= self.cap:
            raise SystemExit("spend cap reached: $%.4f" % self.usd)
        content, finished = self._once(system, user, max_tokens, temperature)
        if not content.strip():
            self.empties += 1
            content, finished = self._once(system, user, min(max_tokens * 3, 6000), temperature)
            if not content.strip():
                self.empties += 1
        return content

    def _once(self, system, user, max_tokens, temperature):
        body = json.dumps({
            "model": MODEL,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }).encode()
        req = urllib.request.Request(
            BASE + "/chat/completions", data=body,
            headers={"Content-Type": "application/json",
                     "Authorization": "Bearer " + self.key})
        d = None
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    d = json.loads(r.read())
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(2 + 3 * attempt)
        if d is None:
            raise RuntimeError("no response from the endpoint")
        u = d.get("usage", {})
        self.prompt_tokens += u.get("prompt_tokens", 0)
        self.completion_tokens += u.get("completion_tokens", 0)
        self.usd = (self.prompt_tokens * IN_PER_M + self.completion_tokens * OUT_PER_M) / 1e6
        self.calls += 1
        ch = d["choices"][0]
        return (ch["message"].get("content") or ""), ch.get("finish_reason")
