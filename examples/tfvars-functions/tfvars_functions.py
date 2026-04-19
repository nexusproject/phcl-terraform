from phcl.terraform import TerraformPHCL as PHCL  # noqa: N812
from phcl.syntax import B
from phcl.terraform import (
    Output,
    Terraform,
    decode_tfvars,
    encode_expr,
    encode_tfvars,
)


class Settings(Terraform):
    required_version = ">= 1.8.0"
    required_providers = B(
        terraform={"source": "terraform.io/builtin/terraform"},
    )


class EncodedTfvars(Output):
    value = encode_tfvars(
        {
            "region": "us-east-1",
            "app_name": "ledger",
            "ports": [80, 443],
        }
    )


class EncodedExpr(Output):
    value = encode_expr(
        {
            "app_name": "ledger",
            "enabled": True,
        }
    )


class DecodedTfvars(Output):
    value = decode_tfvars('region = "us-east-1"')
