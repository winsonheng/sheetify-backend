import datetime
from django.conf import settings
from google.cloud import storage


def generate_download_signed_url_v4(blob_name):
    """Generates a v4 signed URL for downloading a blob.

    Note that this method requires a service account key file. You can not use
    this if you are using Application Default Credentials from Google Compute
    Engine or from the Google Cloud SDK.
    """
    bucket_name = 'orbital-backend'

    storage_client = storage.Client(bucket_name, getattr(settings, 'GS_CREDENTIALS', ''))
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    url = blob.generate_signed_url(
        version="v4",
        # This URL is valid for 60 minutes
        expiration=datetime.timedelta(minutes=60),
        # Allow GET requests using this URL.
        method="GET",
    )

    return url


def cors_configuration():
    """Set a bucket's CORS policies configuration."""
    bucket_name = 'orbital-backend'

    storage_client = storage.Client(bucket_name, getattr(settings, 'GS_CREDENTIALS', ''))
    bucket = storage_client.get_bucket(bucket_name)
    bucket.cors = [
        {
            "origin": ["*"],
            "responseHeader": [
                "Access-Control-Allow-Origin",
                "Content-Type",
                "x-goog-resumable"],
            "method": ['PUT', 'POST'],
            "maxAgeSeconds": 3600
        }
    ]
    bucket.patch()

    print(f"Set CORS policies for bucket {bucket.name} is {bucket.cors}")
    return bucket
