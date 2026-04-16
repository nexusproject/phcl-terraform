<h1>
  <img src="assets/phcl-logo-terraform-outline.svg" width="70" align="absmiddle"
       style="margin-right: 8px;">
  PHCL-TERRAFORM
  <img src="https://codecov.io/gh/nexusproject/phcl-terraform/branch/main/graph/badge.svg"
       align="right">
</h1>

PHCL-TERRAFORM is the Terraform dialect layer for PHCL.
For the core model, rendering, CLI behavior, and general PHCL documentation:

- [PHCL Core Repository](https://github.com/nexusproject/phcl)

## Installation

The intended install surface is:

```python
phcl["terraform"]
```

## Example

Instead of writing Terraform like this:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-123"
  instance_type = "t3.small"
}
```

the dialect aims to let you write:

```python
from phcl.terraform import Resource


class Web(Resource["aws_instance"]):
    ami = "ami-123"
    instance_type = "t3.small"
```
