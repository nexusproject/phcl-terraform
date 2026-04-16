"""
Terraform dialect-level defaults.

This module holds small defaults that are specific to the Terraform dialect
surface, but are still meant to be consumed through the module-level `PHCL`
config contract in user files.
"""


class TerraformPHCL:
    """Default `PHCL` base for Terraform-oriented source files."""

    extension = "tf"
