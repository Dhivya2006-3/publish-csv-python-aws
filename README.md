# Publish CSV File Using Python and Deploy in AWS

A Python-based web application for generating, validating, viewing, and downloading CSV files through an interactive web dashboard, with AWS S3 integration support.

## Project Overview

**Publish CSV File Using Python and Deploy in AWS** demonstrates Python-based CSV processing, Flask web development, frontend-backend communication, automated testing, and cloud storage integration.

The project provides a dashboard for working with CSV data and includes modular utilities for CSV validation and AWS S3 file uploads.

### Objectives

- Generate CSV files dynamically using Python.
- Provide a browser-based dashboard using Flask.
- Display and download generated CSV data.
- Validate CSV files using reusable Python functions.
- Organize code into modular services and utilities.
- Add automated tests for CSV validation.
- Support uploading files to Amazon S3 when AWS is configured.
- Document setup, testing, and deployment procedures.

## Features

### CSV Processing
- Generate CSV files using Python.
- Read and process CSV records.
- Validate CSV files and their headers.
- Handle empty or missing files.

### Interactive Dashboard
- Display CSV records in a browser-based interface.
- Present record and column statistics.
- Visualize numeric data where supported.
- Refresh displayed data after operations.

### File Download
- Download generated CSV files through the application when the download endpoint is configured.
- Open exported CSV files using spreadsheet applications.

### CSV Validation
- Check whether a file exists and is not empty.
- Check whether the CSV contains a usable header.
- Handle common file-reading and CSV-parsing errors.

### AWS S3 Integration
- Check whether the `AWS_S3_BUCKET` environment variable is configured.
- Upload files to an S3 bucket using `boto3`.
- Return a result message for upload success or failure.
- Use AWS credentials supplied through an appropriate credentials provider.

**Note:** Actual AWS upload requires valid AWS credentials, bucket permissions, and configuration. The presence of the upload function does not mean that cloud deployment or a successful upload has already been verified.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and CSV processing |
| Flask | Web application framework |
| HTML5 | Dashboard structure |
| CSS3 | Dashboard styling |
| JavaScript | Frontend interactions and API requests |
| CSV module | CSV reading and writing |
| `boto3` | AWS SDK for Python |
| `unittest` | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| Amazon S3 | Optional cloud file storage |

## Project Structure

```text
publish-csv-python-aws/
├── app.py
├── main.py
├── data.csv
├── requirements.txt
├── README.md
├── utils/
│   └── csv_validator.py
├── services/
│   └── s3_service.py
├── tests/
│   └── test_csv.py
├── reports/
│   └── testing_report.md
└── templates/
    └── index.html
```

### File Descriptions

- `app.py` — Flask application and HTTP endpoints, if included in the repository.
- `main.py` — Standalone Python CSV generation script.
- `data.csv` — Example or generated CSV data.
- `requirements.txt` — Python dependencies.
- `utils/csv_validator.py` — Reusable CSV validation functions.
- `services/s3_service.py` — AWS S3 configuration checks and upload helper.
- `tests/test_csv.py` — Automated CSV validation tests.
- `reports/testing_report.md` — Test plan and test execution results.
- `templates/index.html` — Web dashboard interface.
- `README.md` — Project documentation.

Keep this tree aligned with the files actually present in the repository. Remove entries from the documentation if the corresponding files do not exist.

## Prerequisites

Install the following tools before running the project:

- Python 3
- Visual Studio Code or another Python editor
- Git, if using version control
- A modern web browser
- An AWS account and appropriate permissions, if testing S3 integration

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Dhivya2006-3/publish-csv-python-aws.git
cd publish-csv-python-aws
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create a Virtual Environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can run Python using `.venv\Scripts\python.exe` directly.

### 3. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

The dependency file should contain the packages needed by the features being used, including Flask and `boto3` if the Flask application and S3 integration are included.

## Running the Project

### Run the Flask Dashboard

If the repository contains a working `app.py`, run:

```powershell
python app.py
```

Open the local address printed in the terminal, commonly:

`http://127.0.0.1:5000`

The exact routes and available dashboard features depend on the implementation in `app.py`.

### Run the Standalone CSV Generator

If using `main.py`:

```powershell
python main.py
```

Check the terminal output and the generated CSV file.

**Important:** The standalone script and Flask dashboard may perform different operations. Running `main.py` does not automatically start the Flask website.

## CSV Validation

The reusable validation function is located in:

`utils/csv_validator.py`

The function `is_valid_csv(file_path)` checks whether a file exists, is non-empty, and contains a usable CSV header.

Example:

```python
from utils.csv_validator import is_valid_csv

file_path = "data.csv"

if is_valid_csv(file_path):
    print("CSV file is valid.")
else:
    print("CSV file is invalid.")
```

This is a basic structural check. It does not guarantee that every row has the correct number of columns or that all values meet a particular business rule.

## AWS S3 Integration

The S3 helper is located in:

`services/s3_service.py`

### Configure the Bucket

Set the bucket name using an environment variable.

PowerShell example:

```powershell
$env:AWS_S3_BUCKET = "your-s3-bucket-name"
```

Replace the example value with your own bucket name.

### Configure AWS Credentials

Configure credentials through an approved AWS method, such as an AWS CLI profile or an IAM role attached to the hosting environment.

Do not commit AWS access keys, secret keys, passwords, or other credentials to GitHub.

### Upload a File

The `upload_file_to_s3(file_path, object_name=None)` helper can upload a file when the bucket, credentials, network access, and permissions are correctly configured.

For example, after configuring the environment and installing `boto3`, the helper can be called from Python:

```python
from services.s3_service import upload_file_to_s3

result = upload_file_to_s3("data.csv")
print(result)
```

Run this example only after configuring your AWS environment. An actual upload has not been confirmed merely by adding this code to the repository.

## Automated Testing

Tests for CSV validation are located in:

`tests/test_csv.py`

The test suite covers examples such as:

- Valid CSV files.
- Empty CSV files.
- Missing files.

### Run Tests

From the project root, run:

```powershell
python -m unittest discover -s tests -v
```

Review the output to confirm whether each test passes or fails.

If a test fails, fix the issue before reporting the test as successful. Update `reports/testing_report.md` with the actual test results after execution.

## Application Workflow

1. The user interacts with the dashboard or runs a Python script.
2. Python processes CSV data.
3. CSV validation utilities check basic file structure when called.
4. The application returns data or a result message.
5. The user can download CSV data if the relevant endpoint is implemented.
6. Files can be uploaded to Amazon S3 when the S3 helper is invoked with valid AWS configuration.

The exact workflow depends on which functions and endpoints are connected in the application.

## Security Considerations

- Never upload AWS credentials or `.env` files containing secrets to GitHub.
- Use IAM permissions limited to the required S3 operations.
- Validate uploaded files before processing them.
- Limit upload size and handle invalid file content safely.
- Avoid exposing detailed internal exceptions to public users.
- Use a production-ready WSGI server when deploying Flask.
- Configure HTTPS and appropriate access controls for public deployments.

## Troubleshooting

### Flask Module Not Found

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

### CSV File Not Found

Check that the file path is correct and that the command is run from the expected project directory.

### Tests Cannot Import a Module

Run tests from the project root:

```powershell
python -m unittest discover -s tests
