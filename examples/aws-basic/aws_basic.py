from phcl.terraform import TerraformPHCL as PHCL  # noqa: N812

from phcl.syntax import B
from phcl.terraform import (
    Output,
    Provider,
    Resource,
    Terraform,
)


class Settings(Terraform):
    required_version = ">= 1.8.0"


class Aws(Provider["aws"]):
    region = "us-east-1"


class BackendRepository(Resource["aws_ecr_repository"]):
    name = "phcl-terraform-example"
    image_tag_mutability = "IMMUTABLE"
    image_scanning_configuration = B(scan_on_push=True)
    encryption_configuration = B(encryption_type="AES256")
    tags = {
        "Project": "phcl-terraform",
        "Example": "aws-basic",
    }


class RepositoryUrl(Output):
    value = BackendRepository._.repository_url
