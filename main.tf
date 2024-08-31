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

variable "platform" {
  default = "arm64"
  # default = "x86_64"
}

variable "s3_bucket_prefix" {
  default = "inbound"
}

variable "filename_suffix" {
  default = ".zip"
}

# Provider.  AWS in this case.
provider "aws" {
  region = var.aws_region
}

data "aws_region" "current" {}
data "aws_caller_identity" "current" {}
