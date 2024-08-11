"""
Yaml Representer

Reference:
- https://stackoverflow.com/a/7445560
- https://stackoverflow.com/a/14001707
- https://stackoverflow.com/a/33300001
"""

from typing import Any
import yaml


DEFAULT_TILDE_NULL = True
DEFAULT_DOUBLE_QUOTE = False

YAML_DUMP_CONFIG = {
    "indent": 2,
    "sort_keys": False,
    "allow_unicode": True,
    "width": float("inf"),
    # "default_flow_style": True,
}


# Double Quote

def string_representer(dumper, data: str, style='"'):
    """Represent a string as `\"String\"`."""
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style=style)


if DEFAULT_DOUBLE_QUOTE:
    yaml.add_representer(str, string_representer)


class DoubleQuoteStr(str, yaml.YAMLObject):  # type: ignore
    """Represent a string as `\"String\"`."""
    yaml_tag = '!DoubleQuoteStr'

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return string_representer(dumper, data)


# Tilde None

def none_representer(dumper, _):
    """Represent None / Null as `~`."""
    return dumper.represent_scalar('tag:yaml.org,2002:null', '~')


if DEFAULT_TILDE_NULL:
    yaml.add_representer(type(None), none_representer)


# Flow Dict

def dict_representer(dumper, data, flow_style=True):  # type: ignore
    """Force Represent Dict / Object as flow style."""
    return dumper.represent_mapping('tag:yaml.org,2002:map', data, flow_style=flow_style)


class FlowDict(dict, yaml.YAMLObject):  # type: ignore
    """Force Represent Dict / Object as flow style."""
    yaml_tag = '!FlowDict'
    yaml_flow_style = True

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return dict_representer(dumper, data, flow_style=cls.yaml_flow_style)


# Flow List

def list_representer(dumper, data, flow_style=True):
    """Force Represent List / Array as flow style."""
    return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=flow_style)


class FlowList(list, yaml.YAMLObject):  # type: ignore
    """Force Represent List / Array as flow style."""
    yaml_tag = '!FlowList'
    yaml_flow_style = True

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return list_representer(dumper, data, flow_style=cls.yaml_flow_style)


# Auto Flow List

def auto_flow_list_representer(dumper, data):
    """Use flow represent only if the list has more than one line."""
    if len(data) > 1:
        return list_representer(dumper, data, flow_style=False)
    return list_representer(dumper, data, flow_style=True)


class AutoFlowList(list, yaml.YAMLObject):  # type: ignore
    """Use flow represent only if the list has more than one line."""
    yaml_tag = '!AutoFlowList'

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return auto_flow_list_representer(dumper, data)


# Literal String

class LiteralStr(str, yaml.YAMLObject):  # type: ignore
    """Represent string as Literal `|` style."""
    yaml_tag = '!LiteralStr'

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return string_representer(dumper, data, style='|')


# Auto-Literal String

def auto_literal_str_representer(dumper, data):
    """Use literal represent only if the string has more than one line."""
    if len(data.splitlines()) > 1:
        return string_representer(dumper, data, style='|')
    return string_representer(dumper, data, style='"')


class AutoLiteralStr(str, yaml.YAMLObject):  # type: ignore
    """Represent string as Literal `|` style."""
    yaml_tag = '!AutoLiteralStr'

    @classmethod
    def to_yaml(cls, dumper: yaml.Dumper, data: Any) -> yaml.Node:
        return auto_literal_str_representer(dumper, data)


if __name__ == "__main__":
    pass
