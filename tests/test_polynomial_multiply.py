import random
import unittest
from math import comb

from algorithm_lab.polynomial_multiply import polynomial_multiply


class Tests(unittest.TestCase):
    def test_binomial_coefficients_with_alternating_signs(self):
        # (1-x)**n * (1+x)**n = (1-x*x)**n.
        n = 40
        left = [(-1) ** i * comb(n, i) for i in range(n + 1)]
        right = [comb(n, i) for i in range(n + 1)]
        before = (left[:], right[:])
        expected = [0] * (2 * n + 1)
        for i in range(n + 1):
            expected[2 * i] = (-1) ** i * comb(n, i)
        self.assertEqual(polynomial_multiply(iter(left), iter(right)), expected)
        self.assertEqual(polynomial_multiply(left, right), expected)
        self.assertEqual((left, right), before)
        self.assertEqual(polynomial_multiply([0, 0], right), [])
        self.assertEqual(polynomial_multiply([1, 0, 0], [2, 3, 0]), [2, 3])

    def test_evaluation_identity(self):
        rng = random.Random(212)
        for _ in range(80):
            a = [rng.randrange(-4, 5) for _ in range(rng.randrange(8))]
            b = [rng.randrange(-4, 5) for _ in range(rng.randrange(8))]
            result = polynomial_multiply(a, b)
            for x in range(-4, 5):

                def evaluate(values, x=x):
                    return sum(c * x**i for i, c in enumerate(values))

                self.assertEqual(evaluate(result), evaluate(a) * evaluate(b))
            self.assertTrue(not result or result[-1] != 0)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            polynomial_multiply([], [True])
