import itertools
import unittest

from algorithm_lab.distinct_partition_count import distinct_partition_count


class Tests(unittest.TestCase):
    def test_subset_enumeration(self):
        for n in range(13):
            expected = sum(
                sum(subset) == n
                for size in range(n + 1)
                for subset in itertools.combinations(range(1, n + 1), size)
            )
            self.assertEqual(distinct_partition_count(n), expected)

    def test_invalid(self):
        for n in (-1, True, 1.5, "3", None):
            with self.assertRaises(ValueError):
                distinct_partition_count(n)
