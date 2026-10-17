# Python CSV Dashboard with AWS S3

A Python-based CSV management project featuring a Flask web dashboard, advanced CSV validation, automated unit testing, and optional AWS S3 integration.

## Project Overview

This project helps users work with CSV files through a Python application. It includes CSV structure validation, a Flask dashboard, and an AWS S3 service module for cloud storage integration.

## Features

- **Flask Dashboard:** Web interface for the CSV application.
- **Advanced CSV Validation:** Checks file existence, file size, headers, duplicate column names, missing values, and inconsistent row lengths.
- **Automated Testing:** Unit tests using Python's `unittest` framework.
- **AWS S3 Service:** Optional utility for uploading files to an S3 bucket.
- **Continuous Integration:** GitHub Actions runs automated tests on pushes and pull requests.

## Technology Stack

- Python
- Flask
- CSV module
- Boto3 (AWS SDK for Python)
- unittest
- GitHub Actions
- AWS S3

## Project Structure

```text
Python-CSV-AWS-Project/
├── app.py
├── main.py
├── data.csv
├── requirements.txt
├── templates/
├── utils/
│   └── csv_validator.py
├── services/
│   └── s3_service.py
├── tests/
│   └── test_csv.py
├── reports/
│   └── testing_report.md
└── .github/
    └── workflows/
        └── tests.yml
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dhivya2006-3/publish-csv-python-aws.git
   cd publish-csv-python-aws
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Run the Application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

The CSV validation test suite currently contains seven test cases.

## AWS S3 Configuration

To use the S3 upload utility:

1. Configure AWS credentials securely using an approved AWS credentials profile or environment variables.
2. Set the `AWS_S3_BUCKET` environment variable to your bucket name.
3. Ensure the AWS identity has permission to upload objects to that bucket.

Do not commit AWS access keys, secret keys, or other credentials to GitHub.

**Note:** The S3 service utility is implemented separately. Integration with the dashboard and actual cloud upload should be verified before claiming that the complete upload workflow is operational.

## Testing Report

See [`reports/testing_report.md`](reports/testing_report.md) for validation coverage and test results.

## Continuous Integration

GitHub Actions runs the automated CSV tests on pushes and pull requests. Workflow configuration: [`.github/workflows/tests.yml`](.github/workflows/tests.yml).

## Future Enhancements

- Connect CSV validation to the Flask upload workflow.
- Add dashboard-level tests.
- Add CSV summary statistics and downloadable validation reports.
- Improve error messages and validation result presentation.
- Add deployment configuration and screenshots.

## Project Status

CSV validation and automated tests are implemented. AWS S3 dashboard integration and deployment require further verification.
