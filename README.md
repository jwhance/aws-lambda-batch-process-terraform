SQS Event Example:

{
    'Records': 
    [
        {
            'messageId': 'bf178cec-5a87-451f-ac46-f94426479f28', 
            'receiptHandle': 'AQEBRfrFi1nASeH6Tf+Nryl3q+aDImOOpdrzHORBtrvcFvYGYbjhlRbRDucCd9tvMzd+tlfW7/PWxRbcPoxoOgc1mwei90wkBibnkiVP1jGUbX9l5SmpopFWhiODEulh8nLHhR0nrcUhF2A/TiawCaavcrosGKNZQCykV0tqbuJ+L2O2hffhzh+oZF96KETUv8shmMkEkR8Buni601bx6NzfMnSnY0hadUd2V7pRx6VN2zgAC48XOydFgnVoz47mh0cD3ytthVvL1SBC9DRQqPzkyhJ1wbpy/x9vjpUsqEep0Udm/W77+OlgVV2ycUGBXzAkUSqdGW8yUVY1LigmNUEMuqXygBgGT/Vy6hHKbPOlDDRX3/r58Wqw4RzPPO5tca4LNoe7gL5Y+LDfbaBF0qROKsPY+G4lFAxyONgVWksGzsM=',
             'body': '"Sub-Saharan Africa,The Gambia,Baby Food,Offline,M,2/3/2014,494747245,3/20/2014,5559,255.28,159.42,1419101.52,886215.78,532885.74"', 
             'attributes': 
             {
                'ApproximateReceiveCount': '1', 
                'AWSTraceHeader': 'Root=1-66dad809-78bc1ad55e3eeb134b7a05a0;Parent=264cfe75b9d268e2;Sampled=0;Lineage=1:930743c5:0', 
                'SentTimestamp': '1725618187358', 
                'SenderId': 'AROATHNK2AS5GLKI3CFZC:lambda-dev-lambda-batch-processor', 
                'ApproximateFirstReceiveTimestamp': '1725618187799'
            }, 
            'messageAttributes': {}, 
            'md5OfBody': '525b786a906cf2d74b9974bbff70f52a', 
            'eventSource': 'aws:sqs', 
            'eventSourceARN': 'arn:aws:sqs:us-east-2:XXXXXXXXXXXX:sqs-dev-lambda-batch-processor', 
            'awsRegion': 'us-east-2'
        }, 
        {
            'messageId': 'a0234671-3dbd-47aa-99f1-09021bdd7c46', 
            'receiptHandle': 'AQEBorjQ4Ls/pJyZA9oLnEEoFny3koMv0IC67wf5iM0si1BM8KbPTACLPYdmWQfY/9SI334Pv+4OXxsws//m9AwlDOCdA1LixyewuqhzMHw1rEIDOXwzUV4fctwYs0YbczYHwMMEtw/KIakd2ss7Oj/Hs5Me3wPiM9Faot1FunXggb+t5HCsY9OIwITHMhik/+Xs21UQZBGeHEuO3Vy6iPsr08OqiCilBM+Me8e1PCSMJQJ0UzMwU56F1/jqV8TCkTDqj53wD6OUqYMih8XQRaebcdqHnJG6chxEsKWqCG6Mn/5ZyC2d40jCtB9JVOl5H7EFRBG34KeUPga5QwwRrIjs1I3J8CX867LBnd6pofS4HyDvrecVzmZ1aJJ8BTSxebeFhiPyUxgwmOIyrCDa+V3ACePgbSWQn8QonF9ndcpjvjg=', 
            'body': '"Middle East and North Africa,Kuwait,Fruits,Online,M,4/30/2012,513417565,5/18/2012,522,9.33,6.92,4870.26,3612.24,1258.02"', 
            'attributes': 
            {
                'ApproximateReceiveCount': '1', 
                'AWSTraceHeader': 'Root=1-66dad809-78bc1ad55e3eeb134b7a05a0;Parent=264cfe75b9d268e2;Sampled=0;Lineage=1:930743c5:0', 
                'SentTimestamp': '1725618187360', 
                'SenderId': 'AROATHNK2AS5GLKI3CFZC:lambda-dev-lambda-batch-processor', 
                'ApproximateFirstReceiveTimestamp': '1725618187799'
            }, 
            'messageAttributes': {}, 
            'md5OfBody': 'a1d56634bc42f1b896b9071542e2172d', 
            'eventSource': 'aws:sqs', 
            'eventSourceARN': 'arn:aws:sqs:us-east-2:XXXXXXXXXXXX:sqs-dev-lambda-batch-processor', 
            'awsRegion': 'us-east-2'
        }, 
        {
            'messageId': 'c2853962-70e6-455e-bc6d-4014e4e29c11', 
            'receiptHandle': 'AQEB+GwMqU1LN5NYOcpCSDsneVgJkSkPVPLEBnc/oOeU2QKQDJzmkQ6ofrhpTsVC2J7VrCxaH6QCXj2qNoqZ+3DX9MdnyUxROQHWrCg8ecdzq5hufYJFIFTNH8wDnnUzW8lJjHQfOfMo3BzSKqoJEo3rp5uydhSB8i/CxLWudiUCKNvvKtk1lgWQotiyTKTmO9cGwz+09VhJ5l+sJZDncOB5mI5pHuuYErP3oxV8Wh5nQ4sKMI9CIIb2ytYpq82kDE4yCUan96gnv3ftF70QbU37HYnfa2KhkanE4f/wkORyWP6ar6T4sH4DJzft5Sv+7yFEFCiWjw+8I8WvcdTLWJyHm8yKkwby36aOUMjM+mxD5Ds1Ce00EOp4XbvSdWZ00vPEp13SOCCjvRB8oJonSMaX7v9LujiApLohGLzgE2OONrc=', 
            'body': '"Europe,Slovenia,Beverages,Offline,C,10/23/2016,345718562,11/25/2016,4660,47.45,31.79,221117.00,148141.40,72975.60"', 
            'attributes': 
            {
                'ApproximateReceiveCount': '1', 
                'AWSTraceHeader': 'Root=1-66dad809-78bc1ad55e3eeb134b7a05a0;Parent=264cfe75b9d268e2;Sampled=0;Lineage=1:930743c5:0', 
                'SentTimestamp': '1725618187367', 
                'SenderId': 'AROATHNK2AS5GLKI3CFZC:lambda-dev-lambda-batch-processor', 
                'ApproximateFirstReceiveTimestamp': '1725618187799'
            }, 
            'messageAttributes': {}, 
            'md5OfBody': 'fb77b5834cf7dfa46377a75a563dcefe', 
            'eventSource': 'aws:sqs', 
            'eventSourceARN': 'arn:aws:sqs:us-east-2:XXXXXXXXXXXX:sqs-dev-lambda-batch-processor', 
            'awsRegion': 'us-east-2'
        }, 
        {
            'messageId': 'c8953c34-e009-4cf9-b427-e10a7b58934a', 
            'receiptHandle': 'AQEBC+ZRQmgazxBsxpRGN9bDkglZ1b/J44XuRigwXdsgcr5kSI3wPleyQ4WGWOqECkA3S6rEjeD4OIyFl67tn+HGwnC3KmYBHdCKuDU7/mK5EFVl+KVYzWznsTv5zlzNCozWJ6QEbpFiCoMrrufZ6XFSBcNLJ3dfdYFt8IVQBFIhtetW2uS0F1EUHa/vZ5Aq7kglnT4rHlDoqqBCXYSToMZUHlnsXW8rLm8ulK8oo3MglCokZ4rS1RrwZ3rAQEMPpLCTtokwIhIFYd44rK9bVmyx34mL0zC0VtiHlHuabMYcRlI1YliI++IDeOYIGQnf4U82QVuBZ/Wh4pp5IbS66hYRq2DYU09GmuW9yEPTy8Nq+X0GKYNpvbzM0rQDg2OxSjUTn3kqchGTZkZa6BWUjxz9qECL4VwexCWeSrjTfjEgsf0=', 'body': '"Sub-Saharan Africa,Sierra Leone,Office Supplies,Offline,H,12/6/2016,621386563,12/14/2016,948,651.21,524.96,617347.08,497662.08,119685.00"', 
            'attributes': 
            {
                'ApproximateReceiveCount': '1', 
                'AWSTraceHeader': 'Root=1-66dad809-78bc1ad55e3eeb134b7a05a0;Parent=264cfe75b9d268e2;Sampled=0;Lineage=1:930743c5:0', 
                'SentTimestamp': '1725618187369', 
                'SenderId': 'AROATHNK2AS5GLKI3CFZC:lambda-dev-lambda-batch-processor', 
                'ApproximateFirstReceiveTimestamp': '1725618187799'
            }, 
            'messageAttributes': {}, 
            'md5OfBody': '190a1d766801e89716718dca61bcf90d', 
            'eventSource': 'aws:sqs', 
            'eventSourceARN': 'arn:aws:sqs:us-east-2:XXXXXXXXXXXX:sqs-dev-lambda-batch-processor', 
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
        'accountId': 'XXXXXXXXXXXX', 
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