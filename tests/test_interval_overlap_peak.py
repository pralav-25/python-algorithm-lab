import random
import unittest

from algorithm_lab.interval_overlap_peak import interval_overlap_peak


class Tests(unittest.TestCase):
    def test_integer_grid_oracle(self):
        rng = random.Random(246)
        for _ in range(150):
            intervals = []
            for _ in range(rng.randrange(12)):
                start = rng.randrange(-5, 6)
                intervals.append((start, start + rng.randrange(1, 6)))
            counts = [(sum(a <= x < b for a, b in intervals), x) for x in range(-5, 11)]
            best = max(count for count, _ in counts)
            expected = (
                (best, next(x for count, x in counts if count == best)) if best else (0, None)
            )
            self.assertEqual(interval_overlap_peak(intervals), expected)

    def test_invalid(self):
        for intervals in [[(1, 1)], [(2, 1)], [(False, 2)]]:
            with self.assertRaises(ValueError):
                interval_overlap_peak(intervals)
