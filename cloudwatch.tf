# *** CloudWatch Log ***

# Cloudwatch Log Group for Lambda - this explicitly creates a Cloudwatch log group
resource "aws_cloudwatch_log_group" "cloudwatch_log_group" {
  name              = "/aws/lambda/lambda-${var.environment}-${var.application_name}"
  retention_in_days = 1
  depends_on        = [aws_lambda_function.terraform_lambda_func]
}
