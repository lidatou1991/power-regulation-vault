import tempfile
import unittest
from pathlib import Path

from scripts.validate_notes import validate, validate_intake


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

    def test_optional_publishing_fields_are_backward_compatible_and_controlled(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            notes = root / "04_Topics"
            notes.mkdir()
            base = "---\ntitle: Test\ncountry: CL\nstatus: current\nsource_type: law\nlast_verified: 2026-08-14\nconfidence: high\n"
            (notes / "legacy.md").write_text(base + "---\n", encoding="utf-8")
            self.assertEqual(validate(root), [])
            (notes / "quoted.md").write_text(
                base + 'publishable: "no"\n---\n', encoding="utf-8"
            )
            self.assertEqual(validate(root), [])
            (notes / "invalid.md").write_text(
                base + "publication_status: public\n---\n", encoding="utf-8"
            )
            self.assertTrue(any("invalid publication_status" in warning for warning in validate(root)))

    def test_intake_validation_is_separate_and_checks_controlled_values(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "00_Inbox" / "manual"
            inbox.mkdir(parents=True)
            (inbox / "record.md").write_text(
                "---\nsource_id: TEST-SOURCE\ntitle: Test\nreview_status: pending\n---\n",
                encoding="utf-8",
            )
            self.assertEqual(validate(root), [])
            warnings = validate_intake(root)
            self.assertTrue(any("missing country" in warning for warning in warnings))
            self.assertTrue(any("invalid review_status" in warning for warning in warnings))

    def test_intake_validation_ignores_non_intake_markdown(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            inbox = root / "00_Inbox"
            inbox.mkdir()
            (inbox / "readme.md").write_text("# Notes\n", encoding="utf-8")
            self.assertEqual(validate_intake(root), [])


if __name__ == "__main__":
    unittest.main()
