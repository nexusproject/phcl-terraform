import re
import sys
import types
from pathlib import Path


def _to_snake_case(name: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()


repo_root = Path(__file__).resolve().parents[1]
phcl_root = repo_root / "phcl"

phcl_module = types.ModuleType("phcl")
phcl_module.__path__ = [str(phcl_root)]

core_module = types.ModuleType("phcl.core")
decorators_module = types.ModuleType("phcl.core.decorators")
expression_module = types.ModuleType("phcl.core.expression")
nodes_module = types.ModuleType("phcl.core.nodes")


def abstract(cls):
    return cls


class Reference:
    def __init__(self, name: str):
        self.name = name

    def __getattr__(self, item: str):
        return Reference(f"{self.name}.{item}")

    def __repr__(self) -> str:
        return f"Reference({self.name!r})"


class Node:
    _phcl_label = None

    def _phcl_normalize_attr(self, name, value):
        return value

    @classmethod
    def __class_getitem__(cls, label):
        labels = [label] if isinstance(label, str) else list(label)
        return type(f"{cls.__name__}Labeled", (cls,), {"_phcl_label": labels})

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        normalizer = cls.__new__(cls)
        for name, value in list(cls.__dict__.items()):
            if name.startswith("_"):
                continue
            normalized = cls._phcl_normalize_attr(normalizer, name, value)
            if normalized is not value:
                setattr(cls, name, normalized)

    @classmethod
    def _phcl_logical_name(cls) -> str:
        return _to_snake_case(cls.__name__)


decorators_module.abstract = abstract
expression_module.Reference = Reference
nodes_module.Node = Node

core_module.decorators = decorators_module
core_module.expression = expression_module
core_module.nodes = nodes_module

phcl_module.core = core_module

sys.modules["phcl"] = phcl_module
sys.modules["phcl.core"] = core_module
sys.modules["phcl.core.decorators"] = decorators_module
sys.modules["phcl.core.expression"] = expression_module
sys.modules["phcl.core.nodes"] = nodes_module
