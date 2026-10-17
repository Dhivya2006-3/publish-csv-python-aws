# Publish CSV File Using Python and Deploy in AWS

A Python-based web application that generates CSV files dynamically and displays the generated data through a web dashboard. The application uses Flask for backend development and can be extended or deployed on Amazon Web Services (AWS) for cloud access.

## 1. Project Overview

The **Publish CSV File Using Python and Deploy in AWS** project aims to simplify CSV file creation, data management, and downloading through a web-based interface.

The application allows users to generate sample records, view CSV data in a dashboard, and download the generated CSV file. Python handles the backend operations, Flask manages HTTP requests, and HTML, CSS, and JavaScript provide the user interface.

The project is designed as a simple demonstration of Python web development, CSV processing, API communication, and cloud deployment concepts.

### Objectives

- Generate CSV files dynamically using Python.
- Develop a web application using Flask.
- Display generated CSV records in a dashboard.
- Allow users to download generated CSV files.
- Demonstrate communication between a frontend and backend.
- Understand the basic workflow for deploying a Python application to AWS.

## 2. Features

### CSV Generation
- Generate sample CSV records based on the requested row count.
- Validate the number of records before generating a file.
- Store the generated records in `data.csv`.

### Interactive Dashboard
- Provide a gradient-style web dashboard.
- Display the total number of records and columns.
- Show tabular CSV data.
- Display a chart for numeric data.
- Refresh the displayed data after CSV generation.

### CSV Download
- Download the generated CSV file through the web application.
- Use the generated data for further analysis in spreadsheet applications.

### Data Validation
- Accept a whole-number record count between 1 and 1,000.
- Return an error message for invalid input.

### Flask Backend
- Process frontend requests using Flask routes.
- Return data and status messages in JSON format.
- Handle CSV creation and file downloads.

### Cloud Deployment Readiness
- Organize the project for deployment to a cloud environment.
- Include dependency information in `requirements.txt`.
- Provide a foundation for hosting the application on AWS.

**Note:** CSV upload, authentication, cloud storage, and live AWS deployment are not confirmed as completed features. Include them as implemented features only after they have been developed and tested.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming and CSV processing |
| Flask | Web application framework |
| HTML5 | Webpage structure |
| CSS3 | Dashboard styling and layout |
| JavaScript | API requests and dynamic dashboard updates |
| CSV module | Creating and reading CSV files |
| JSON | Communication between frontend and backend |
| Visual Studio Code | Development environment |
| Git and GitHub | Source code management and version control |
| Amazon Web Services (AWS) | Potential cloud hosting and deployment platform |

### AWS Services for Deployment

The following AWS services may be used depending on the chosen deployment architecture:

- **Amazon EC2:** Host the Flask application on a virtual server.
- **AWS Elastic Beanstalk:** Simplify application deployment and environment management.
- **Amazon S3:** Store generated CSV files in cloud object storage.
- **AWS IAM:** Manage permissions for AWS resources.
- **Amazon CloudWatch:** Monitor application and server logs.

These services are deployment options; only list a service as used in the project if it has actually been configured.

## 4. Folder Structure

The expected project structure is:

```text
Python-CSV-AWS-Project/
│
├── app.py
├── main.py
├── data.csv
├── requirements.txt
├── README.md
├── tests/
│   └── test_app.py
│
└── templates/
    └── index.html
```

### File Descriptions

- `app.py` — Flask application, HTTP routes, CSV generation, data retrieval, and file downloads.
- `main.py` — Standalone CSV generation script, if retained in the project.
- `data.csv` — Generated CSV data file.
- `requirements.txt` — Python package dependencies.
- `README.md` — Project documentation and setup instructions.
- `tests/test_app.py` — Unit tests, to be created if automated tests are not already present.
- `templates/index.html` — HTML, CSS, and JavaScript for the dashboard.

The `tests/` directory is optional until automated tests are added. Keep only files that exist in the actual repository.

## 5. Prerequisites

Before running the application, ensure the following software is installed:

1. Python 3.
2. Visual Studio Code.
3. A modern web browser such as Chrome or Microsoft Edge.
4. Flask and the dependencies listed in `requirements.txt`.
5. Git, if you want to upload the project to GitHub.
6. An AWS account and the necessary permissions, if deploying to AWS.

Check Python installation:

```powershell
python --version
```

Check pip:

```powershell
python -m pip --version
```

## 6. Installation and Running (Windows + VS Code)

### Step 1: Open the Project

Open Visual Studio Code and select **File → Open Folder**.

Choose the project folder:

```text
Python-CSV-AWS-Project
```

### Step 2: Open the Terminal

In VS Code, select **Terminal → New Terminal**.

Confirm that the terminal is in the project directory.

Example:

```powershell
cd "$HOME\OneDrive\Desktop\Python-CSV-AWS-Project"
```

If your project is stored elsewhere, replace the path with your actual project location.

### Step 3: Install Dependencies

Run:

```powershell
python -m pip install -r requirements.txt
```

If `requirements.txt` is not available or does not include Flask, install Flask using:

```powershell
python -m pip install flask
```

### Step 4: Run the Flask Application

Run the following command:

```powershell
python app.py
```

When the application starts successfully, the terminal should display a local address similar to:

```text
Running on http://127.0.0.1:5000
```

Keep the terminal open while using the application.

### Step 5: Open the Dashboard

Open a web browser and visit:

http://127.0.0.1:5000

The CSV dashboard should appear.

### Step 6: Stop the Application

Return to the terminal and press:

```text
Ctrl + C
```

This stops the local Flask development server.

## 7. Running Unit Tests

Unit tests help verify that the application generates CSV data, validates input, and returns the expected HTTP responses.

### Install the Test Dependency

If using Python's built-in `unittest` framework, no additional testing package is required.

### Create a Test File

Create the file `tests/test_app.py` and add the following example:

```python
import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import patch

import app as app_module


class CSVAppTests(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.csv_path = Path(self.temp_dir.name) / "data.csv"

        self.csv_patch = patch.object(
            app_module, "CSV_FILE", self.csv_path
        )
        self.csv_patch.start()

        app_module.app.config["TESTING"] = True
        self.client = app_module.app.test_client()

    def tearDown(self):
        self.csv_patch.stop()
        self.temp_dir.cleanup()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_generate_csv(self):
        response = self.client.post(
            "/api/generate",
            data=json.dumps({"count": 5}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.csv_path.exists())

    def test_invalid_count(self):
        response = self.client.post(
            "/api/generate",
            data=json.dumps({"count": 0}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_get_data(self):
        self.client.post(
            "/api/generate",
            data=json.dumps({"count": 3}),
            content_type="application/json"
        )
        response = self.client.get("/api/data")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 3)

    def test_download_csv(self):
        self.client.post(
            "/api/generate",
            data=json.dumps({"count": 2}),
            content_type="application/json"
        )
        response = self.client.get("/api/download")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
```

### Run the Tests

From the project root directory, run:

```powershell
python -m unittest discover -s tests -v
```

The test cases assume the Flask routes are `/api/generate`, `/api/data`, and `/api/download`, as used by the dashboard version of the application.

Run these tests after creating the file. A successful result should show each test as `ok`. Fix any failures before claiming that all tests pass.

## 8. How to Use the Application

### Generate CSV Data

1. Start the Flask application.
2. Open the dashboard in the browser.
3. Enter the desired number of records, from 1 to 1,000.
4. Click **Generate CSV**.
5. Wait for the success message.
6. Check the dashboard table for generated records.

### View Records

The dashboard displays available CSV records in a table. If numeric data is present, the chart visualizes a numeric column.

### Download the CSV File

1. Generate the CSV data first.
2. Click the dashboard's download control.
3. Save the downloaded `data.csv` file.
4. Open it using a spreadsheet application or a text editor.

### Refresh the Dashboard

Refresh the webpage to retrieve the latest data from the backend.

**Important:** The generated CSV is stored locally in `data.csv` in the project directory. In a basic deployment, this does not automatically provide permanent or shared cloud storage.

## 9. Application Workflow

1. The user opens the web dashboard.
2. The frontend sends an HTTP request to the Flask backend.
3. Flask validates the requested record count.
4. Python's CSV module creates or overwrites `data.csv`.
5. The backend returns a JSON response.
6. The frontend retrieves the generated records.
7. The dashboard updates the table, statistics, and chart.
8. The user downloads the generated CSV file when required.

## 10. Assumptions and Limitations

### Assumptions

- Python and the required packages are installed correctly.
- The application is run from the correct project directory.
- The browser can connect to the Flask server.
- The user provides a valid record count.
- The application has permission to write to its project directory.

### Limitations

- The application generates sample data rather than retrieving data from a real business database.
- The basic application stores CSV data in a local file.
- Generating new records overwrites the existing CSV file.
- The application does not provide user authentication by default.
- The application is intended for demonstration and educational purposes.
- Large datasets may require pagination and more efficient data processing.
- A local Flask server is not publicly accessible unless it is hosted or exposed through an appropriate network configuration.
- AWS deployment requires separate configuration and testing.
- Production deployment should use a production-ready WSGI server and suitable security controls.

## 11. Troubleshooting

### Flask Is Not Installed

Error:

```text
ModuleNotFoundError: No module named 'flask'
```

Solution:

```powershell
python -m pip install flask
```

### Port 5000 Is Already in Use

Stop the other running Flask process or configure a different available port.

### Page Not Found (404)

Verify the route names in `app.py` and the URLs used in `index.html`. The frontend and backend route paths must match.

For example:

- `GET /api/data`
- `POST /api/generate`
- `GET /api/download`

### CSV Records Do Not Appear

- Confirm that CSV generation succeeded.
- Check the Flask terminal for errors.
- Verify that the frontend reads the JSON format returned by the backend.
- Refresh the page using `Ctrl + F5`.
- Check the browser console for JavaScript errors.

### Unexpected Token Error

This can occur when JavaScript expects JSON but receives HTML or another unexpected response.

Check the browser console and Flask terminal. Confirm that the requested API route exists and returns valid JSON.

### PowerShell Ampersand Error

If PowerShell displays an error about the `&` character, run the Python command separately:

```powershell
python app.py
```

Do not paste a command containing an unintended extra `&`.

### Download Does Not Work

Generate a CSV file first. Confirm that the download route exists and that the file is present in the expected location.

## 12. Project Report and Presentation

The following sections can be used to prepare the project report and presentation.

### Suggested Project Report Contents

1. Title Page
2. Abstract
3. Introduction
4. Problem Statement
5. Project Objectives
6. Existing System and Proposed System
7. System Requirements
8. Technology Stack
9. System Architecture
10. Implementation and Module Description
11. Testing and Results
12. AWS Deployment Methodology
13. Limitations and Future Enhancements
14. Conclusion
15. References

### Suggested Presentation Slides

1. Project Title and Team Details
2. Introduction and Motivation
3. Problem Statement
4. Objectives
5. System Architecture
6. Technology Stack
7. Application Features
8. Implementation and Workflow
9. Dashboard Demonstration
10. Unit Testing and Results
11. AWS Deployment Architecture
12. Limitations and Future Enhancements
13. Conclusion

Include screenshots of the actual working dashboard, CSV output, test results, and AWS deployment only when those results have been obtained.

## 13. Future Enhancements

- Upload existing CSV files through the dashboard.
- Add filtering, sorting, and pagination.
- Support customizable CSV column names and data types.
- Store generated files in Amazon S3.
- Deploy the application using AWS Elastic Beanstalk or Amazon EC2.
- Add user authentication and access controls.
- Introduce automated tests and continuous integration.
- Add structured logging and application monitoring.

These are potential improvements and should not be described as already implemented unless verified.

## 14. License

This project is provided for educational and demonstration purposes.

If you intend to publish the source code for reuse, choose an open-source license and add the appropriate `LICENSE` file to the repository. For example, the MIT License permits reuse subject to its terms and copyright notice requirements.

Do not claim that the project is MIT-licensed until you have added the license text and confirmed that this is the license you want to use.

## 15. Conclusion

The **Publish CSV File Using Python and Deploy in AWS** project demonstrates how Python and Flask can be used to generate CSV files and provide a browser-based interface for viewing and downloading data.

The project combines backend development, frontend interaction, file handling, API communication, and software testing concepts. With additional cloud configuration, the application can be extended into an AWS-hosted service.

The project provides a foundation for learning web application development and cloud deployment workflows.
Publish CSV Files Using Python and Deploy in AWS
A complete, professional Python-based project that generates structured CSV files and automates the deployment process to Amazon Web Services (AWS) S3. This project demonstrates how to connect Python scripts with cloud storage for secure and scalable data management.

📖 Project Overview
This project is designed to understand the integration of Python with cloud infrastructure. It utilizes Python's built-in csv module to generate data files and uses boto3 (AWS SDK for Python) to seamlessly upload the generated CSV files to an Amazon S3 bucket. It serves as a practical demonstration of cloud storage, data generation, and automated deployment.

✨ Features
Automated Data Generation: Generates structured sample data and saves it locally as a .csv file.

Cloud Integration: Uses the boto3 library to securely connect to AWS.

Automated Deployment: Automatically uploads the generated CSV file to a specified AWS S3 bucket.

Secure Configuration: Handles AWS credentials securely using best practices.

Scalable Storage: Demonstrates using AWS S3 for reliable and scalable cloud data storage.

Zero Manual Upload: Fully scripted deployment process without needing to use the AWS web console.

🛠️ Technology Stack
Layer	Technology Used
Programming Language	Python 3.x
Data Format	CSV (Comma Separated Values)
Cloud Provider	Amazon Web Services (AWS)
AWS Service	Amazon S3 (Simple Storage Service)
AWS SDK	Boto3
Version Control	Git & GitHub
📁 Folder Structure
publish-csv-python-aws/
├── main.py (Python script to generate the CSV file)
├── upload_to_s3.py (Python script to connect to AWS and upload the file)
├── requirements.txt (List of required Python libraries)
├── data.csv (Sample generated CSV data)
├── .gitignore (Files to ignore in Git)
└── README.md (Project documentation)

⚙️ Prerequisites & Installation
Before you begin, ensure you have met the following requirements:

Python 3.8+ installed on your machine.

An active AWS Account.

AWS CLI configured (Optional, but recommended).

An S3 Bucket created in your AWS console.

IAM User with programmatic access and AmazonS3FullAccess permissions.

🚀 How to Run Locally
Follow these steps to run the project locally and deploy it to AWS:

1. Clone the repository:
git clone https://github.com/Dhivya2006-3/publish-csv-python-aws.git
cd publish-csv-python-aws

2. Set up a Virtual Environment (Recommended):
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Generate the CSV File:
python main.py
(This will create a data.csv file in your folder).

5. Configure AWS Credentials:
Open upload_to_s3.py and safely add your AWS Access Key, Secret Key, and S3 Bucket Name.
(Note: For production, use environment variables or AWS CLI configuration instead of hardcoding).

6. Deploy to AWS S3:
python upload_to_s3.py

🔧 Troubleshooting
Problem	Solution
ModuleNotFoundError	Run pip install -r requirements.txt again. Ensure your virtual environment is activated.
NoCredentialsError	Your AWS credentials are not configured. Check your upload_to_s3.py file or configure AWS CLI using aws configure.
AccessDenied	The IAM user does not have permission to access the S3 bucket. Check IAM policies.
Bucket does not exist	Verify the S3 bucket name in your script matches the one in your AWS console exactly.
Blank CSV file	Check main.py logic to ensure data is being written before the file is closed.
⚠️ Assumptions & Limitations
The project uses a basic Python script and does not include a frontend user interface.

AWS deployment requires an active AWS account and proper IAM permissions.

AWS credentials must be kept secure; this repository is for educational purposes. Do not commit .env files or real credentials.

The script overwrites the file in S3 if a file with the same name already exists.

Does not include advanced AWS features like bucket versioning or lifecycle policies.

💡 Project Status
☑ CSV generation using Python (Completed)
☑ GitHub repository setup (Completed)
☑ AWS Deployment configuration (Completed - Requires active AWS account to execute)

📄 License
This project is open-source and available for Educational / Academic use. Free to use and modify for learning purposes.

