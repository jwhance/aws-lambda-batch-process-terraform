import json
import os

import boto3
import retry

AWS_REGION = os.environ.get('AWS_REGION', 'us-east-2')
DYNAMODB = boto3.resource('dynamodb', region_name=AWS_REGION)
TABLE = DYNAMODB.Table(os.environ.get('DYNAMO_TABLE', 'ddb-dev-lambda-batch-processor'))
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-2')

@retry.retry(exceptions=Exception, tries=3, delay=2)
def write_item_to_table(table_resource, item_body: str, item_id: int, ttl: int) -> dict:
    response = table_resource.put_item(
        Item={
            'Id': str(item_id),
            'Ttl': ttl,
            'Data': item_body
        }
    )
    return response

# Not used in the application but useful for testing if you need to clear the table without deleting and re-creating it.
#
# usage:
#           python
#           import dynamodb
#           dynamodb.delete_all_table_items(dynamodb.TABLE)
#
def delete_all_table_items(table_resource) -> None:
    scan = table_resource.scan()
    with table_resource.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'Id': each['Id'],
                    'Data': each['Data']
                }
            )
