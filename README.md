# CSV Publisher and AWS Cloud Deployment System

A complete, professional Python-based project that generates structured CSV files and automates the deployment process to Amazon Web Services (AWS) S3. This project demonstrates how to connect Python scripts with cloud storage for secure and scalable data management.

## 📖 Project Overview

This project is designed to understand the integration of Python with cloud infrastructure. It utilizes Python's built-in `csv` module to generate data files and uses `boto3` (AWS SDK for Python) to seamlessly upload the generated CSV files to an Amazon S3 bucket. It serves as a practical demonstration of cloud storage and deployment.

## ✨ Features

* **Automated Data Generation:** Generates structured sample data and saves it locally as a `.csv` file.
* **Cloud Integration:** Uses the `boto3` library to securely connect to AWS.
* **Automated Deployment:** Automatically uploads the generated CSV file to a specified AWS S3 bucket.
* **Secure Configuration:** Handles AWS credentials securely using best practices.
* **Scalable Storage:** Demonstrates using AWS S3 for reliable and scalable cloud data storage.
* **Zero Manual Upload:** Fully scripted deployment process without needing to use the AWS web console.

## 🛠️ Technology Stack

| Layer | Technology Used |
| :--- | :--- |
| **Programming Language** | Python 3.x |
| **Data Format** | CSV (Comma Separated Values) |
| **Cloud Provider** | Amazon Web Services (AWS) |
| **AWS Service** | Amazon S3 (Simple Storage Service) |
| **AWS SDK** | Boto3 |
| **Version Control** | Git & GitHub |

## 📁 Folder Structure

```text
publish-csv-python-aws/
├── main.py              # Python script to generate the CSV file
├── upload_to_s3.py      # Python script to connect to AWS and upload the file
├── requirements.txt     # List of required Python libraries (boto3)
├── data.csv             # Sample generated CSV data (generated after running main.py)
├── .gitignore           # Files to ignore in Git
└── README.md            # Project documentation
