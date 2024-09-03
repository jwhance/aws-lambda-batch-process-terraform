resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "ddb-${var.environment}-${var.application_name}"
  billing_mode   = "PROVISIONED"
  read_capacity  = 2
  write_capacity = 2
  hash_key       = "Id"
  range_key      = "Data"

  attribute {
    name = "Id"
    type = "S"
  }

  attribute {
    name = "Data"
    type = "S"
  }

  #   ttl {
  #     attribute_name = "TimeToExist"
  #     enabled        = true
  #   }
}
