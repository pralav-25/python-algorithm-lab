import unittest

from algorithm_lab.prefix_sum import PrefixSum


class PrefixSumTests(unittest.TestCase):
    def test_every_slice_and_independent_storage(self):
        values = [4, -6, 2, 8, -3]
        prefix = PrefixSum(values)
        for start in range(len(values) + 1):
            for stop in range(start, len(values) + 1):
                self.assertEqual(prefix.sum(start, stop), sum(values[start:stop]))
        values[0] = 999
        self.assertEqual(prefix.sum(0, 1), 4)
        self.assertEqual(len(prefix), 5)
        self.assertEqual(PrefixSum([]).sum(0, 0), 0)

    def test_invalid_bounds(self):
        prefix = PrefixSum([1, 2])
        for start, stop in [(-1, 1), (2, 1), (0, 3), (True, 1), (0, 1.5)]:
            with self.assertRaises(ValueError):
                prefix.sum(start, stop)
        with self.assertRaises(ValueError):
            PrefixSum([1.2])
