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

API Gateway Example

{
    'version': '1.0', 
    'resource': '/handler', 
    'path': '/dev/handler', 
    'httpMethod': 'GET', 
    'headers': {
        'Content-Length': '0', 
        'Host': 'ms7r4pc4u0.execute-api.us-east-2.amazonaws.com', 
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', 
        'X-Amzn-Trace-Id': 'Root=1-66d22c3e-2a93ccf573a01ec008cc84b8', 
        'X-Forwarded-For': '72.106.63.81', 
        'X-Forwarded-Port': '443', 
        'X-Forwarded-Proto': 'https', 
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
        'accept-encoding': 'gzip, deflate, br, zstd', 
        'accept-language': 'en-US,en;q=0.9', 
        'cache-control': 'max-age=0', 
        'dnt': '1', 
        'priority': 'u=0, i', 
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"', 
        'sec-ch-ua-mobile': '?0', 
        'sec-ch-ua-platform': '"Windows"', 
        'sec-fetch-dest': 'document', 
        'sec-fetch-mode': 'navigate', 
        'sec-fetch-site': 'none', 
        'sec-fetch-user': '?1', 
        'upgrade-insecure-requests': '1'
    }, 
    'multiValueHeaders': {
        'Content-Length': ['0'], 
        'Host': ['ms7r4pc4u0.execute-api.us-east-2.amazonaws.com'], 
        'User-Agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'], 
        'X-Amzn-Trace-Id': ['Root=1-66d22c3e-2a93ccf573a01ec008cc84b8'], 
        'X-Forwarded-For': ['72.106.63.81'], 
        'X-Forwarded-Port': ['443'], 
        'X-Forwarded-Proto': ['https'], 
        'accept': ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'], 
        'accept-encoding': ['gzip, deflate, br, zstd'], 
        'accept-language': ['en-US,en;q=0.9'], 
        'cache-control': ['max-age=0'], 
        'dnt': ['1'], 
        'priority': ['u=0, i'], 
        'sec-ch-ua': ['"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"'], 
        'sec-ch-ua-mobile': ['?0'], 
        'sec-ch-ua-platform': ['"Windows"'], 
        'sec-fetch-dest': ['document'], 
        'sec-fetch-mode': ['navigate'], 
        'sec-fetch-site': ['none'], 
        'sec-fetch-user': ['?1'], 
        'upgrade-insecure-requests': ['1']
    }, 
    'queryStringParameters': None, 
    'multiValueQueryStringParameters': None, 
    'requestContext': {
        'accountId': '222085907642', 
        'apiId': 'ms7r4pc4u0', 
        'domainName': 'ms7r4pc4u0.execute-api.us-east-2.amazonaws.com', 
        'domainPrefix': 'ms7r4pc4u0', 
        'extendedRequestId': 'dVvZ1js5CYcEMhQ=', 
        'httpMethod': 'GET', 
        'identity': {
            'accessKey': None, 
            'accountId': None, 
            'caller': None, 
            'cognitoAmr': None, 
            'cognitoAuthenticationProvider': None, 
            'cognitoAuthenticationType': None, 
            'cognitoIdentityId': None, 
            'cognitoIdentityPoolId': None, 
            'principalOrgId': None, 
            'sourceIp': '72.106.63.81', 
            'user': None, 
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36', 
            'userArn': None
        }, 
        'path': '/dev/handler', 
        'protocol': 'HTTP/1.1', 
        'requestId': 'dVvZ1js5CYcEMhQ=', 
        'requestTime': '30/Aug/2024:20:31:58 +0000', 
        'requestTimeEpoch': 1725049918660, 
        'resourceId': 'GET /handler', 
        'resourcePath': '/handler', 
        'stage': 'dev'
    }, 
    'pathParameters': None, 
    'stageVariables': None, 
    'body': None, 
    'isBase64Encoded': False
}