#!/usr/bin/env python3
"""Regression checks for evidence identity and recoverability, in temporary projects."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("evidence", Path(__file__).with_name("evidence.py"))
evidence = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evidence)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.task = "plan/part/01-work.md"
        p = self.root / self.task
        p.parent.mkdir(parents=True)
        p.write_text("---\nstatus: doing\nblocked_by: []\n---\n# Task\n\n## Delivers\nOutput\n\n## Check by\nCheck a known value\n\n## Done when\n- [ ] Value matches\n\n## Delivered\n\n## Review\n")
        (p.parent / "brief.md").write_text("# Outcome\nA useful result\n")
        (self.root / "output one.txt").write_text("one\n")
        (self.root / "output-two.txt").write_text("two\n")

    def identity(self, files=None, absent=None):
        return evidence.receipt(self.root, self.task, files or ["output one.txt"], absent or [], [])

    def test_path_order_and_spelling_are_stable(self):
        a = self.identity(["output one.txt", "output-two.txt"])
        b = self.identity(["./output-two.txt", "./output one.txt"])
        self.assertEqual(a, b)

    def test_content_change_changes_only_output_identity(self):
        before = self.identity()
        (self.root / "output one.txt").write_text("wrong answer\n")
        after = self.identity()
        self.assertNotEqual(before["version"], after["version"])
        self.assertEqual(before["scope"], after["scope"])

    def test_scope_changes_without_output_change(self):
        before = self.identity()
        p = self.root / self.task
        p.write_text(p.read_text().replace("Value matches", "Value matches and currency is stated"))
        self.assertNotEqual(before["scope"], self.identity()["scope"])
        self.assertEqual(before["version"], self.identity()["version"])
        (p.parent / "brief.md").write_text("Different outcome\n")
        self.assertNotEqual(before["scope"], self.identity()["scope"])

    def test_workflow_ticks_and_receipts_do_not_change_scope(self):
        before = self.identity()
        p = self.root / self.task
        p.write_text(p.read_text().replace("status: doing", "status: review").replace("[ ]", "[x]") + "Checked: observed result\n")
        self.assertEqual(before, self.identity())

    def test_missing_file_fails_and_explicit_removal_is_identified(self):
        (self.root / "output one.txt").unlink()
        with self.assertRaises(ValueError):
            self.identity()
        a = self.identity(["output-two.txt"], ["output one.txt"])
        self.assertNotEqual(a["version"], self.identity(["output-two.txt"])["version"])
        with self.assertRaises(ValueError):
            self.identity(["output-two.txt"], ["output-two.txt"])

    def test_retained_copy_survives_later_edits_and_cannot_be_overwritten(self):
        before = self.identity()
        evidence.retain(self.root, before, "notes/evidence/first")
        (self.root / "output one.txt").write_text("later result\n")
        snapshot = self.root / "notes/evidence/first"
        self.assertEqual((snapshot / "output/output one.txt").read_text(), "one\n")
        self.assertEqual(json.loads((snapshot / "receipt.json").read_text())["scope"], before["scope"])
        with self.assertRaises(ValueError):
            evidence.retain(self.root, before, "notes/evidence/first")

    def test_outside_project_is_rejected(self):
        with self.assertRaises(ValueError):
            self.identity(["../outside"])
        outside = self.root.parent / (self.root.name + "-outside")
        outside.write_text("private")
        self.addCleanup(outside.unlink)
        (self.root / "link").symlink_to(outside)
        with self.assertRaises(ValueError):
            self.identity(["link"])

    def test_missing_criteria_cannot_get_a_scope_identity(self):
        (self.root / self.task).write_text("# Unspecified work\n")
        with self.assertRaises(ValueError):
            self.identity()

    def test_example_headings_are_content_and_duplicate_real_sections_fail(self):
        p = self.root / self.task
        p.write_text(p.read_text().replace("Output\n", "Output\n```md\n## Review\nExample output\n```\n"))
        before = self.identity()
        p.write_text(p.read_text().replace("Example output", "Different example"))
        self.assertNotEqual(before["scope"], self.identity()["scope"])
        p.write_text(p.read_text() + "\n## Delivers\nAmbiguous replacement\n")
        with self.assertRaises(ValueError):
            self.identity()


if __name__ == "__main__":
    unittest.main()
