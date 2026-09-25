import random
import unittest

from algorithm_lab.sliding_window_min import sliding_window_min


class Tests(unittest.TestCase):
    def test_window_oracle(self):
        rng = random.Random(239)
        for n in range(1, 50):
            values = [rng.randrange(-5, 6) for _ in range(n)]
            for width in range(1, n + 1):
                self.assertEqual(
                    sliding_window_min(values, width),
                    [min(values[i : i + width]) for i in range(n - width + 1)],
                )

    def test_invalid(self):
        for values, width in [([], 1), ([1], 0), ([1], 2), ([1], True)]:
            with self.assertRaises(ValueError):
                sliding_window_min(values, width)
