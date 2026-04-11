from phcl.core.expression import Reference
from phcl.terraform import Data, Locals, Module, Output, Provider, Resource
from phcl.terraform import Terraform, Variable, each


def test_public_api_exports():
    assert Resource.__name__ == "Resource"
    assert Data.__name__ == "Data"
    assert Variable.__name__ == "Variable"
    assert Output.__name__ == "Output"
    assert Module.__name__ == "Module"
    assert Provider.__name__ == "Provider"
    assert Locals.__name__ == "Locals"
    assert Terraform.__name__ == "Terraform"
    assert isinstance(each, Reference)
    assert each.name == "each"
