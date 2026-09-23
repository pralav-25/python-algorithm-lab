import random
import unittest

from algorithm_lab.inversion_count import inversion_count


class InversionTests(unittest.TestCase):
    def test_quadratic_oracle(self):
        rng = random.Random(9)
        for size in range(100):
            data = [rng.randrange(-10, 11) for _ in range(size)]
            before = data[:]
            expected = sum(data[i] > data[j] for i in range(size) for j in range(i + 1, size))
            self.assertEqual(inversion_count(data), expected)
            self.assertEqual(data, before)

    def test_extremes(self):
        self.assertEqual(inversion_count([1] * 20), 0)
        self.assertEqual(inversion_count(range(100, 0, -1)), 100 * 99 // 2)
