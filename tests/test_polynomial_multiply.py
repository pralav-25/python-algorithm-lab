import random
import unittest

from algorithm_lab.polynomial_multiply import polynomial_multiply


class Tests(unittest.TestCase):
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
