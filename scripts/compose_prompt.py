#!/usr/bin/env python3
"""Compose a Bedrock Converse `system` array from the base, an agent file and the session template."""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLACE = re.compile(r"\{([A-Z][A-Z0-9_]*)\}")


def fill(text, values):
    missing = set()

    def rep(m):
        k = m.group(1)
        if k in values:
            return str(values[k])
        missing.add(k)
        return m.group(0)

    return PLACE.sub(rep, text), missing


def latest_version():
    base = ROOT / "prompts" / "enterprise-base"
    vs = sorted((p for p in base.glob("v*") if p.is_dir()),
                key=lambda p: tuple(int(x) for x in p.name[1:].split(".")))
    if not vs:
        sys.exit("No prompt versions found")
    return vs[-1].name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", required=True)
    ap.add_argument("--version", default=None, help="e.g. v1.1.0 (default: latest)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--single-checkpoint", action="store_true", help="omit the shared checkpoint after the base")
    ap.add_argument("--with-example-session", action="store_true", help="fill session context from session_example")
    a = ap.parse_args()

    ver = a.version or latest_version()
    vdir = ROOT / "prompts" / "enterprise-base" / ver
    agent = json.loads(pathlib.Path(a.agent).read_text(encoding="utf-8"))
    values = agent["values"]

    parts = {}
    for key, fname in (("base", "base.md"), ("agent", "agent-layer.template.md")):
        parts[key], missing = fill((vdir / fname).read_text(encoding="utf-8"), values)
        if missing:
            sys.exit("Unfilled placeholders in %s: %s" % (fname, ", ".join(sorted(missing))))

    session = (vdir / "session-context.template.md").read_text(encoding="utf-8")
    if a.with_example_session:
        session, _ = fill(session, agent.get("session_example", {}))

    cp = {"cachePoint": {"type": "default"}}
    system = [{"text": parts["base"]}]
    if not a.single_checkpoint:
        system.append(cp)
    system += [{"text": parts["agent"]}, cp, {"text": session}]

    out = pathlib.Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"prompt_version": ver, "agent": agent["name"], "system": system}, indent=2), encoding="utf-8")
    static_chars = len(parts["base"]) + len(parts["agent"])
    print("Composed %s (%s) -> %s" % (agent["name"], ver, out))
    print("Static prefix ~%d tokens (rough estimate). Session context is filled at request time." % (static_chars // 4))


if __name__ == "__main__":
    main()
