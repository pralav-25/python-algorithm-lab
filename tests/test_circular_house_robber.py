import itertools
import unittest

from algorithm_lab.circular_house_robber import circular_house_robber


class Tests(unittest.TestCase):
    def test_all_circular_independent_subsets(self):
        for size in range(6):
            for values in itertools.product([0, 1, 3], repeat=size):
                expected = max(
                    sum(value for i, value in enumerate(values) if mask >> i & 1)
                    for mask in range(1 << size)
                    if not mask & (mask << 1)
                    and not (size > 1 and mask & 1 and mask >> (size - 1) & 1)
                )
                original = list(values)
                self.assertEqual(circular_house_robber(iter(original)), expected)
                self.assertEqual(original, list(values))
        self.assertEqual(circular_house_robber([7]), 7)
        self.assertEqual(circular_house_robber([7, 4]), 7)

    def test_invalid(self):
        for values in [[True], [-1], [1.0], [1, None]]:
            with self.assertRaises(ValueError):
                circular_house_robber(values)
