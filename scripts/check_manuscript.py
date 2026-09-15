#!/usr/bin/env python3
"""Small, offline regression checks for the revised manuscript (stdlib only).

This deliberately checks explicit QMD links and the current simple configuration,
not arbitrary YAML, every generated asset, or external resources.
"""

import re
import csv
import hashlib
import unittest
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def configured_files():
    config = (ROOT / "_quarto.yml").read_text(encoding="utf-8")
    return re.findall(r"^\s*-\s+([^\s]+\.qmd)\s*$", config, re.MULTILINE)


class ManuscriptChecks(unittest.TestCase):
    def test_lab_checksums(self):
        lab = ROOT / 'resources/lab-v1'
        entries = (lab / 'SHA256SUMS').read_text().splitlines()
        self.assertEqual(len(entries), 3)
        for entry in entries:
            digest, filename = entry.split()
            self.assertEqual(hashlib.sha256((lab / filename).read_bytes()).hexdigest(), digest)

    def test_configured_files_exist_and_are_unique(self):
        files = configured_files()
        self.assertEqual(len(files), 22)
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

    def test_customer_fixture_and_printed_inputs(self):
        lab = ROOT / 'resources/lab-v1'
        with (lab / 'customers.csv').open() as handle:
            rows = list(csv.DictReader(handle))
        appendix = (ROOT / 'appendices/g-reproducible-lab.qmd').read_text()
        self.assertEqual(len(rows), 12)
        self.assertEqual(len({r['id'] for r in rows}), 12)
        for r in rows:
            printed = '| ' + ' | '.join([r['id'], r['region'], r['tenure_months'],
                r['satisfaction'], r['renewal_label'], r['split'].title()]) + ' |'
            self.assertIn(printed, appendix)
        groups = {}
        for region in ['South', 'Metro', 'North']:
            group = [r for r in rows if r['region'] == region]
            groups[region] = (sum(r['renewal_label'] == 'Low' for r in group), len(group))
        self.assertEqual(groups, {'South': (4, 5), 'Metro': (2, 4), 'North': (0, 3)})
        test = [r for r in rows if r['split'] == 'test']
        self.assertEqual([r['id'] for r in test], ['T01', 'T02', 'T03', 'T04'])
        actual = [r['renewal_label'] for r in test]
        predictions = [
            ['Low' if int(r['satisfaction']) <= 6 else 'High' for r in test],
            ['Low' if int(r['tenure_months']) <= 6 else 'High' for r in test],
            ['High'] * 4,
        ]
        results = [(sum(a == p for a, p in zip(actual, pred)),
                    sum(a == p == 'Low' for a, p in zip(actual, pred)))
                   for pred in predictions]
        self.assertEqual(results, [(2, 1), (3, 1), (2, 0)])
        self.assertFalse(any(correct >= 3 and detected == 2 for correct, detected in results))
        self.assertIn('neither meets the brief', appendix)

    def test_support_fixture_and_toy_scorer(self):
        with (ROOT / 'resources/lab-v1/support.csv').open() as handle:
            rows = list(csv.DictReader(handle))
        appendix = (ROOT / 'appendices/g-reproducible-lab.qmd').read_text()
        positive = {'wonderful', 'thank', 'clear', 'polite'}
        negative = {'outage', 'fail', 'errors', 'down'}
        results = []
        self.assertEqual(len(rows), 6)
        for r in rows:
            self.assertIn('| ' + ' | '.join([r['id'], r['text'],
                r['reference_theme'].title(), r['reference_tone'].title()]) + ' |', appendix)
            words = re.findall(r'\b\w+\b', r['text'].lower())
            score = sum(w in positive for w in words) - sum(w in negative for w in words)
            results.append('positive' if score > 0 else 'negative' if score < 0 else 'neutral')
        self.assertEqual(results, ['neutral', 'positive', 'neutral', 'neutral', 'negative', 'neutral'])
        self.assertEqual(sum(p == r['reference_tone'] for p, r in zip(results, rows)), 2)
        self.assertIn('2/6', appendix)

    def test_printed_retrieval_sources_match_download(self):
        sources = (ROOT / 'resources/lab-v1/sources.txt').read_text()
        appendix = (ROOT / 'appendices/g-reproducible-lab.qmd').read_text()
        excerpts = re.findall(r'— [^:]+:\*\* “([^”]+)”', appendix)
        self.assertEqual(len(excerpts), 3)
        for excerpt in excerpts:
            self.assertIn(excerpt, sources)
        for filename in ['customers.csv', 'support.csv', 'sources.txt']:
            self.assertIn('../resources/lab-v1/' + filename, appendix)
        self.assertIn('resources/lab-v1/**', (ROOT / '_quarto.yml').read_text())

    def test_practice_variation(self):
        chapters = [(ROOT / name).read_text() for name in configured_files()
                    if name.startswith('chapters/')]
        self.assertLessEqual(sum('> **Role:**' in chapter for chapter in chapters), 3)
        self.assertTrue(all('**Time:**' in chapter for chapter in chapters))
        self.assertNotIn('**Expose.**', '\n'.join(chapters))

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
