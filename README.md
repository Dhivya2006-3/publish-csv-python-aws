# Publish CSV File Using Python
### A Python-Powered CSV Processing, Data Analytics and AWS Cloud Integration Project

---

## 📌 Project Overview

**Publish CSV File Using Python** is a Python-based web application designed to simplify CSV file publishing, validation, data cleaning, and processing through a user-friendly dashboard.

CSV (Comma-Separated Values) files are widely used to store and exchange structured data. However, working with raw CSV files can involve common challenges such as missing values, duplicate records, inconsistent data, and difficulties in managing files efficiently.

This project addresses these challenges by combining Python, Flask, and Pandas to provide essential CSV-processing capabilities through a web interface. It also incorporates AWS S3 integration to support cloud-storage workflows.

The application aims to make CSV data handling more accessible, organized, and efficient while demonstrating practical applications of Python programming, web development, data processing, and cloud integration.

## 🎯 Project Objectives

The primary objective of this project is to develop a simple and effective platform for handling CSV files using Python.

The specific objectives are:

- To provide a convenient interface for uploading and processing CSV files.
- To validate uploaded datasets before performing operations.
- To identify and handle missing values in datasets.
- To detect and remove duplicate records.
- To display CSV data for easier inspection and analysis.
- To enable users to download processed datasets.
- To support integration with AWS S3 for cloud-based file storage.
- To demonstrate the practical use of Python libraries in data-processing applications.

## 💡 Problem Statement

Handling CSV files manually can become time-consuming when datasets contain incomplete records, duplicate entries, or inconsistent information. Users may need to switch between different tools to inspect, clean, and save their data.

Furthermore, managing processed files and integrating them with cloud storage can introduce additional complexity.

The proposed solution brings essential CSV-processing operations together in a single web-based dashboard, reducing manual effort and creating a more organized workflow for working with structured data.

## ✨ Key Features

### 1. CSV File Upload
Allows users to upload CSV files through the web interface for further processing.

### 2. CSV Validation
Uses Python-based validation logic to check uploaded CSV files and help identify unsuitable input files before processing.

### 3. Data Preview and Inspection
Displays CSV data through the dashboard so users can inspect records and understand the structure of their datasets.

### 4. Missing Value Handling
Provides functionality to identify and clean missing values, helping users prepare datasets for further analysis.

### 5. Duplicate Record Removal
Helps eliminate duplicate rows from datasets to improve data consistency.

### 6. Processed CSV Download
Enables users to download processed CSV data for reuse in other applications, reports, or analytical workflows.

### 7. AWS S3 Integration
Includes AWS S3 integration to support cloud-storage operations, subject to the required AWS configuration and permissions.

### 8. Interactive Web Dashboard
Uses HTML, CSS, JavaScript, and Flask to provide an accessible interface for interacting with CSV-processing features.

## 🛠️ Technologies Used

| Technology | Role in the Project |
|---|---|
| Python | Core programming and application logic |
| Flask | Web application framework and API routes |
| Pandas | CSV manipulation, cleaning, and data analysis |
| HTML5 | Structure of the dashboard |
| CSS3 | Styling and layout |
| JavaScript | Frontend interactions with application APIs |
| AWS S3 | Cloud object storage integration |
| Git | Version control |
| GitHub | Source code hosting and project collaboration |
| Pytest | Automated testing, where configured |

## 🏗️ System Architecture

The application follows a simple web-based architecture.

1. **User Interface:** Users interact with the dashboard through a web browser.
2. **Backend Processing:** Flask handles incoming requests and coordinates application operations.
3. **Data Processing:** Pandas and Python utilities support CSV validation, cleaning, and processing.
4. **File Management:** The application provides functionality for accessing and downloading processed data.
5. **Cloud Storage:** AWS S3 integration supports configured cloud-storage operations.
6. **Testing:** Automated tests help verify selected application functions.

This architecture separates the user interface from the backend processing logic and supports future improvements.

## 📂 Project Structure

```text
publish-csv-python-aws/
│
├── app.py
├── main.py
├── upload_to_s3.py
├── data.csv
├── requirements.txt
├── README.md
│
├── services/
│   └── s3_service.py
│
├── utils/
│   └── csv_validator.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
├── tests/
│   └── test_csv.py
│
├── reports/
│   └── testing.report
│
├── Presentation/
└── REPORT/
```

*Note: The structure above represents the expected project layout. Update it if any files or folders differ in your repository.*

## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

- Python 3.x
- pip package manager
- Git
- A code editor such as Visual Studio Code

### Step 1: Clone the Repository

```bash
git clone https://github.com/Dhivya2006-3/publish-csv-python-aws.git
```

### Step 2: Navigate to the Project Directory

```bash
cd publish-csv-python-aws
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Start the Flask Application

```bash
python app.py
```

### Step 5: Open the Dashboard

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

The application can be accessed locally while the Flask server is running.

## ☁️ AWS S3 Configuration

AWS S3 can be used to store files in the cloud, subject to the application's implementation and configuration.

To enable cloud-related functionality:

1. Set up an AWS account and an S3 bucket if required.
2. Configure AWS credentials securely.
3. Provide the necessary bucket permissions.
4. Configure the application to use the appropriate bucket and region.
5. Test the upload workflow with a sample CSV file.

**Security Best Practice:** Never commit AWS access keys, secret keys, passwords, or other sensitive credentials to a public repository. Use environment variables or an AWS-supported credentials profile.

## 🧪 Testing and Validation

Testing is important for checking the reliability of CSV-processing operations.

Run the available tests using:

```bash
python -m pytest
```

Depending on the implemented tests, validation may cover:

- CSV input handling
- Data validation logic
- Missing-value processing
- Duplicate-row handling
- Expected application behavior

Test results depend on the current test suite and environment configuration.

## 🔐 Security and Reliability

The project can be operated more securely by following these practices:

- Validate uploaded files before processing.
- Handle invalid input and processing errors appropriately.
- Keep AWS credentials outside the source code.
- Apply appropriate access permissions to cloud resources.
- Test data-cleaning operations before using the output in critical workflows.

## 🚀 Future Enhancements

The project can be extended with additional capabilities, including:

- Deployment to a public cloud hosting platform.
- Interactive charts and visual summaries.
- Support for additional data-cleaning strategies.
- Improved validation and error messages.
- Better handling of large CSV files.
- User authentication and access control.
- Processing history and downloadable reports.
- Enhanced dashboard design and mobile responsiveness.

These enhancements could improve usability and expand the project's practical applications.

## 🏁 Conclusion

**Publish CSV File Using Python** demonstrates how Python programming, web technologies, data-processing libraries, and cloud services can be combined to simplify CSV file management.

By bringing CSV upload, validation, cleaning, preview, and download capabilities into a single dashboard, the project provides a foundation for more efficient data-handling workflows. AWS S3 integration further demonstrates how cloud storage can complement a Python-based application.

The project also offers practical experience in backend development, frontend integration, data processing, testing, and version control. Its modular structure provides opportunities for future improvements and additional analytics features.

---

## 🔗 Project Links

- **GitHub Repository:** [Explore the Source Code](https://github.com/Dhivya2006-3/publish-csv-python-aws)
- **Live Application:** Not deployed yet
- **Project Presentation:** [Open Presentation Folder](./Presentation/)
- **Project Report:** [Open Report Folder](./REPORT/)

---

*Developed as a Python-based CSV processing, data analytics, and cloud integration project.*
