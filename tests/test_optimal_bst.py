import itertools
import unittest
from functools import lru_cache

from algorithm_lab.optimal_bst import optimal_bst


class Tests(unittest.TestCase):
    def test_enumerate_ordered_tree_depths(self):
        @lru_cache(None)
        def trees(size):
            if not size:
                return [()]
            return [
                tuple(depth + 1 for depth in left) + (1,) + tuple(depth + 1 for depth in right)
                for left_size in range(size)
                for left in trees(left_size)
                for right in trees(size - left_size - 1)
            ]

        for size in range(6):
            for frequencies in itertools.product([0, 1, 3], repeat=size):
                expected = min(
                    sum(f * depth for f, depth in zip(frequencies, depths, strict=True))
                    for depths in trees(size)
                )
                values = list(frequencies)
                self.assertEqual(optimal_bst(iter(values)), expected)
                self.assertEqual(values, list(frequencies))
        self.assertEqual(optimal_bst([34, 8, 50]), 142)

    def test_invalid(self):
        for values in [[True], [-1], [1.5], [1, None]]:
            with self.assertRaises(ValueError):
                optimal_bst(values)
