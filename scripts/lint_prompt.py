#!/usr/bin/env python3
"""Heuristic checks for prompt files. Review prompts, not verdicts. Exit 1 on blocking findings."""
import argparse, pathlib, re, sys

REQUIRED_BASE_TAGS = [
    "identity", "core_principles", "instruction_priority", "scope_boundary", "context_usage",
    "untrusted_content", "evidence_priority", "hallucination_prevention", "traceability",
    "confidence_framework", "escalation", "tool_usage", "privacy_and_access", "failure_handling",
    "completion_and_limits", "security",
]
SECRETS = [
    r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"ghp_[A-Za-z0-9]{30,}", r"sk-[A-Za-z0-9]{20,}",
    r"(?i)(api[_-]?key|password|secret|token)\s*[:=]\s*[^\s{]{8,}",
]


def est(s):
    return -(-len(s) // 4)


def lint(path, max_tokens):
    text = path.read_text(encoding="utf-8")
    fails, warns = [], []
    t = est(text)
    if t > max_tokens:
        warns.append("about %d tokens (limit %d): review for repetition" % (t, max_tokens))
    for pat in SECRETS:
        if re.search(pat, text):
            fails.append("possible secret or credential")
            break
    if "session-context" not in path.name and re.search(r"(?i)\b(today is|current date|20\d\d-\d\d-\d\d)\b", text):
        fails.append("volatile date in a static prompt file (breaks caching)")
    sents = [x.strip().lower() for x in re.split(r"[.!?\n]+", text) if len(x.strip()) > 20]
    dups = len(sents) - len(set(sents))
    if dups > 3:
        warns.append("%d repeated sentences" % dups)
    if path.name == "base.md":
        for tag in REQUIRED_BASE_TAGS:
            if "<%s>" % tag not in text or "</%s>" % tag not in text:
                fails.append("missing required section <%s>" % tag)
    return t, fails, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--max-tokens", type=int, default=2500)
    a = ap.parse_args()
    files = []
    for p in map(pathlib.Path, a.paths):
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]
    files = [f for f in files if f.name in ("base.md", "agent-layer.template.md", "session-context.template.md")]
    bad = 0
    for f in files:
        t, fails, warns = lint(f, a.max_tokens)
        print("%s  (~%d tokens)" % (f, t))
        for m in fails:
            print("  FAIL", m); bad += 1
        for m in warns:
            print("  warn", m)
        if not fails and not warns:
            print("  ok")
    if not files:
        sys.exit("No prompt files found")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
