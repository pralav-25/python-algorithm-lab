import unittest
from itertools import product

from algorithm_lab.circular_max_subarray import circular_max_subarray


class Tests(unittest.TestCase):
    def test_circular_slice_oracle(self):
        for n in range(1, 7):
            for values in product([-2, 0, 3], repeat=n):
                expected = max(
                    sum(values[(start + i) % n] for i in range(length))
                    for start in range(n)
                    for length in range(1, n + 1)
                )
                self.assertEqual(circular_max_subarray(values), expected)

    def test_invalid(self):
        for values in [[], [True], [1.5]]:
            with self.assertRaises(ValueError):
                circular_max_subarray(values)
