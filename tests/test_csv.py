
import csv
import tempfile
import unittest
from pathlib import Path


def is_valid_csv(file_path):
    path = Path(file_path)

    if not path.is_file() or path.stat().st_size == 0:
        return False

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            return bool(header) and any(cell.strip() for cell in header)
    except (OSError, UnicodeError, csv.Error):
        return False


class TestCSVValidation(unittest.TestCase):
    def test_valid_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.csv"
            path.write_text("ID,Name\n1,Sample\n", encoding="utf-8")
            self.assertTrue(is_valid_csv(path))

    def test_empty_csv(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "empty.csv"
            path.write_text("", encoding="utf-8")
            self.assertFalse(is_valid_csv(path))


if __name__ == "__main__":
    unittest.main()
