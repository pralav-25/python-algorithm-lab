import unittest
from fractions import Fraction

from algorithm_lab.stern_brocot_path import stern_brocot_path


class Tests(unittest.TestCase):
    def test_walk_tree(self):
        for n in range(1, 20):
            for d in range(1, 20):
                left, right = (0, 1), (1, 0)
                for direction, count in stern_brocot_path(n, d):
                    for _ in range(count):
                        mid = (left[0] + right[0], left[1] + right[1])
                        if direction == "L":
                            right = mid
                        else:
                            left = mid
                self.assertEqual(Fraction(left[0] + right[0], left[1] + right[1]), Fraction(n, d))
        self.assertEqual(stern_brocot_path(10**100, 1), [("R", 10**100 - 1)])

    def test_invalid(self):
        for args in [(0, 1), (1, -1), (True, 1)]:
            with self.assertRaises(ValueError):
                stern_brocot_path(*args)
