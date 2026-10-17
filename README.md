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

