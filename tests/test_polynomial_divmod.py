import random
import unittest
from fractions import Fraction

from algorithm_lab.polynomial_divmod import polynomial_divmod


class Tests(unittest.TestCase):
    def test_nonmonic_rational_division_and_input_isolation(self):
        divisor = [Fraction(1, 2), Fraction(-2, 3), 0]
        dividend = [Fraction(7, 10), Fraction(-1, 8), Fraction(-1, 2), 0, 0]
        before = (dividend[:], divisor[:])
        quotient, remainder = polynomial_divmod(iter(dividend), iter(divisor))
        self.assertEqual(quotient, [Fraction(3, 4), Fraction(3, 4)])
        self.assertEqual(remainder, [Fraction(13, 40)])
        self.assertTrue(all(type(v) is Fraction for v in quotient + remainder))
        polynomial_divmod(dividend, divisor)
        self.assertEqual((dividend, divisor), before)
        quotient[0] = 999
        remainder[0] = 999
        self.assertEqual((dividend, divisor), before)

    def test_lower_degree_and_zero_dividends_are_canonical(self):
        self.assertEqual(polynomial_divmod([2, 0, 0], [1, 0, 3, 0]), ([], [Fraction(2)]))
        self.assertEqual(polynomial_divmod([0, 0], [Fraction(1, 3), 0]), ([], []))

    def test_division_identity(self):
        rng = random.Random(213)
        for _ in range(100):
            a = [rng.randrange(-5, 6) for _ in range(rng.randrange(10))]
            b = [rng.randrange(-5, 6) for _ in range(rng.randrange(5))] + [2]
            q, r = polynomial_divmod(a, b)
            self.assertLess(len(r), len(b))
            for x in range(-4, 5):

                def evaluate(values, x=x):
                    return sum(c * x**i for i, c in enumerate(values))

                self.assertEqual(evaluate(a), evaluate(q) * evaluate(b) + evaluate(r))
        self.assertEqual(polynomial_divmod([1], [2]), ([Fraction(1, 2)], []))

    def test_invalid(self):
        for a, b in [([1], []), ([1], [0, 0]), ([True], [1]), ([1.0], [1])]:
            with self.assertRaises(ValueError):
                polynomial_divmod(a, b)
