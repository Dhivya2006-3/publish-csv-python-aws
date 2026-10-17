import boto3
import os
from botocore.exceptions import ClientError, NoCredentialsError

# 1. Change this to your actual AWS S3 bucket name
BUCKET_NAME = "your-actual-bucket-name-here" 

# 2. Make sure this file exists in the same folder
FILE_NAME = "data.csv" 

def upload_to_s3():
    try:
        # Boto3 will automatically look for credentials in ~/.aws/credentials
        s3 = boto3.client("s3")
        
        print(f"Uploading {FILE_NAME} to {BUCKET_NAME}...")
        
        # Upload the file
        s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
        
        print("✅ CSV uploaded to AWS S3 successfully!")
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{FILE_NAME}' was not found. Run main.py first.")
    except NoCredentialsError:
        print("❌ Error: AWS credentials not found. Please run 'aws configure'.")
    except ClientError as e:
        print(f"❌ AWS Error: {e}")

if __name__ == "__main__":
    upload_to_s3()
