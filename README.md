
# Publish CSV Files Generated Using Python and Deploy in AWS

## Project Overview
This project generates CSV files using Python and prepares them for deployment to Amazon Web Services (AWS) S3.

## Objectives
- Generate structured CSV files using Python.
- Store generated data in CSV format.
- Upload CSV files to AWS S3.
- Learn cloud storage and deployment.

## Technologies Used
- Python
- CSV module
- Boto3
- Amazon S3
- GitHub

## Project Files
- `main.py` - Generates the CSV file.
- `data.csv` - Sample generated CSV data.
- `requirements.txt` - Python dependency.
- `upload_to_s3.py` - Uploads the CSV to AWS S3.

## How to Run
1. Install Python.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run `python main.py`.
4. Configure AWS credentials securely.
5. Create an S3 bucket and configure its name in `upload_to_s3.py`.
6. Run `python upload_to_s3.py`.

## Project Status
CSV generation and GitHub upload are completed.
AWS deployment requires an active AWS account and S3 bucket.

