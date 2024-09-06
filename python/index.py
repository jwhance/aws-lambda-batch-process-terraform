import json
import os
import time

import boto3

import dynamodb
import s3
import sqs


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')
S3_PREFIX = os.environ.get('S3_PREFIX')
DYNAMO_TABLE = os.environ.get('DYNAMO_TABLE')

SQS_CLIENT = boto3.client('sqs')

def lambda_handler(event, context):

    if ENVIRONMENT == 'dev':
        # print('Running in development mode')
        print(f'EVENT: {event}')

    # If triggered by SQS event, process the records in the payload
    if event.get('Records') and event['Records'][0].get('eventSource') == 'aws:sqs':
        # print('Event came from SQS')

        # Process each record and write to DynamoDb table
        for record in event.get('Records'):
            # print(record.get('body'))
            body_dict = json.loads(record.get('body'))
            result = dynamodb.write_item_to_table(dynamodb.TABLE, body_dict.get('Message'), body_dict.get('ObjectKey') + "_" + str(body_dict.get('LineNumber')))
            # print(result)


        print(f'Processed {len(event.get('Records'))} records from SQS')

        return {
            'message' : f'Wrote {len(event.get('Records'))} items to DynamoDb table {DYNAMO_TABLE}'
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

        queue_batch = []
        batch_count = 0
        lines = s3.get_s3_object_iterable_lines(bucket_name, object_key)
        for idx, line in enumerate(lines):

            queue_batch.append(
                {
                    'Id': str(idx), 
                    'MessageBody': {
                        'ObjectKey': object_key,
                        'LineNumber': idx,
                        'Message': line.decode('ascii')
                    }
                }
            )

            if len(queue_batch) >= 10:
                response = sqs.enqueue_to_sqs_batch(queue_batch, batch_count)
                queue_batch = []
                batch_count += 10

        if len(queue_batch) > 0:
            response = sqs.enqueue_to_sqs_batch(queue_batch, batch_count)

        end_time = time.time()

        print(f'=====> Queued {idx+1} records from S3 file: s3://{bucket_name}/{object_key} in {end_time-start_time} seconds.')

        return {
            'message' : f'Queued {idx+1} records from S3 file: s3://{bucket_name}/{object_key} in {end_time-start_time} seconds.'
        }
    
    return {
        'statusCode': 400,
        'body' : 'ERROR: UNKNOWN EVENT'
    }    