import random
import unittest

from algorithm_lab.segment_tree import SegmentTree


class SegmentTests(unittest.TestCase):
    def test_queries_and_replacements(self):
        rng = random.Random(111)
        for n in range(30):
            data = [rng.randrange(-9, 10) for _ in range(n)]
            tree = SegmentTree(data)
            for _ in range(40):
                if n:
                    i, value = rng.randrange(n), rng.randrange(-9, 10)
                    tree.set(i, value)
                    data[i] = value
                a, b = sorted((rng.randrange(n + 1), rng.randrange(n + 1)))
                self.assertEqual(tree.range_sum(a, b), sum(data[a:b]))

    def test_invalid(self):
        tree = SegmentTree([1])
        for i, value in [(-1, 2), (1, 2), (True, 2), (0, False)]:
            with self.assertRaises(ValueError):
                tree.set(i, value)
        for a, b in [(1, 0), (0, 2), (0.0, 1)]:
            with self.assertRaises(ValueError):
                tree.range_sum(a, b)
        self.assertEqual(tree.range_sum(0, 1), 1)
