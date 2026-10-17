import tempfile
import unittest
from pathlib import Path

from utils.csv_validator import is_valid_csv


class TestCSVValidation(unittest.TestCase):

    def test_valid_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.csv"
            path.write_text(
                "ID,Name\n1,Sample\n",
                encoding="utf-8"
            )
            self.assertTrue(is_valid_csv(path))

    def test_empty_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "empty.csv"
            path.write_text("", encoding="utf-8")
            self.assertFalse(is_valid_csv(path))

    def test_missing_file(self):
        path = Path("missing_file.csv")
        self.assertFalse(is_valid_csv(path))


if __name__ == "__main__":
    unittest.main()
