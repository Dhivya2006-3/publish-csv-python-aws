"""AWS S3 service utilities."""

import os
import boto3
from botocore.exceptions import BotoCoreError, ClientError


def validate_s3_configuration():
    bucket_name = os.getenv("AWS_S3_BUCKET")

    if not bucket_name:
        return {
            "configured": False,
            "message": "AWS S3 bucket is not configured."
        }

    return {
        "configured": True,
        "message": "AWS S3 bucket configuration is present."
    }


def upload_file_to_s3(file_path, object_name=None):
    bucket_name = os.getenv("AWS_S3_BUCKET")

    if not bucket_name:
        return {
            "success": False,
            "message": "AWS S3 bucket is not configured."
        }

    if not os.path.isfile(file_path):
        return {
            "success": False,
            "message": "File not found."
        }

    object_name = object_name or os.path.basename(file_path)

    try:
        s3 = boto3.client("s3")
        s3.upload_file(file_path, bucket_name, object_name)

        return {
            "success": True,
            "message": "File uploaded successfully.",
            "file_name": object_name
        }

    except (BotoCoreError, ClientError) as error:
        return {
            "success": False,
            "message": f"S3 upload failed: {error}"
        }
