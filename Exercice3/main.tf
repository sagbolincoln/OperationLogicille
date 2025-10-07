provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bucket_s3_lincoln" {
  bucket = "lincoln-tf-test-bucket"
}