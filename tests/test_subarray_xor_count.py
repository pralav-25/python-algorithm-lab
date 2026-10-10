import itertools
import unittest
from functools import reduce
from operator import xor

from algorithm_lab.subarray_xor_count import subarray_xor_count


class SubarrayXorTests(unittest.TestCase):
    def test_all_subarray_oracle(self):
        for n in range(6):
            for data in itertools.product(range(3), repeat=n):
                for target in range(4):
                    expected = sum(
                        reduce(xor, data[i:j], 0) == target
                        for i in range(n)
                        for j in range(i + 1, n + 1)
                    )
                    self.assertEqual(subarray_xor_count(iter(data), target), expected)

    def test_no_mutation_large_bits_and_validation(self):
        data = [2**100, 0, 2**100]
        original = data[:]
        self.assertEqual(subarray_xor_count(data, 0), 2)
        self.assertEqual(data, original)
        for bad in [-1, True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                subarray_xor_count([bad], 0)
            with self.assertRaises(ValueError):
                subarray_xor_count([], bad)
