import json
import os
import time

import boto3

import s3
import sqs


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
S3_PREFIX = os.environ.get('S3_PREFIX')

SQS_CLIENT = boto3.client('sqs')

def lambda_handler(event, context):

    if ENVIRONMENT == 'dev':
        print('Running in development mode')
        print(f'EVENT: {event}')

    # If triggered by SQS event, process the records in the payload
    if event.get('Records') and event['Records'][0].get('eventSource') == 'aws:sqs':
        print('Event came from SQS')

        for record in event.get('Records'):
            print(record.get('body'))

        print(f'Processed {len(event.get('Records'))} records from SQS')

        return {
            'message' : 'Hello from SQS Event Handler'
        }
    
    # If triggered by API Gateway event, process the payload
    if event.get('requestContext'):
        print('Event came from API Gateway')

        # Generate an S3 presigned URL for the S3 file
        presigned_url = s3.get_s3_presigned_url(S3_BUCKET_NAME, S3_PREFIX)
        presigned_post = s3.get_s3_presigned_post(S3_BUCKET_NAME, S3_PREFIX)

        return {
            'statusCode': 200,
            'body' : json.dumps({'presigned_url' : presigned_url, 'presigned_post': presigned_post})
        }
    
    # If triggered by S3 event, read the file and enqueue each record to the SQS Queue
    if event.get('Records') and event['Records'][0].get('eventSource') == 'aws:s3':
        print('Event came from S3')

        start_time = time.time()

        # s3.bucket.name and s3.object.key
        bucket_name = event.get('Records')[0].get('s3').get('bucket').get('name')
        object_key = event.get('Records')[0].get('s3').get('object').get('key')

        print(f'Bucket: {bucket_name}, Key: {object_key}, Size: {s3.get_s3_file_size(bucket_name, object_key)}')
        lines = s3.get_s3_object_iterable_lines(bucket_name, object_key)
        for idx, line in enumerate(lines):
            sqs_messageid = sqs.enqueue_to_sqs(idx, line.decode('ascii'))

        end_time = time.time()

        print(f'Queued {idx+1} records from S3 file: s3://{bucket_name}/{object_key} in {end_time-start_time} seconds.')

        return {
            'message' : f'Queued {idx+1} records from S3 file: s3://{bucket_name}/{object_key} in {end_time-start_time} seconds.'
        }
    
    return {
        'statusCode': 400,
        'body' : 'ERROR: UNKNOWN EVENT'
    }    