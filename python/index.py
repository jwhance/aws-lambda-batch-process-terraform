import json
import os

import boto3


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')
S3_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME')

SQS_CLIENT = boto3.client('sqs')

def lambda_handler(event, context):

    if ENVIRONMENT == 'dev':
        print('Running in development mode')
        print(f'EVENT: {event}')

    # If triggered by SQS event, process the records in the payload
    if event.get('Records') and event['Records'][0].get('eventSource') == 'aws:sqs':
        print('Event came from SQS')
        return {
            'message' : 'Hello from SQS Event Handler'
        }
    
    # If triggered by S3 event, read the file and enqueue each record to the SQS Queue
    if event.get('Records') and event['Records'][0].get('eventSource') == 'aws:s3':
        print('Event came from S3') 
   
    # Write a message to SQS Queue
    print(f'Writing message to SQS Queue: {SQS_QUEUE_URL}')
    s3_filename = event.get('Records')[0].get('s3').get('object').get('key')

    try:
        response = SQS_CLIENT.send_message(
            QueueUrl=SQS_QUEUE_URL,
            MessageBody=(
                json.dumps({'s3_file': s3_filename})
            )
        )
        print(f'SQS Message ID: {response.get('MessageId')}')

    except Exception as e:
        print(e)
        return {
            'message' : f'Something went wrong: {e}'
        }        

    return {
        'message' : f'Queued all records in S3 file: {s3_filename}'
    }