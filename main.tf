terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Variables
variable "application_name" {
  default = "lambda-batch-processor"
}

variable "aws_region" {
  default = "us-east-2"
}

variable "environment" {
  default = "dev"
}

# Provider.  AWS in this case.
provider "aws" {
  region = var.aws_region
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
