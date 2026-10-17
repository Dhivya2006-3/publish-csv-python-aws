# CSV Validation Testing Report

## Project
Publish CSV File Using Python and Deploy in AWS

## Objective
To validate CSV file structure, column headers, row consistency, missing values, and file size.

## Validation Features

- File existence check
- Empty file detection
- Maximum file size limit of 10 MB
- Empty header detection
- Duplicate column name detection
- Missing value detection
- Inconsistent column count detection
- CSV parsing error handling

## Automated Test Cases

| Test Case | Expected Result | Status |
|---|---|---|
| Valid CSV | Accepted | Pending execution |
| Empty file | Rejected | Pending execution |
| Missing file | Rejected | Pending execution |
| Duplicate headers | Rejected | Pending execution |
| Empty header | Rejected | Pending execution |
| Missing value | Rejected | Pending execution |
| Inconsistent columns | Rejected | Pending execution |

## Test Framework
Python `unittest`

## Execution Command

```bash
python -m unittest discover -s tests -v
```

## Conclusion
Advanced CSV validation and automated test cases have been added to the project. Final test results must be recorded after running the tests locally.
