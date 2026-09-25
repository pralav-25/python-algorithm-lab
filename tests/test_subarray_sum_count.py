import unittest
from itertools import product

from algorithm_lab.subarray_sum_count import subarray_sum_count


class Tests(unittest.TestCase):
    def test_all_slices_oracle(self):
        for n in range(6):
            for values in product([-1, 0, 1], repeat=n):
                for target in range(-2, 3):
                    expected = sum(
                        sum(values[i:j]) == target for i in range(n) for j in range(i + 1, n + 1)
                    )
                    self.assertEqual(subarray_sum_count(values, target), expected)

    def test_invalid(self):
        for values, target in [([True], 0), ([1.5], 0), ([], True)]:
            with self.assertRaises(ValueError):
                subarray_sum_count(values, target)
