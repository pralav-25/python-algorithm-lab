import itertools
import random
import unittest

from algorithm_lab.interval_scheduling import interval_scheduling


class IntervalSchedulingTests(unittest.TestCase):
    def test_optimal_cardinality_against_subsets(self):
        rng = random.Random(45)
        for _ in range(50):
            rows = [(start := rng.randrange(-5, 8), start + rng.randrange(1, 6)) for _ in range(8)]
            best = 0
            for count in range(9):
                for group in itertools.combinations(rows, count):
                    ordered = sorted(group)
                    if all(a[1] <= b[0] for a, b in itertools.pairwise(ordered)):
                        best = max(best, count)
            selected = interval_scheduling(rows)
            self.assertEqual(len(selected), best)
            self.assertTrue(all(a[1] <= b[0] for a, b in itertools.pairwise(selected)))

    def test_invalid_and_empty(self):
        self.assertEqual(interval_scheduling([]), [])
        for row in [(1, 1), (2, 1), (False, 2), (1.2, 2)]:
            with self.assertRaises(ValueError):
                interval_scheduling([row])
