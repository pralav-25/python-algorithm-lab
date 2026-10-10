import math
import unittest

from algorithm_lab.primitive_root import primitive_root


class Tests(unittest.TestCase):
    def test_residue_group_oracle(self):
        for modulus in range(2, 120):
            units = {value for value in range(1, modulus) if math.gcd(value, modulus) == 1}
            expected = next(
                (
                    value
                    for value in sorted(units)
                    if {pow(value, exponent, modulus) for exponent in range(1, len(units) + 1)}
                    == units
                ),
                None,
            )
            self.assertEqual(primitive_root(modulus), expected)

    def test_invalid(self):
        for modulus in (0, 1, -2, True, 2.5, "7", None):
            with self.assertRaises(ValueError):
                primitive_root(modulus)
