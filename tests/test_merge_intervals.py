import random
import unittest

from algorithm_lab.merge_intervals import merge_intervals


class MergeIntervalsTests(unittest.TestCase):
    def test_containment_touching_and_gaps(self):
        self.assertEqual(merge_intervals([(1, 9), (3, 4), (9, 10), (12, 12)]), [(1, 10), (12, 12)])
        self.assertEqual(merge_intervals([]), [])

    def test_coverage_at_half_integer_points(self):
        rng = random.Random(21)
        for _ in range(100):
            rows = [
                tuple(sorted((rng.randrange(-10, 11), rng.randrange(-10, 11)))) for _ in range(10)
            ]
            merged = merge_intervals(rows)
            for half in range(-21, 22):
                point = half / 2
                self.assertEqual(
                    any(a <= point <= b for a, b in rows), any(a <= point <= b for a, b in merged)
                )
            self.assertTrue(all(a[1] < b[0] for a, b in zip(merged, merged[1:], strict=False)))

    def test_invalid_bounds(self):
        for rows in [[(3, 2)], [(True, 2)], [(1.5, 2)]]:
            with self.assertRaises(ValueError):
                merge_intervals(rows)
