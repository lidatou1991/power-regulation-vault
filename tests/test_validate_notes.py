import tempfile
import unittest
from pathlib import Path

from scripts.validate_notes import validate


class ValidateNotesTests(unittest.TestCase):
    def test_warns_for_missing_required_field(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            notes = root / "04_Topics"
            notes.mkdir()
            (notes / "note.md").write_text("---\ntitle: Test\n---\n", encoding="utf-8")
            warnings = validate(root)
            self.assertEqual(len(warnings), 1)
            self.assertIn("country", warnings[0])


if __name__ == "__main__":
    unittest.main()

