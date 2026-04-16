"""
Terraform-specific PHCL layer.

This package builds on top of `phcl.core` and provides Terraform-shaped
declarations such as resources, data sources, variables, outputs, and modules.
"""

from .expressions import each, local, module, var
from .dialect import TerraformPHCL
from .nodes import Data, Module, Output, Resource, Variable
from .nodes import Locals, Provider, Terraform

__all__ = [
    "TerraformPHCL",
    "Resource",
    "Data",
    "Variable",
    "Output",
    "Module",
    "Provider",
    "Locals",
    "Terraform",
    "each",
    "var",
    "local",
    "module",
]
