"""CSV validation utilities."""

import csv
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
