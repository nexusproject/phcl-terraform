"""
Terraform-specific top-level declaration nodes.

These classes adapt the generic PHCL core model to Terraform block kinds while
preserving the declarative class-based style of the base DSL.
"""

from phcl.core import Node
from phcl.syntax import abstract


@abstract
class Resource(Node):
    """
    Terraform resource block.

    Usage:
        class Web(Resource["aws_instance"]):
            ...
    """

    @classmethod
    def _phcl_reference_base(cls) -> str:
        labels = list(getattr(cls, "_phcl_label", []) or [])
        logical_name = cls._phcl_logical_name()
        if not labels:
            raise ValueError(f"Resource type is not set for {cls.__name__}")
        return f"{labels[0]}.{logical_name}"


@abstract
class Data(Node):
    """
    Terraform data source block.

    Usage:
        class AmazonLinux(Data["aws_ami"]):
            ...
    """

    @classmethod
    def _phcl_reference_base(cls) -> str:
        labels = list(getattr(cls, "_phcl_label", []) or [])
        logical_name = cls._phcl_logical_name()
        if not labels:
            raise ValueError(f"Data source type is not set for {cls.__name__}")
        return f"data.{labels[0]}.{logical_name}"


@abstract
class Variable(Node):
    """
    Terraform variable block.

    Usage:
        class Region(Variable):
            type = "string"
            default = "us-east-1"
    """

    @classmethod
    def _phcl_reference_base(cls) -> str:
        return f"var.{cls._phcl_logical_name()}"


@abstract
class Output(Node):
    """
    Terraform output block.

    Usage:
        class InstanceId(Output):
            value = expr("aws_instance.web.id")
    """

    @classmethod
    def _phcl_reference_base(cls) -> str:
        return cls._phcl_logical_name()


@abstract
class Module(Node):
    """
    Terraform module block.

    Usage:
        class Vpc(Module):
            source = "./modules/vpc"
    """

    @classmethod
    def _phcl_reference_base(cls) -> str:
        return f"module.{cls._phcl_logical_name()}"


@abstract
class Provider(Node):
    """
    Terraform provider block.

    Usage:
        class Aws(Provider["aws"]):
            region = "us-east-1"
    """


@abstract
class Locals(Node):
    """
    Terraform locals block.

    Usage:
        class Shared(Locals):
            project = "demo"
    """


@abstract
class Terraform(Node):
    """
    Terraform settings block.

    Usage:
        class Settings(Terraform):
            required_version = ">= 1.8.0"
    """
