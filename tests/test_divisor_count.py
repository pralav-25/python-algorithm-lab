import unittest

from algorithm_lab.divisor_count import divisor_count


class Tests(unittest.TestCase):
    def test_divisor_enumeration(self):
        for n in range(1, 700):
            self.assertEqual(divisor_count(n), sum(n % divisor == 0 for divisor in range(1, n + 1)))

    def test_invalid(self):
        for n in (0, -1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                divisor_count(n)
