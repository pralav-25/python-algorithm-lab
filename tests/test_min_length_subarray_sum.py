import itertools
import unittest

from algorithm_lab.min_length_subarray_sum import min_length_subarray_sum


class MinLengthSumTests(unittest.TestCase):
    def test_all_intervals_oracle(self):
        for n in range(6):
            for data in itertools.product((0, 1, 3), repeat=n):
                for target in range(1, 7):
                    candidates = [
                        (i, j)
                        for i in range(n)
                        for j in range(i + 1, n + 1)
                        if sum(data[i:j]) >= target
                    ]
                    expected = min(
                        candidates, key=lambda span: (span[1] - span[0], span[0]), default=None
                    )
                    self.assertEqual(min_length_subarray_sum(data, target), expected)

    def test_zeroes_ties_no_mutation_and_validation(self):
        data = [0, 4, 0, 4, 0]
        self.assertEqual(min_length_subarray_sum(data, 4), (1, 2))
        self.assertEqual(data, [0, 4, 0, 4, 0])
        for bad in [-1, True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                min_length_subarray_sum([bad], 1)
        for bad in [0, -1, True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                min_length_subarray_sum([], bad)
