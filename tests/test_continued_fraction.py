import unittest
from fractions import Fraction

from algorithm_lab.continued_fraction import continued_fraction


class Tests(unittest.TestCase):
    def test_reconstruct_signed_rationals(self):
        for n in range(-25, 26):
            for d in range(-12, 13):
                if d == 0:
                    continue
                terms = continued_fraction(n, d)
                value = Fraction(terms[-1])
                for term in reversed(terms[:-1]):
                    value = term + 1 / value
                self.assertEqual(value, Fraction(n, d))
                self.assertTrue(all(x > 0 for x in terms[1:]))
                if len(terms) > 1:
                    self.assertGreater(terms[-1], 1)

    def test_invalid(self):
        for args in [(1, 0), (True, 1), (1, 2.5)]:
            with self.assertRaises(ValueError):
                continued_fraction(*args)
