<h1>
  <img src="https://raw.githubusercontent.com/nexusproject/phcl-terraform/main/assets/phcl-logo-terraform-outline.svg" width="70" align="absmiddle"
       style="margin-right: 8px;">
  PHCL-Terraform
  <img src="https://codecov.io/gh/nexusproject/phcl-terraform/branch/main/graph/badge.svg"
       align="right">
</h1>

PHCL-Terraform is the Terraform dialect layer for PHCL.

For the core model, rendering, CLI behavior, and general PHCL documentation:

- [PHCL Core Repository](https://github.com/nexusproject/phcl)

## Installation

```bash
pip install 'phcl[terraform]'
```

## Example

Instead of writing Terraform like this:

```hcl
resource "aws_instance" "web" {
  ami           = "ami-123"
  instance_type = "t3.small"
}
```

PHCL aims to let you express the same declaration shape like this:

```python
class Web(Resource["aws_instance"]):
    ami = "ami-123"
    instance_type = "t3.small"
```
