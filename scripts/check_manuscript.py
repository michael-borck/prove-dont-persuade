#!/usr/bin/env python3
"""Small, offline regression checks for the revised manuscript (stdlib only).

This deliberately checks explicit QMD links and the current simple configuration,
not arbitrary YAML, every generated asset, or external resources.
"""

import re
import unittest
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def configured_files():
    config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    return re.findall(r"^\s*-\s+([^\s]+\.qmd)\s*$", config, re.MULTILINE)


class ManuscriptChecks(unittest.TestCase):
    def test_configured_files_exist_and_are_unique(self):
        files = configured_files()
        self.assertEqual(len(files), 21)
        self.assertEqual(len(files), len(set(files)))
        for name in files:
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file())

    def test_dependency_order_preserves_stable_filenames(self):
        chapters = [Path(p).name[:2] for p in configured_files()
                    if p.startswith("chapters/")]
        self.assertEqual(chapters,
                         ["01", "02", "03", "04", "06", "05",
                          "07", "08", "09", "11", "10", "12"])

    def test_explicit_local_chapter_links(self):
        checked = 0
        for name in configured_files():
            source = ROOT / name
            text = source.read_text(encoding="utf-8")
            for href in re.findall(r"\]\(([^)]+)\)", text):
                link = urlsplit(href)
                if link.scheme or not link.path.endswith(".qmd"):
                    continue
                target = (source.parent / unquote(link.path)).resolve()
                with self.subTest(source=name, target=href):
                    self.assertTrue(target.is_file())
                    if link.fragment:
                        self.assertIn("#" + link.fragment,
                                      target.read_text(encoding="utf-8"))
                checked += 1
        self.assertGreater(checked, 0)

    def test_worked_evaluation_arithmetic(self):
        text = (ROOT / "chapters/09-does-it-actually-work.qmd").read_text(
            encoding="utf-8")
        rows = re.findall(
            r"^\| (Healthy|Degraded|Fault) \| (Normal|Dim) \| (\d+) \| (\d+) \|$",
            text, re.MULTILINE)
        self.assertEqual(len(rows), 6)
        self.assertEqual(len({(label, lighting) for label, lighting, _, _ in rows}), 6)
        groups = defaultdict(lambda: [0, 0])
        for label, lighting, count, correct in rows:
            count, correct = int(count), int(correct)
            self.assertTrue(0 <= correct <= count)
            for group in ["overall", label, lighting]:
                groups[group][0] += correct
                groups[group][1] += count
        self.assertEqual(groups["overall"], [41, 60])
        self.assertEqual(groups["Healthy"], [19, 20])
        self.assertEqual(groups["Degraded"], [16, 20])
        self.assertEqual(groups["Fault"], [6, 20])
        self.assertEqual(groups["Dim"], [16, 30])
        for group in ["overall", "Dim"]:
            correct, count = groups[group]
            self.assertIn(f"{correct}/{count}", text)
            self.assertIn(f"{100 * correct / count:.1f}%", text)
        self.assertIn("invented for this exercise", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
