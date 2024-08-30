# *** SQS Queue ***

resource "aws_sqs_queue" "terraform_queue" {
  name                        = "sqs-${var.environment}-${var.application_name}"
  content_based_deduplication = false
  fifo_queue                  = false
}

# SQS Event Source to trigger Lambda function
resource "aws_lambda_event_source_mapping" "event_source_mapping" {
  event_source_arn = aws_sqs_queue.terraform_queue.arn
  function_name    = aws_lambda_function.terraform_lambda_func.arn
  enabled          = true
  batch_size       = 10
  depends_on = [
    aws_sqs_queue.terraform_queue,
    aws_lambda_function.terraform_lambda_func
  ]
}
