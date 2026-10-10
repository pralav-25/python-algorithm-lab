import itertools
import unittest

from algorithm_lab.house_robber import house_robber


class Tests(unittest.TestCase):
    def test_all_independent_subsets(self):
        for size in range(6):
            for values in itertools.product([0, 1, 3], repeat=size):
                expected = max(
                    sum(value for i, value in enumerate(values) if mask >> i & 1)
                    for mask in range(1 << size)
                    if not mask & (mask << 1)
                )
                original = list(values)
                self.assertEqual(house_robber(iter(original)), expected)
                self.assertEqual(original, list(values))

    def test_invalid(self):
        for values in [[True], [-1], [1.0], [1, None]]:
            with self.assertRaises(ValueError):
                house_robber(values)
