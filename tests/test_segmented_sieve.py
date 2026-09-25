import math
import unittest

from algorithm_lab.segmented_sieve import segmented_sieve


class Tests(unittest.TestCase):
    def test_all_small_intervals(self):
        for start in range(30):
            for stop in range(start, 60):
                expected = [
                    n
                    for n in range(max(2, start), stop)
                    if all(n % d for d in range(2, math.isqrt(n) + 1))
                ]
                self.assertEqual(segmented_sieve(start, stop), expected)
        self.assertEqual(segmented_sieve(49, 50), [])

    def test_invalid(self):
        for args in [(-1, 3), (4, 3), (True, 3), (1, 3.5)]:
            with self.assertRaises(ValueError):
                segmented_sieve(*args)
