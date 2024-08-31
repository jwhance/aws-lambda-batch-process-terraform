# *** S3 Bucket ***

# An S3 Bucket to handle the file drop
resource "aws_s3_bucket" "file_drop_bucket" {
  bucket = "s3-${var.environment}-${var.application_name}"
}

# This allows the S3 Bucket to invoke the Lambda function. (Resource-based permission)
resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.terraform_lambda_func.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.file_drop_bucket.arn
  depends_on = [
    aws_lambda_function.terraform_lambda_func,
    aws_s3_bucket.file_drop_bucket
  ]
}

# Setup S3 Bucket ObjectCreated notification to trigger Lambda
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.file_drop_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.terraform_lambda_func.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "${var.s3_bucket_prefix}/"
    filter_suffix       = var.filename_suffix
  }

  depends_on = [
    aws_sqs_queue.terraform_queue,
    aws_s3_bucket.file_drop_bucket
  ]
}
