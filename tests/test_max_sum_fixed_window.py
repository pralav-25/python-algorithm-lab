import itertools
import unittest

from algorithm_lab.max_sum_fixed_window import max_sum_fixed_window


class FixedWindowTests(unittest.TestCase):
    def test_independent_window_sums(self):
        for n in range(1, 7):
            for data in itertools.product((-2, 0, 3), repeat=n):
                for size in range(1, n + 1):
                    candidates = [(sum(data[i : i + size]), i) for i in range(n - size + 1)]
                    expected = min(candidates, key=lambda pair: (-pair[0], pair[1]))
                    self.assertEqual(max_sum_fixed_window(data, size), expected)

    def test_validation_and_no_mutation(self):
        data = [-1, -1, -1]
        self.assertEqual(max_sum_fixed_window(data, 2), (-2, 0))
        self.assertEqual(data, [-1, -1, -1])
        for bad in [0, -1, 4, True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                max_sum_fixed_window(data, bad)
        with self.assertRaises(ValueError):
            max_sum_fixed_window([], 1)
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                max_sum_fixed_window([bad], 1)
