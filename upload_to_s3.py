
import boto3

BUCKET_NAME = "your-unique-bucket-name"
FILE_NAME = "data.csv"

s3 = boto3.client("s3")

s3.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)

print("CSV uploaded to AWS S3 successfully!")
