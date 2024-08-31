import os

import boto3
from botocore.client import Config

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-2')
S3_SESSION = boto3.Session()
S3_CLIENT = S3_SESSION.client('s3', config=Config(signature_version='s3v4'), region_name=AWS_REGION)

def get_s3_presigned_url(bucket_name, object_key, client_action="put_object", expiration=3600):
    return S3_CLIENT.generate_presigned_url(
        ClientMethod=client_action,
        Params={
            'Bucket': bucket_name,
            'Key': object_key
        },
        ExpiresIn=expiration
    )

def get_s3_presigned_post(bucket_name, object_key, expiration=3600):
    return S3_CLIENT.generate_presigned_post(
        Bucket=bucket_name, 
        Key=object_key,
        Fields=None,
        Conditions=None,
        ExpiresIn=expiration
    )