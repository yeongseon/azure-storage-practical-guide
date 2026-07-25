from __future__ import annotations

import importlib
from io import StringIO
from typing import Protocol

__all__ = ["build_yaml", "dump_frontmatter"]


class FrontmatterYaml(Protocol):
    def load(self, text: str) -> object: ...

    def dump(self, data: object, buffer: StringIO) -> None: ...


def build_yaml() -> FrontmatterYaml:
    yaml_module = importlib.import_module("ruamel.yaml")
    yaml_instance = yaml_module.YAML(typ="rt")
    yaml_instance.indent(mapping=2, sequence=4, offset=2)
    yaml_instance.preserve_quotes = True
    yaml_instance.width = 4096
    yaml_instance.explicit_end = False
    return yaml_instance


def dump_frontmatter(data: object, *, trailing_newline: bool = True) -> str:
    yaml = build_yaml()
    buffer = StringIO()
    yaml.dump(data, buffer)
    text = buffer.getvalue()
    if trailing_newline and not text.endswith("\n"):
        text += "\n"
    return text
