import unittest
from itertools import product

from algorithm_lab.longest_bitonic_subsequence import longest_bitonic_subsequence


def bitonic(values):
    return not values or any(
        all(values[i] < values[i + 1] for i in range(peak))
        and all(values[i] > values[i + 1] for i in range(peak, len(values) - 1))
        for peak in range(len(values))
    )


class Tests(unittest.TestCase):
    def test_subsequence_enumeration(self):
        for n in range(6):
            for values in product(range(3), repeat=n):
                subs = [
                    tuple(v for i, v in enumerate(values) if mask >> i & 1)
                    for mask in range(1 << n)
                ]
                actual = tuple(longest_bitonic_subsequence(values))
                self.assertIn(actual, subs)
                self.assertTrue(bitonic(actual))
                self.assertEqual(len(actual), max(len(s) for s in subs if bitonic(s)))

    def test_invalid(self):
        with self.assertRaises(ValueError):
            longest_bitonic_subsequence([True])
