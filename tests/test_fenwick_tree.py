import random
import unittest

from algorithm_lab.fenwick_tree import FenwickTree


class FenwickTests(unittest.TestCase):
    def test_updates_against_list(self):
        rng = random.Random(110)
        for n in range(25):
            data = [rng.randrange(-50, 51) for _ in range(n)]
            tree = FenwickTree(iter(data))
            for _ in range(40):
                if n:
                    i, delta = rng.randrange(n), rng.randrange(-20, 21)
                    tree.add(i, delta)
                    data[i] += delta
                a, b = sorted((rng.randrange(n + 1), rng.randrange(n + 1)))
                self.assertEqual(tree.range_sum(a, b), sum(data[a:b]))
            self.assertEqual(tree.prefix_sum(n), sum(data))

    def test_validation_is_atomic(self):
        tree = FenwickTree([3, 4])
        for i, delta in [(True, 1), (-1, 1), (2, 1), (0, 1.5)]:
            with self.assertRaises(ValueError):
                tree.add(i, delta)
        for a, b in [(1, 0), (0, 3), (-1, 0), (False, 1)]:
            with self.assertRaises(ValueError):
                tree.range_sum(a, b)
        self.assertEqual(tree.range_sum(0, 2), 7)
        with self.assertRaises(ValueError):
            FenwickTree([True])
