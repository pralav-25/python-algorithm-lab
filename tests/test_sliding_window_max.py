import random
import unittest

from algorithm_lab.sliding_window_max import sliding_window_max


class SlidingWindowTests(unittest.TestCase):
    def test_all_windows_against_slices(self):
        rng = random.Random(6)
        for size in range(1, 45):
            values = [rng.randrange(-20, 21) for _ in range(size)]
            for width in range(1, size + 1):
                expected = [max(values[i : i + width]) for i in range(size - width + 1)]
                self.assertEqual(sliding_window_max(values, width), expected)

    def test_invalid_windows(self):
        for values, width in [([], 1), ([1], 0), ([1], 2), ([1], True), ([1], 0.5)]:
            with self.assertRaises(ValueError):
                sliding_window_max(values, width)
