terraform {
  required_version = ">= 1.8.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_ecr_repository" "backend_repository" {
  name = "phcl-terraform-example"
  image_tag_mutability = "IMMUTABLE"
  tags = {
    Project = "phcl-terraform"
    Example = "aws-basic"
  }

  image_scanning_configuration {
    scan_on_push = true
  }

  encryption_configuration {
    encryption_type = "AES256"
  }
}

output "repository_url" {
  value = aws_ecr_repository.backend_repository.repository_url
}
