import unittest

from algorithm_lab.base_conversion import base_conversion


class Tests(unittest.TestCase):
    def test_builtin_parser_roundtrip(self):
        for base in range(2, 37):
            for value in range(-200, 201):
                text = base_conversion(value, base)
                self.assertEqual(int(text, base), value)
                self.assertEqual(text, text.lower())
                self.assertFalse(text.lstrip("-").startswith("0") and text != "0")

    def test_builtin_formats(self):
        for base, specifier in ((2, "b"), (8, "o"), (16, "x")):
            for value in (0, -1, 1, -255, 255, 2**130 + 17):
                self.assertEqual(base_conversion(value, base), format(value, specifier))
        self.assertEqual(base_conversion(123), "123")
        self.assertEqual(base_conversion(-35, 36), "-z")

    def test_invalid(self):
        for args in ((True,), (1.5,), (None,), (2, 1), (2, 37), (2, True), (2, 2.5)):
            with self.assertRaises(ValueError):
                base_conversion(*args)
