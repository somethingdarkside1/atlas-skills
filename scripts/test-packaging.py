#!/usr/bin/env python3
"""Check portable references and real stale/missing bundle failures in scratch copies."""
import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bundles", ROOT / "scripts/bundle-methods.py")
bundles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bundles)


class PackagingTests(unittest.TestCase):
    def test_current_generated_content_matches_canonical_sources(self):
        self.assertEqual(bundles.bundle(ROOT, True), [])

    def test_each_skill_keeps_its_file_dependencies_when_copied_alone(self):
        for skill in (ROOT / "skills").iterdir():
            if not skill.is_dir():
                continue
            with self.subTest(skill=skill.name), tempfile.TemporaryDirectory() as folder:
                dest = (Path(folder) / skill.name).resolve()
                shutil.copytree(skill, dest)
                for doc in dest.rglob("*.md"):
                    body = re.sub(r"```.*?```", "", doc.read_text(), flags=re.S)
                    for target in re.findall(r"\]\(([^)]+)\)", body):
                        if re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("#"):
                            continue
                        resolved = (doc.parent / unquote(target.split("#")[0])).resolve()
                        self.assertTrue(resolved.is_relative_to(dest), (doc, target))
                        self.assertTrue(resolved.exists(), (doc, target))

    def test_missing_and_changed_copies_are_detected_and_regenerated(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ("methods", "skills", "scripts"):
                shutil.copytree(ROOT / name, root / name, ignore=shutil.ignore_patterns("__pycache__"))
            missing = root / "skills/build-it/verification.md"
            stale = root / "skills/review-it/diagnosis.md"
            missing.unlink()
            stale.write_text("outdated method\n")
            errors = bundles.bundle(root, True)
            self.assertIn("skills/build-it/verification.md", errors)
            self.assertIn("skills/review-it/diagnosis.md", errors)
            self.assertEqual(bundles.bundle(root), [])
            self.assertEqual(bundles.bundle(root, True), [])


if __name__ == "__main__":
    unittest.main()
