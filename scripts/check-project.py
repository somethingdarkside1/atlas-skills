#!/usr/bin/env python3
"""Check Atlas's active planning graph and portable project documentation.

This checks project structure, not agent behavior or remote URLs. The validation
work package owns future distributable-format and behavioral checks.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        raise ValueError("missing frontmatter")
    fields = {}
    for line in match[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def check(root: Path) -> dict:
    errors: list[str] = []
    optional: set[str] = set()
    tasks: dict[str, dict] = {}
    graph: dict[str, list[str]] = {}
    parts: set[str] = set()
    part_graph: dict[str, list[str]] = {}
    map_text = (root / "MAP.md").read_text()
    sections = re.split(r"(?=^## )", map_text, flags=re.M)[1:]
    for section in sections:
        heading = section.splitlines()[0][3:]
        part = heading.lower().replace(" ", "-")
        if part in parts:
            errors.append(f"duplicate map part: {part}")
        parts.add(part)
        needed = re.search(r"^Needs: (.+)$", section, re.M)
        need_text = needed[1].rstrip(".") if needed else "none"
        part_graph[part] = [] if need_text == "none" else [x.strip() for x in need_text.split(",")]
        for field in ("**Status:**", "Needs:", "Open questions:", "Decisions:", "Plan:"):
            if not any(line.startswith(field) for line in section.splitlines()):
                errors.append(f"{part}: missing {field}")
        status = re.search(r"^\*\*Status:\*\* (\w+)$", section, re.M)
        if not status or status[1] not in {"sketched", "decided", "building", "done"}:
            errors.append(f"{part}: invalid map status")
        elif f'{part}["{heading}"]:::{status[1]}' not in map_text:
            errors.append(f"{part}: diagram node or status disagrees")
    for part, dependencies in part_graph.items():
        for dependency in dependencies:
            if dependency not in parts:
                errors.append(f"{part}: missing decision prerequisite {dependency}")
            if f"  {dependency} --> {part}" not in map_text:
                errors.append(f"{part}: missing diagram dependency {dependency}")
    part_visiting: list[str] = []
    part_seen: set[str] = set()

    def visit_part(node: str):
        if node in part_visiting:
            errors.append("part cycle: " + " -> ".join(part_visiting + [node]))
            return
        if node in part_seen:
            return
        part_visiting.append(node)
        for dependency in part_graph.get(node, []):
            visit_part(dependency)
        part_visiting.pop()
        part_seen.add(node)

    for part in part_graph:
        visit_part(part)
    for path in sorted((root / "plan").glob("*/*.md")):
        rel = str(path.relative_to(root))
        if path.parent.name not in parts:
            errors.append(f"{rel}: active part is absent from map")
        try:
            fields = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        headings = re.findall(r"^## (.+)$", path.read_text(), re.M)
        if path.name == "brief.md":
            if fields.get("part") != path.parent.name:
                errors.append(f"{rel}: brief part disagrees with folder")
            if headings != ["Problem", "Outcome", "Decisions", "Out of scope"]:
                errors.append(f"{rel}: invalid brief sections")
            continue
        name = re.fullmatch(r"([0-9]{2,})-([a-z0-9-]+)\.md", path.name)
        if not name:
            errors.append(f"{rel}: invalid task filename")
            continue
        identity = f"{path.parent.name}/{name[1]}"
        if identity in tasks:
            errors.append(f"duplicate task id: {identity}")
        tasks[identity] = {"path": path, "fields": fields}
        if fields.get("status") not in {"todo", "doing", "review", "done", "canceled"}:
            errors.append(f"{rel}: invalid task status")
        if fields.get("kind") not in {"decision", "build", "check", "release"}:
            errors.append(f"{rel}: invalid task kind")
        if headings != ["Delivers", "Check by", "Done when", "Delivered", "Review"]:
            errors.append(f"{rel}: invalid task sections")
        if not re.search(r"^- \[[ x]\] .+", path.read_text(), re.M):
            errors.append(f"{rel}: missing acceptance checks")
        try:
            blockers = json.loads(fields["blocked_by"])
            if not isinstance(blockers, list) or any(not isinstance(x, str) for x in blockers):
                raise ValueError("expected a list of quoted ids")
            graph[identity] = [x if "/" in x else f"{path.parent.name}/{x}" for x in blockers]
        except (ValueError, KeyError) as exc:
            errors.append(f"{rel}: invalid blockers ({exc})")
            graph[identity] = []
    for part in parts:
        if not (root / "plan" / part / "brief.md").is_file():
            errors.append(f"{part}: missing brief")
        if not any(key.startswith(part + "/") for key in tasks):
            errors.append(f"{part}: package has no tasks")
    for task, blockers in graph.items():
        for blocker in blockers:
            if blocker not in tasks:
                errors.append(f"{task}: missing blocker {blocker}")
            elif tasks[blocker]["fields"].get("status") == "canceled":
                errors.append(f"{task}: canceled blocker requires disposition: {blocker}")
    visiting: list[str] = []
    seen: set[str] = set()

    def visit(node: str):
        if node in visiting:
            errors.append("task cycle: " + " -> ".join(visiting[visiting.index(node):] + [node]))
            return
        if node in seen:
            return
        visiting.append(node)
        for blocker in graph.get(node, []):
            visit(blocker)
        visiting.pop()
        seen.add(node)

    for node in graph:
        visit(node)
    docs = [root / name for name in ("README.md", "INDEX.md", "CLAUDE.md", "GLOSSARY.md", "MAP.md", "skills/README.md")]
    for folder in ("plan", "glossary", "decisions", "notes"):
        docs.extend((root / folder).rglob("*.md"))
    links = 0
    for path in docs:
        if not path.is_file():
            errors.append(f"missing document: {path.relative_to(root)}")
            continue
        text = path.read_text()
        # Ignore code examples: their example paths are not live project links.
        visible = re.sub(r"```.*?```", "", text, flags=re.S)
        for match in re.finditer(r"\]\(([^)]+)\)", visible):
            target = match[1]
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            location = unquote(target.split("#", 1)[0])
            resolved = (path.parent / location).resolve()
            links += 1
            if resolved.is_relative_to(root / "reference"):
                optional.add(str(resolved.relative_to(root)))
                continue
            if not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing link {target}")
    archived = list((root / "notes/archive/2026-09-13-initial-review/plan").glob("*/*.md"))
    migration = (root / "plan/MIGRATION.md").read_text()
    for path in archived:
        if path.name != "brief.md":
            old_id = f"{path.parent.name}/{path.name.split('-', 1)[0]}"
            if f"[{old_id}]" not in migration:
                errors.append(f"unaccounted archived task: {old_id}")
    for manifest in ("plugin.json", "marketplace.json"):
        try:
            json.loads((root / ".claude-plugin" / manifest).read_text())
        except (ValueError, OSError) as exc:
            errors.append(f"invalid {manifest}: {exc}")
    agents = root / "AGENTS.md"
    if not agents.exists() or agents.resolve() != (root / "CLAUDE.md").resolve():
        errors.append("AGENTS.md must resolve to the shared CLAUDE.md instructions")
    ready = sorted(task for task in tasks if tasks[task]["fields"].get("status") == "todo" and all(b in tasks and tasks[b]["fields"].get("status") == "done" for b in graph[task]))
    return {"parts": len(parts), "tasks": len(tasks), "documents": len(docs), "local_links": links,
            "optional_ignored_reference_sources": len(optional), "ready_by_state": ready,
            "note": "Readiness still requires access to the accepted blocker outputs. Remote links and agent behavior are not tested.",
            "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    result = check(args.root.resolve())
    print(json.dumps(result, indent=2))
    return int(bool(result["errors"]))


if __name__ == "__main__":
    raise SystemExit(main())
