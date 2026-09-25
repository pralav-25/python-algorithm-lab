import unittest
from itertools import product

from algorithm_lab.bounded_compositions import bounded_compositions


class Tests(unittest.TestCase):
    def test_cartesian_oracle(self):
        for bounds in [[], [0], [3], [2, 1, 3], [0, 2, 0, 2]]:
            for total in range(9):
                expected = [p for p in product(*(range(b + 1) for b in bounds)) if sum(p) == total]
                self.assertEqual(list(bounded_compositions(total, bounds)), expected)

    def test_invalid(self):
        for total, bounds in [(-1, []), (1, [-1]), (True, []), (1, [False])]:
            with self.assertRaises(ValueError):
                list(bounded_compositions(total, bounds))
