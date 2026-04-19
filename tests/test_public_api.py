from phcl.core import Expression, Reference
from phcl.terraform import Data, Locals, Module, Output, Provider, Resource
from phcl.terraform import Terraform, TerraformPHCL, Variable
from phcl.terraform import decode_tfvars, each, encode_expr, encode_tfvars, local, module, var


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


def test_terraform_specific_functions_render_provider_calls():
    encoded_tfvars = encode_tfvars({"example": "Hello!"})
    decoded_tfvars = decode_tfvars('example = "Hello!"')
    encoded_expr = encode_expr({"enabled": True})

    assert isinstance(encoded_tfvars, Expression)
    assert encoded_tfvars.source == 'provider::terraform::encode_tfvars({example = "Hello!"})'

    assert isinstance(decoded_tfvars, Expression)
    assert decoded_tfvars.source == 'provider::terraform::decode_tfvars("example = \\"Hello!\\"")'

    assert isinstance(encoded_expr, Expression)
    assert encoded_expr.source == 'provider::terraform::encode_expr({enabled = true})'
