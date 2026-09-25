import unittest

from algorithm_lab.interval_intersection import interval_intersection


class Tests(unittest.TestCase):
    def test_pairwise_oracle(self):
        lists = [[], [(0, 0)], [(0, 2), (5, 8)], [(2, 6)], [(-5, -1), (1, 3), (7, 10)]]
        for a in lists:
            for b in lists:
                expected = sorted(
                    (max(x, u), min(y, v)) for x, y in a for u, v in b if max(x, u) <= min(y, v)
                )
                self.assertEqual(interval_intersection(a, b), expected)

    def test_invalid(self):
        for values in [[(2, 1)], [(0, 2), (2, 3)], [(2, 3), (0, 1)], [(False, 1)]]:
            with self.assertRaises(ValueError):
                interval_intersection(values, [])
