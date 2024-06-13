"""Test case of CJK Width."""
import unittest

import utilities.cjk_width as cjkw

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class TestCJKWMethods(unittest.TestCase):
    def test_width(self):
        test_str = "asd謝謝茄子asd"
        self.assertEqual(cjkw.string_width(test_str), 14)

    def test_just(self):
        self.assertEqual(cjkw.ljust("こんにちは", 21, "_"), "こんにちは___________")
        self.assertEqual(cjkw.ljust("こんにちは", 21, "は"), "こんにちはははははは")
        self.assertEqual(cjkw.rjust("こんにちは", 21, "こ"), "ここここここんにちは")

    def test_cut(self):
        test_str = "asd茄子"
        self.assertEqual(repr(cjkw.cut(test_str, -9)), "('', 'asd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -8)), "('', 'asd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -7)), "('', 'asd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -6)), "('a', 'sd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -5)), "('as', 'd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -4)), "('asd', '茄子')")
        self.assertEqual(repr(cjkw.cut(test_str, -3)), "('asd茄', '子')")
        self.assertEqual(repr(cjkw.cut(test_str, -2)), "('asd茄', '子')")
        self.assertEqual(repr(cjkw.cut(test_str, -1)), "('asd茄子', '')")
        self.assertEqual(repr(cjkw.cut(test_str,  0)), "('', 'asd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str,  1)), "('a', 'sd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str,  2)), "('as', 'd茄子')")
        self.assertEqual(repr(cjkw.cut(test_str,  3)), "('asd', '茄子')")
        self.assertEqual(repr(cjkw.cut(test_str,  4)), "('asd', '茄子')")
        self.assertEqual(repr(cjkw.cut(test_str,  5)), "('asd茄', '子')")
        self.assertEqual(repr(cjkw.cut(test_str,  6)), "('asd茄', '子')")
        self.assertEqual(repr(cjkw.cut(test_str,  7)), "('asd茄子', '')")
        self.assertEqual(repr(cjkw.cut(test_str,  8)), "('asd茄子', '')")
        self.assertEqual(repr(cjkw.cut(test_str,  9)), "('asd茄子', '')")

    def test_overflow(self):
        test_str = 'asd私はガラスasd'
        with self.assertRaises(AssertionError):
            cjkw.overflow(test_str, 1)
        with self.assertRaises(AssertionError):
            cjkw.overflow(test_str, 2)
        self.assertEqual(cjkw.overflow(test_str,  3, "...", "_"), "...")
        self.assertEqual(cjkw.overflow(test_str,  4, "...", "_"), "a...")
        self.assertEqual(cjkw.overflow(test_str,  5, "...", "_"), "as...")
        self.assertEqual(cjkw.overflow(test_str,  6, "...", "_"), "asd...")
        self.assertEqual(cjkw.overflow(test_str,  7, "...", "_"), "asd..._")
        self.assertEqual(cjkw.overflow(test_str,  8, "...", "_"), "asd私...")
        self.assertEqual(cjkw.overflow(test_str,  9, "...", "_"), "asd私..._")
        self.assertEqual(cjkw.overflow(test_str, 10, "...", "_"), "asd私は...")
        self.assertEqual(cjkw.overflow(test_str, 11, "...", "_"), "asd私は..._")
        self.assertEqual(cjkw.overflow(test_str, 12, "...", "_"), "asd私はガ...")
        self.assertEqual(cjkw.overflow(test_str, 13, "...", "_"), "asd私はガ..._")
        self.assertEqual(cjkw.overflow(test_str, 14, "...", "_"), "asd私はガラ...")
        self.assertEqual(cjkw.overflow(test_str, 15, "...", "_"), "asd私はガラ..._")
        self.assertEqual(cjkw.overflow(test_str, 16, "...", "_"), "asd私はガラスasd")
        self.assertEqual(cjkw.overflow(test_str, 17, "...", "_"), "asd私はガラスasd")
