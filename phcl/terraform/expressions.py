from phcl.core import Expression, Reference
from phcl.core.expression import render_expression_value


each = Reference("each")
var = Reference("var")
local = Reference("local")
module = Reference("module")


def _terraform_function(name: str, *args) -> Expression:
    rendered = ", ".join(render_expression_value(arg) for arg in args)
    return Expression(f"provider::terraform::{name}({rendered})")


def encode_tfvars(value) -> Expression:
    return _terraform_function("encode_tfvars", value)


def decode_tfvars(value) -> Expression:
    return _terraform_function("decode_tfvars", value)


def encode_expr(value) -> Expression:
    return _terraform_function("encode_expr", value)
