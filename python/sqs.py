import json
import os

import boto3
import retry

SQS_QUEUE_URL = os.environ.get('SQS_QUEUE_URL')

SQS_CLIENT = boto3.client('sqs')

@retry.retry(tries=3, delay=2, backoff=2)
def enqueue_to_sqs(index: int, message: str) -> str:
    response = SQS_CLIENT.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=(
            json.dumps({'index': index, 'message': message})
        )
    )
    return response.get('MessageId')