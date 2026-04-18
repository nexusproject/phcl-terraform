import pytest

from phcl.terraform import Data, Module, Resource, Variable


def test_resource_reference_base():
    class Web(Resource["aws_instance"]):
        pass

    assert Web._phcl_reference_base() == "aws_instance.web"


def test_data_reference_base():
    class AmazonLinux(Data["aws_ami"]):
        pass

    assert AmazonLinux._phcl_reference_base() == "data.aws_ami.amazon_linux"


def test_variable_reference_base():
    class Region(Variable):
        pass

    assert Region._phcl_reference_base() == "var.region"


def test_module_reference_base():
    class Vpc(Module):
        pass

    assert Vpc._phcl_reference_base() == "module.vpc"


def test_resource_requires_label():
    class Unlabeled(Resource):
        pass

    with pytest.raises(ValueError, match="Resource type is not set"):
        Unlabeled._phcl_reference_base()


def test_data_requires_label():
    class Unlabeled(Data):
        pass

    with pytest.raises(ValueError, match="Data source type is not set"):
        Unlabeled._phcl_reference_base()


def test_resource_for_each_keeps_mapping():
    mapping = {"a": {"name": "web-a"}}

    class Fleet(Resource["aws_instance"]):
        for_each = mapping

    assert Fleet.for_each == mapping


def test_resource_for_each_leaves_iterable_untouched():
    values = [{"name": "web-a"}, {"name": "web-b"}]

    class Fleet(Resource["aws_instance"]):
        for_each = values

    assert Fleet.for_each == values


def test_resource_for_each_leaves_strings_untouched():
    class Fleet(Resource["aws_instance"]):
        for_each = "literal"

    assert Fleet.for_each == "literal"


def test_module_for_each_leaves_iterable_untouched():
    values = ["a", "b"]

    class Child(Module):
        for_each = values

    assert Child.for_each == values
