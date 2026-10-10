import itertools
import unittest

from algorithm_lab.minimum_partition_difference import minimum_partition_difference


class Tests(unittest.TestCase):
    def test_all_subsets(self):
        for size in range(7):
            for values in itertools.product([0, 1, 3], repeat=size):
                expected = min(
                    abs(
                        sum(values)
                        - 2 * sum(value for i, value in enumerate(values) if mask >> i & 1)
                    )
                    for mask in range(1 << size)
                )
                original = list(values)
                self.assertEqual(minimum_partition_difference(iter(original)), expected)
                self.assertEqual(original, list(values))
        self.assertEqual(minimum_partition_difference([100, 1, 1]), 98)

    def test_invalid(self):
        for values in [[True], [-1], [1.0], [1, None]]:
            with self.assertRaises(ValueError):
                minimum_partition_difference(values)
