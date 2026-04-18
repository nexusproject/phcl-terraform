from phcl.core import Reference
from phcl.terraform import Data, Locals, Module, Output, Provider, Resource
from phcl.terraform import Terraform, TerraformPHCL, Variable, each, local, module, var


def test_public_api_exports():
    assert TerraformPHCL.__name__ == "TerraformPHCL"
    assert TerraformPHCL.extension == "tf"
    assert Resource.__name__ == "Resource"
    assert Data.__name__ == "Data"
    assert Variable.__name__ == "Variable"
    assert Output.__name__ == "Output"
    assert Module.__name__ == "Module"
    assert Provider.__name__ == "Provider"
    assert Locals.__name__ == "Locals"
    assert Terraform.__name__ == "Terraform"
    assert isinstance(each, Reference)
    assert each.source == "each"
    assert isinstance(var, Reference)
    assert var.source == "var"
    assert isinstance(local, Reference)
    assert local.source == "local"
    assert isinstance(module, Reference)
    assert module.source == "module"
