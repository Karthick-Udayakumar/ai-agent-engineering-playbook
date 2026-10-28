#!/usr/bin/env python3
"""Minimal evaluation runner. Use --dry-run without AWS access. Replace with your own harness at scale."""
import argparse, json, os, pathlib, sys

BASE_FIELDS = ("status", "confidence", "evidence_refs", "flags")


def load_cases(path):
    cases = []
    for i, line in enumerate(pathlib.Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            c = json.loads(line)
        except json.JSONDecodeError as e:
            sys.exit("%s:%d invalid JSON: %s" % (path, i, e))
        for k in ("id", "input"):
            if k not in c:
                sys.exit("%s:%d missing %r" % (path, i, k))
        cases.append(c)
    return cases


def check(case, out_text):
    exp = case.get("expect", {})
    try:
        data = json.loads(out_text)
    except Exception:
        return ["output is not valid JSON"]
    problems = ["missing base field %s" % f for f in BASE_FIELDS if f not in data]
    if "expect_status" in exp and data.get("status") not in exp["expect_status"]:
        problems.append("status %r not in %s" % (data.get("status"), exp["expect_status"]))
    for s in exp.get("must_not_contain", []):
        if s.lower() in out_text.lower():
            problems.append("output contains forbidden text %r" % s)
    if exp.get("must_flag") and not data.get("flags"):
        problems.append("expected a non-empty flags list")
    return problems


def call_model(system_blocks, user_text, model_id):
    import boto3  # imported lazily so --dry-run needs no dependencies
    brt = boto3.client("bedrock-runtime")
    msgs = [{"role": "user", "content": [{"text": "<untrusted_input>\n%s\n</untrusted_input>" % user_text}]}]
    r = brt.converse(modelId=model_id, system=system_blocks, messages=msgs,
                     inferenceConfig={"maxTokens": 1500, "temperature": 0})
    return "".join(b.get("text", "") for b in r["output"]["message"]["content"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--system", required=True)
    ap.add_argument("--cases", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--model-id", default=os.environ.get("BEDROCK_MODEL_ID"))
    a = ap.parse_args()

    spec = json.loads(pathlib.Path(a.system).read_text(encoding="utf-8"))
    cases = load_cases(a.cases)
    if a.dry_run:
        print("Dry run: %d cases, prompt %s, agent %s" % (len(cases), spec["prompt_version"], spec["agent"]))
        for c in cases:
            print("  -", c["id"], "| expects", c.get("expect", {}))
        return
    if not a.model_id:
        sys.exit("Set BEDROCK_MODEL_ID or pass --model-id")
    failed = 0
    for c in cases:
        out = call_model(spec["system"], c["input"], a.model_id)
        problems = check(c, out)
        print(("PASS " if not problems else "FAIL ") + c["id"], "; ".join(problems))
        failed += bool(problems)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
