#!/usr/bin/env python3
"""Generate or check self-contained method/helper copies in consumer skills."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


def bundle(root: Path, check: bool = False) -> list[str]:
    consumers = json.loads((root / "methods/consumers.json").read_text())
    errors = []
    destinations = set()
    for source, names in consumers.items():
        path = root / source
        content = path.read_bytes()
        sha = hashlib.sha256(content).hexdigest()
        marker = f"Generated from {source}; sha256={sha}. Edit the source and regenerate."
        if path.suffix == ".py":
            lines = content.splitlines(keepends=True)
            expected = lines[0] + ("# " + marker + "\n").encode() + b"".join(lines[1:])
        else:
            expected = ("<!-- " + marker + " -->\n\n").encode() + content
        for name in names:
            dest = root / "skills" / name / path.name
            if dest in destinations:
                raise ValueError(f"duplicate generated destination: {dest}")
            destinations.add(dest)
            if not (dest.parent / "SKILL.md").is_file():
                raise ValueError(f"unknown skill: {name}")
            if check:
                if not dest.is_file() or dest.read_bytes() != expected:
                    errors.append(str(dest.relative_to(root)))
            else:
                dest.write_bytes(expected)
    for path in (root / "skills").glob("*/*"):
        if path.is_file() and path.suffix in {".md", ".py"} and path not in destinations:
            if "Generated from " in path.read_text()[:250]:
                errors.append("orphan generated file: " + str(path.relative_to(root)))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = bundle(args.root, args.check)
    print("\n".join(errors) if errors else "Method bundles are current.")
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
