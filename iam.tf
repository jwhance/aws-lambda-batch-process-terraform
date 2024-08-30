# IAM Role for Lambda Function - this allows the Lambda function to assume the role and use the policies that are attached
resource "aws_iam_role" "lambda_role" {
  name               = "role-${var.environment}-${var.application_name}"
  assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "lambda.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF
}

# Lambda policy statement - these are the permissions that the Lambda will have at runtime
resource "aws_iam_policy" "iam_policy_for_lambda" {

  name        = "policy-${var.environment}-${var.application_name}"
  path        = "/"
  description = "AWS IAM Policy for managing aws lambda role"
  policy      = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": [
       "logs:CreateLogGroup",
       "logs:CreateLogStream",
       "logs:PutLogEvents"
     ],
     "Resource": "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/lambda-${var.environment}-${var.application_name}*",
     "Effect": "Allow"
   },
   {
     "Action": [
       "sqs:SendMessage",
       "sqs:ReceiveMessage",
       "sqs:DeleteMessage",
       "sqs:GetQueueAttributes"
     ],
     "Resource": "arn:aws:sqs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:sqs-${var.environment}-${var.application_name}",
     "Effect": "Allow"
   },
   {
    "Action": [
      "s3:GetObject",
      "s3:PutObject",
      "s3:DeleteObject"
    ],
    "Resource": "arn:aws:s3:::s3-${var.environment}-${var.application_name}",
    "Effect": "Allow"
   }  
 ]
}
EOF
}

# Attach policy to role
resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.iam_policy_for_lambda.arn
}
