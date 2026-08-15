import tempfile
import unittest
from pathlib import Path

from scripts.find_broken_links import find_broken


class BrokenLinksTests(unittest.TestCase):
    def test_finds_only_unresolved_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Known.md").write_text("# Known\n", encoding="utf-8")
            (root / "Index.md").write_text("[[Known]] [[Missing]]\n", encoding="utf-8")
            broken = find_broken(root)
            self.assertEqual(len(broken), 1)
            self.assertIn("[[Missing]]", broken[0])


if __name__ == "__main__":
    unittest.main()

