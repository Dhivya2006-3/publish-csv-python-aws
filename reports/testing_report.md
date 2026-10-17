
import csv
import tempfile
import unittest
from pathlib import Path


def validate_csv(file_path):
    path = Path(file_path)

    if not path.exists() or path.stat().st_size == 0:
        return False

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            return bool(header) and any(header)
    except (OSError, UnicodeError, csv.Error):
        return False


class TestCSVValidation(unittest.TestCase):
    def test_valid_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.csv"
            path.write_text("ID,Name\n1,Sample\n", encoding="utf-8")
            self.assertTrue(validate_csv(path))

    def test_empty_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "empty.csv"
            path.write_text("", encoding="utf-8")
            self.assertFalse(validate_csv(path))


if __name__ == "__main__":
    unittest.main()
