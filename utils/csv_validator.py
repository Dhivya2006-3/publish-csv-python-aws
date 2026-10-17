
"""Advanced CSV validation utilities."""

import csv
from pathlib import Path

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def validate_csv(file_path):
    """Validate CSV file structure and return validation details."""
    path = Path(file_path)

    if not path.is_file():
        return {"valid": False, "errors": ["File not found."]}

    if path.stat().st_size == 0:
        return {"valid": False, "errors": ["File is empty."]}

    if path.stat().st_size > MAX_FILE_SIZE:
        return {"valid": False, "errors": ["File exceeds the 10 MB limit."]}

    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            reader = csv.reader(file, strict=True)
            headers = next(reader, None)

            if not headers or not any(h.strip() for h in headers):
                return {"valid": False, "errors": ["CSV header is missing."]}

            cleaned = [h.strip() for h in headers]

            if any(not h for h in cleaned):
                return {"valid": False, "errors": ["Empty column name found."]}

            if len(set(cleaned)) != len(cleaned):
                return {"valid": False, "errors": ["Duplicate column names found."]}

            row_count = 0

            for line_number, row in enumerate(reader, start=2):
                if len(row) != len(headers):
                    return {
                        "valid": False,
                        "errors": [
                            f"Row {line_number} has {len(row)} values; "
                            f"expected {len(headers)}."
                        ],
                    }

                if any(not value.strip() for value in row):
                    return {
                        "valid": False,
                        "errors": [f"Missing value found in row {line_number}."],
                    }

                row_count += 1

            return {
                "valid": True,
                "errors": [],
                "columns": len(headers),
                "rows": row_count,
            }

    except (OSError, UnicodeError, csv.Error) as error:
        return {"valid": False, "errors": [f"Unable to read CSV: {error}"]}


def is_valid_csv(file_path):
    """Compatibility helper returning a boolean result."""
    return validate_csv(file_path)["valid"]
