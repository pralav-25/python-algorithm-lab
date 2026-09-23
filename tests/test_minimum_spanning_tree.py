import itertools
import math
import random
import unittest

from algorithm_lab.minimum_spanning_tree import minimum_spanning_tree


def connected(size, edges):
    seen = {0}
    while True:
        expanded = (
            seen | {b for a, b, _ in edges if a in seen} | {a for a, b, _ in edges if b in seen}
        )
        if expanded == seen:
            return len(seen) == size
        seen = expanded


class MSTTests(unittest.TestCase):
    def test_brute_force_spanning_trees(self):
        rng = random.Random(12)
        for _ in range(35):
            edges = [(a, b, rng.randrange(-5, 9)) for a in range(4) for b in range(a + 1, 4)]
            expected = min(
                sum(w for _, _, w in group)
                for group in itertools.combinations(edges, 3)
                if connected(4, group)
            )
            total, tree = minimum_spanning_tree(4, edges)
            self.assertEqual(total, expected)
            self.assertTrue(connected(4, tree))
            self.assertEqual(len(tree), 3)

    def test_disconnected_parallel_and_invalid_edges(self):
        with self.assertRaises(ValueError):
            minimum_spanning_tree(3, [(0, 1, 2)])
        self.assertEqual(
            minimum_spanning_tree(3, [(0, 1, 2)], require_connected=False), (2, [(0, 1, 2)])
        )
        self.assertEqual(
            minimum_spanning_tree(2, [(0, 0, -10), (0, 1, 4), (0, 1, 1)]), (1, [(0, 1, 1)])
        )
        self.assertEqual(minimum_spanning_tree(0, []), (0, []))
        for edges in [[(0, 2, 1)], [(0, 1, math.nan)], [(True, 1, 2)]]:
            with self.assertRaises(ValueError):
                minimum_spanning_tree(2, edges)
