import ast
import os
from typing import Generator

import boto3
from botocore.client import Config, ClientError
import retry

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-2')

S3_SESSION = boto3.Session()
S3_CLIENT = S3_SESSION.client(
    's3', 
    config=Config(signature_version='s3v4'), 
    region_name=AWS_REGION
)

def get_s3_presigned_url(bucket_name: str, object_key: str, client_action: str="put_object", expiration: int=3600) -> dict:
    return S3_CLIENT.generate_presigned_url(
        ClientMethod=client_action,
        Params={
            'Bucket': bucket_name,
            'Key': object_key
        },
        ExpiresIn=expiration
    )

def get_s3_presigned_post(bucket_name: str, object_key: str, expiration: int=3600) -> dict:
    return S3_CLIENT.generate_presigned_post(
        Bucket=bucket_name, 
        Key=object_key,
        Fields=None,
        Conditions=None,
        ExpiresIn=expiration
    )

@retry.retry(tries=3, delay=2)
def get_s3_file_size(bucket: str, key: str) -> int:
    """Gets the file size of S3 object by a HEAD request

    Args:
        bucket (str): S3 bucket
        key (str): S3 object path

    Returns:
        int: File size in bytes. Defaults to 0 if any error.
    """
    file_size = 0
    try:
        response = S3_CLIENT.head_object(Bucket=bucket, Key=key)
        if response:
            file_size = int(response.get('ResponseMetadata').get('HTTPHeaders').get('content-length'))
    
    except ClientError as e:
        print(f'Client error reading S3 file {bucket} : {key}')
        print(e)

    return file_size

@retry.retry(tries=3, delay=2)
def get_s3_object_iterable_lines(bucket: str, key: str) -> Generator[str, None, None]:
    s3_object = S3_SESSION.resource('s3').Object(bucket_name=bucket, key=key)
    return s3_object.get()['Body'].iter_lines()

@retry.retry(tries=3, delay=2)
def move_s3_object(source_bucket: str, source_key: str, dest_bucket: str, dest_key: str) -> None:
    copy_source = {
        'Bucket': source_bucket,
        'Key': source_key
    }
    S3_CLIENT.copy_object(
        CopySource=copy_source,
        Bucket=dest_bucket,
        Key=dest_key
    )

    # Now delete the original object
    S3_CLIENT.delete_object(
        Bucket=source_bucket,
        Key=source_key
    )