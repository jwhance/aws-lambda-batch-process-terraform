SQS Event Example:

{
	'Records': [
		{
			'messageId': 'c62a7f0a-9c9a-405f-a77a-70456235e4b0', 
			'receiptHandle': 'AQEB+6U5MaQP3DCYoXYuQZC51Urq4Bu4U4bDuoBr1bclT8iIRty+KBBDaOhD/uhALbJlYGM/4e+fa/Q2UU9IoD1o+AJFKgKtXMl5CSdl3Dgtwhn7JRG75AZPPrKuSIinst7fDlX6ud6szpr0AdmTsdlc5B/av+5+4NhAUq6tRmjK4FF5V48XwVhL0fEkTUjoXqS1nPIVhirbqVu5YEbP9ko56LWyiyGc2qoFdeI6tHVNYcC4YMaCgcf/x8pM8bgORKDgCD0hLc6A4fa2JSBErYqQFmliQDlwMHYOwKZnvNlDmLc=',
			'body': '{"message": "Hello from Lambda!"}', 
			'attributes': {
				'ApproximateReceiveCount': '1', 
				'AWSTraceHeader': 'Root=1-66d1b4e3-626138ad2312c074529cde61;Parent=731e80a90b07d25b;Sampled=0;Lineage=6ce33430:0', 
				'SentTimestamp': '1725019364558', 
				'SequenceNumber': '18888349031036399616', 
				'MessageGroupId': '0001', 
				'SenderId': 'AROATHNK2AS5MROPHPUNL:lambda_dev_aws_terraform', 
				'MessageDeduplicationId': '614e15abe8e68a90d16eb2ece1920a5dbdda5501096b40ac3cf3407b7bf34224', 
				'ApproximateFirstReceiveTimestamp': '1725023816443'
			}, 
			'messageAttributes': {}, 
			'md5OfBody': 'afb60e570a7e889a52ef63e0768982b7', 
			'eventSource': 'aws:sqs', 
			'eventSourceARN': 'arn:aws:sqs:us-east-2:222085907642:sqs_dev_aws_terraform.fifo', 
			'awsRegion': 'us-east-2'
		}
	]
}

S3 Bucket Event Example:

{
    'Records': [
        {
            'eventVersion': '2.1', 
            'eventSource': 'aws:s3', 
            'awsRegion': 'us-east-2', 
            'eventTime': '2024-08-30T14:41:03.120Z', 
            'eventName': 'ObjectCreated:Put', 
            'userIdentity': {
                'principalId': 'A113FQK2B7L6JY'
            }, 
            'requestParameters': {
                'sourceIPAddress': '72.106.63.81'
            }, 
            'responseElements': {
                'x-amz-request-id': '3QGDED35AXS2G1NK', 
                'x-amz-id-2': '6SUrQC9RHc/8/aPZ+jhB0DizIpDt8XQl4vhtC9oWl2i6Hk5NN9l0yGLzEEwbxDdZEMe/9IZT9WjELzZpimVV6zk/YC4UUkYbjSCg8T4qSs0='
            }, 
            's3': {
                's3SchemaVersion': '1.0', 
                'configurationId': 'tf-s3-lambda-20240830143858898100000001', 
                'bucket': {
                    'name': 's3-dev-aws-terraform', 
                    'ownerIdentity': {
                        'principalId': 'A113FQK2B7L6JY'
                }, 
                    'arn': 'arn:aws:s3:::s3-dev-aws-terraform'
                }, 
                'object': {
                    'key': 'test.csv', 
                    'size': 9, 
                    'eTag': 'd85195f9b6b7a484db8e77aa06b183de', 
                    'sequencer': '0066D1D9FF0F5564B2'
                }
            }
        }
    ]
}