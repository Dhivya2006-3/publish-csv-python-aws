
"""AWS S3 service helpers for the CSV Studio project."""


def validate_s3_configuration():
    """Check whether the required S3 configuration exists."""
    import os

    bucket_name = os.getenv("AWS_S3_BUCKET")

    if not bucket_name:
        return {
            "configured": False,
            "message": "AWS_S3_BUCKET is not configured."
        }

    return {
        "configured": True,
        "message": "S3 bucket configuration is present."
    }
