resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name         = "ddb-${var.environment}-${var.application_name}"
  billing_mode = "PAY_PER_REQUEST"
  #   read_capacity  = 5
  #   write_capacity = 10
  hash_key  = "Id"
  range_key = "Data"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "Data"
    type = "S"
  }

  ttl {
    attribute_name = "Ttl"
    enabled        = true
  }
}
