# Planted IaC misconfigurations. Never apply this.

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "testbed" {
  bucket = "scanner-testbed-public-bucket"
  # Planted: public ACL, no encryption, no versioning
  acl = "public-read"
}

resource "aws_security_group" "testbed" {
  name        = "scanner-testbed-open"
  description = "Planted: SSH open to the world"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
