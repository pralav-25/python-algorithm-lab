import unittest

from algorithm_lab.integer_nth_root import integer_nth_root


class Tests(unittest.TestCase):
    def test_bracketing(self):
        for degree in range(1, 12):
            for value in [*range(100), 10**300 - 1, 10**300, 10**300 + 1]:
                root = integer_nth_root(value, degree)
                self.assertLessEqual(root**degree, value)
                self.assertGreater((root + 1) ** degree, value)
        self.assertEqual(integer_nth_root(2, 10**20), 1)

    def test_invalid(self):
        for args in [(-1, 2), (1, 0), (True, 2), (1, 2.0)]:
            with self.assertRaises(ValueError):
                integer_nth_root(*args)
