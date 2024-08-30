# *** LAMBDA FUNCTION ***

# Lambda function itself
resource "aws_lambda_function" "terraform_lambda_func" {
  filename         = "${path.module}/python/python-function.zip"
  function_name    = "lambda-${var.environment}-${var.application_name}"
  role             = aws_iam_role.lambda_role.arn
  handler          = "index.lambda_handler"
  runtime          = "python3.12"
  architectures    = ["arm64"]
  depends_on       = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
  source_code_hash = data.archive_file.zip_the_python_code.output_base64sha256
  environment {
    variables = {
      ENVIRONMENT    = "${var.environment}",
      SQS_QUEUE_URL  = "https://sqs.${var.environment}.amazonaws.com/${data.aws_caller_identity.current.account_id}/sqs-${var.environment}-${var.application_name}"
      S3_BUCKET_NAME = "s3-${var.environment}-${var.application_name}"
    }
  }
}

# Zip up the Python code
# Create the Python function's ZIP file for deployment
data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "${path.module}/python/"
  output_path = "${path.module}/python/python-function.zip"
}
