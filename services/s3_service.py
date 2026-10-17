
"""AWS S3 configuration helpers."""

import os


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
