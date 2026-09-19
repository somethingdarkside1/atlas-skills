#!/usr/bin/env python3
"""Identify file output and task scope; optionally retain a recoverable copy.

Run --help. Identity is read-only. Retention writes only a new destination.
This does not judge acceptance or prove that a supplied file list is complete.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import stat
import sys


def digest(value: object) -> str:
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return "sha256:" + hashlib.sha256(data.encode()).hexdigest()


def project_path(root: Path, value: str) -> tuple[str, Path]:
    path = root / value
    resolved = path.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"path leaves project: {value}")
    # Preserve a symlink's project path in the identity; read its target's bytes.
    relative = Path(value)
    if relative.is_absolute():
        relative = relative.relative_to(root)
    if ".." in relative.parts:
        raise ValueError(f"use a project-relative path without '..': {value}")
    return relative.as_posix(), path


def file_record(root: Path, value: str) -> dict:
    name, path = project_path(root, value)
    if not path.is_file():
        raise ValueError(f"required file is missing or not regular: {name}")
    return {
        "path": name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "executable": bool(path.stat().st_mode & stat.S_IXUSR),
    }


def task_criteria(path: Path) -> dict[str, str]:
    text = path.read_text()
    sections: dict[str, list[str]] = {}
    current = None
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            run = marker[1]
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence):
                fence = None
            if current is not None:
                sections[current].append(line)
            continue
        heading = re.match(r"^## ([^\n]+)\s*$", line) if fence is None else None
        if heading:
            current = heading[1].strip()
            if current in sections:
                raise ValueError(f"duplicate task section: {current}")
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
    result = {}
    for name in ("Delivers", "Check by", "Done when"):
        if name not in sections:
            raise ValueError(f"task lacks {name}: {path.name}")
        result[name] = re.sub(r"(?m)^(\s*[-*] )\[[ xX]\]", r"\1[]", "".join(sections[name])).strip()
    return result


def receipt(root: Path, task: str, files: list[str], absent: list[str], scope: list[str]) -> dict:
    task_name, task_path = project_path(root, task)
    if not task_path.is_file():
        raise ValueError(f"missing task: {task_name}")
    records = {r["path"]: r for r in (file_record(root, p) for p in files)}
    removals = set()
    for value in absent:
        name, path = project_path(root, value)
        if path.exists() or path.is_symlink():
            raise ValueError(f"declared absent path still exists: {name}")
        removals.add(name)
    if not records and not removals:
        raise ValueError("name at least one output file or explicit removal")
    if set(records) & removals:
        raise ValueError("a path cannot be both present and absent")
    brief = task_path.parent / "brief.md"
    scope_paths = [str(brief.relative_to(root)), *scope]
    scope_records = {r["path"]: r for r in (file_record(root, p) for p in scope_paths)}
    # Exclude changing workflow state and checkbox ticks from the requirement identity.
    scope_value = {"task": task_name, "criteria": task_criteria(task_path),
                   "sources": sorted(scope_records.values(), key=lambda r: r["path"])}
    output_value = {"files": sorted(records.values(), key=lambda r: r["path"]),
                    "absent": sorted(removals)}
    return {"files": sorted(records), "absent": sorted(removals),
            "version": digest(output_value), "scope": digest(scope_value),
            "output_manifest": output_value, "scope_manifest": scope_value}


def retain(root: Path, result: dict, destination: str) -> str:
    name, target = project_path(root, destination)
    if target.exists():
        raise ValueError(f"retention destination already exists: {name}")
    target.mkdir(parents=True)
    try:
        for path in result["files"]:
            dest = target / "output" / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / path, dest)
        for source in result["scope_manifest"]["sources"]:
            dest = target / "scope" / source["path"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(root / source["path"], dest)
        (target / "receipt.json").write_text(json.dumps(result, indent=2) + "\n")
        # Check copied bytes against the receipt rather than claiming a raced copy succeeded.
        for record in result["output_manifest"]["files"]:
            actual = file_record(target / "output", record["path"])
            if actual != record:
                raise ValueError("output changed during retention; inspect partial copy")
        for record in result["scope_manifest"]["sources"]:
            if file_record(target / "scope", record["path"]) != record:
                raise ValueError("scope changed during retention; inspect partial copy")
    except Exception:
        # Keep a partial copy for inspection; never remove a user's destination on failure.
        raise
    return name


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--task", required=True, help="task path, such as plan/wordmark/02-build.md")
    parser.add_argument("--files", nargs="*", default=[], help="actual delivered files, quoted for spaces")
    parser.add_argument("--absent", nargs="*", default=[], help="explicit removed paths")
    parser.add_argument("--scope", nargs="*", default=[], help="additional requirements or decisions")
    parser.add_argument("--retain", help="new project-relative folder for a recoverable copy")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        result = receipt(root, args.task, args.files, args.absent, args.scope)
        retained = retain(root, result, args.retain) if args.retain else None
    except (OSError, ValueError) as error:
        print(f"Evidence unavailable: {error}", file=sys.stderr)
        return 1
    print("Files: " + json.dumps(result["files"], ensure_ascii=False))
    if result["absent"]:
        print("Absent: " + json.dumps(result["absent"], ensure_ascii=False))
    print("Version: " + result["version"])
    print("Scope: " + result["scope"])
    print("Scope files: " + json.dumps([r["path"] for r in result["scope_manifest"]["sources"]], ensure_ascii=False))
    if retained:
        print("Retained: " + retained)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
