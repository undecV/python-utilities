"""Test case of yaml representer."""

import unittest
import yaml

import utilities.yaml_representer as yrep


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class TestYrepMethods(unittest.TestCase):
    def test_double_quote(self):
        out = yaml.dump(yrep.AutoLiteralStr("lorem ipsum"))
        self.assertEqual(out, "\"lorem ipsum\"\n")

    def test_flow_dict(self):
        out = yaml.dump(yrep.FlowDict({"key_1": "value_1", "key_2": "value_2"}))
        self.assertEqual(out, "{key_1: value_1, key_2: value_2}\n")

    def test_flow_list(self):
        out = yaml.dump(yrep.FlowList(["item_1", "item_2", "item_3"]))
        self.assertEqual(out, "[item_1, item_2, item_3]\n")

    def test_literal_str(self):
        out = yaml.dump(yrep.LiteralStr("lorem ipsum"))
        self.assertEqual(out, "|-\n  lorem ipsum\n")
        out = yaml.dump(yrep.LiteralStr("lorem\nipsum"))
        self.assertEqual(out, "|-\n  lorem\n  ipsum\n")

    def test_auto_literal_str(self):
        out = yaml.dump(yrep.AutoLiteralStr("lorem ipsum"))
        self.assertEqual(out, "\"lorem ipsum\"\n")
        out = yaml.dump(yrep.AutoLiteralStr("lorem\nipsum"))
        self.assertEqual(out, "|-\n  lorem\n  ipsum\n")
