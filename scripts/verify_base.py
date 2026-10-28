#!/usr/bin/env python3
"""Fail if a released base.md changed without a matching hash (locked-section integrity)."""
import argparse, hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = ROOT / "prompts" / "enterprise-base"


def digest(path):
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", metavar="VERSION", help="write the hash for a version, e.g. v1.2.0 (reviewed change only)")
    a = ap.parse_args()

    if a.update:
        d = BASE / a.update
        h = digest(d / "base.md")
        (d / "base.sha256").write_text(h + "  base.md\n", encoding="utf-8")
        print("Updated hash for", a.update, h)
        return

    bad = 0
    dirs = sorted(p for p in BASE.glob("v*") if p.is_dir())
    if not dirs:
        sys.exit("No versions found")
    for d in dirs:
        hf = d / "base.sha256"
        if not hf.exists():
            print("FAIL %s: missing base.sha256" % d.name); bad += 1; continue
        expected = hf.read_text(encoding="utf-8").split()[0]
        actual = digest(d / "base.md")
        mf = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
        if mf["version"] != d.name[1:]:
            print("FAIL %s: manifest version %s does not match directory" % (d.name, mf["version"])); bad += 1
        if expected != actual:
            print("FAIL %s: base.md changed. Create a new version directory, update CHANGELOG and get Governance approval." % d.name); bad += 1
        else:
            print("ok   %s base.md matches its recorded hash" % d.name)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
