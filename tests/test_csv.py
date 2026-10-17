
import tempfile
import unittest
from pathlib import Path

from utils.csv_validator import validate_csv, is_valid_csv


class TestCSVValidation(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def make_csv(self, name, content):
        path = self.folder / name
        path.write_text(content, encoding="utf-8")
        return path

    def test_valid_csv(self):
        path = self.make_csv("valid.csv", "ID,Name\n1,Sample\n")
        result = validate_csv(path)
        self.assertTrue(result["valid"])
        self.assertEqual(result["rows"], 1)

    def test_empty_csv(self):
        path = self.make_csv("empty.csv", "")
        self.assertFalse(is_valid_csv(path))

    def test_missing_file(self):
        path = self.folder / "missing.csv"
        self.assertFalse(is_valid_csv(path))

    def test_duplicate_headers(self):
        path = self.make_csv("duplicate.csv", "ID,ID\n1,2\n")
        self.assertFalse(validate_csv(path)["valid"])

    def test_empty_header(self):
        path = self.make_csv("header.csv", ",Name\n1,Sample\n")
        self.assertFalse(validate_csv(path)["valid"])

    def test_missing_value(self):
        path = self.make_csv("missing_value.csv", "ID,Name\n1,\n")
        self.assertFalse(validate_csv(path)["valid"])

    def test_inconsistent_columns(self):
        path = self.make_csv("columns.csv", "ID,Name\n1,Sample,Extra\n")
        self.assertFalse(validate_csv(path)["valid"])


if __name__ == "__main__":
    unittest.main()
