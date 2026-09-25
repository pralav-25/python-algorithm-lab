import random
import unittest
from fractions import Fraction

from algorithm_lab.polynomial_divmod import polynomial_divmod


class Tests(unittest.TestCase):
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
