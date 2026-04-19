terraform {
  required_version = ">= 1.8.0"

  required_providers {
    terraform = {
      source = "terraform.io/builtin/terraform"
    }
  }
}

output "encoded_tfvars" {
  value = provider::terraform::encode_tfvars({region = "us-east-1", app_name = "ledger", ports = [80, 443]})
}

output "encoded_expr" {
  value = provider::terraform::encode_expr({app_name = "ledger", enabled = true})
}

output "decoded_tfvars" {
  value = provider::terraform::decode_tfvars("region = \"us-east-1\"")
}
