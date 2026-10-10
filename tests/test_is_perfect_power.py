import unittest

from algorithm_lab.is_perfect_power import is_perfect_power


class Tests(unittest.TestCase):
    def test_bounded_power_enumeration(self):
        limit = 2000
        powers = {
            base**exponent
            for base in range(2, 45)
            for exponent in range(2, 12)
            if base**exponent <= limit
        }
        for n in range(2, limit + 1):
            self.assertEqual(is_perfect_power(n), n in powers)

    def test_large_exact_powers(self):
        for base, exponent in ((2, 127), (3, 100), (2**100 + 13, 2)):
            self.assertTrue(is_perfect_power(base**exponent))

    def test_invalid(self):
        for n in (0, 1, -4, True, 4.0, "4", None):
            with self.assertRaises(ValueError):
                is_perfect_power(n)
