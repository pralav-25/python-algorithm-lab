import math
import random
import unittest

from algorithm_lab.integer_sqrt import integer_sqrt


class IntegerSqrtTests(unittest.TestCase):
    def test_builtin_isqrt_and_large_boundaries(self):
        for value in range(5000):
            self.assertEqual(integer_sqrt(value), math.isqrt(value))
        rng = random.Random(27)
        for bits in [64, 128, 512, 2048, 4096]:
            root = rng.getrandbits(bits) + 1
            for value in [root * root - 1, root * root, root * root + 1]:
                result = integer_sqrt(value)
                self.assertEqual(result, math.isqrt(value))
                self.assertTrue(result * result <= value < (result + 1) ** 2)

    def test_invalid_inputs(self):
        for value in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                integer_sqrt(value)
