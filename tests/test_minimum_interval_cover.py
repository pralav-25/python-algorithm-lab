import random
import unittest
from itertools import combinations

from algorithm_lab.minimum_interval_cover import minimum_interval_cover


def covers(intervals):
    current = 0
    for left, right in sorted(intervals):
        if left > current:
            break
        current = max(current, right)
    return current >= 5


class Tests(unittest.TestCase):
    def test_subset_oracle(self):
        rng = random.Random(245)
        for _ in range(100):
            intervals = []
            for _ in range(7):
                left = rng.randrange(-1, 6)
                intervals.append((left, left + rng.randrange(1, 5)))
            expected = next(
                (k for k in range(8) if any(covers(sub) for sub in combinations(intervals, k))),
                None,
            )
            actual = minimum_interval_cover(intervals, 0, 5)
            self.assertEqual(None if actual is None else len(actual), expected)
            if actual is not None:
                self.assertTrue(covers([intervals[i] for i in actual]))

    def test_invalid(self):
        for intervals, start, stop in [([], 1, 1), ([(1, 1)], 0, 2), ([(True, 2)], 0, 2)]:
            with self.assertRaises(ValueError):
                minimum_interval_cover(intervals, start, stop)
