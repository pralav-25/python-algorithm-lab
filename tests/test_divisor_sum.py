import unittest

from algorithm_lab.divisor_sum import divisor_sum


class Tests(unittest.TestCase):
    def test_divisor_enumeration(self):
        for n in range(1, 700):
            expected = sum(divisor for divisor in range(1, n + 1) if n % divisor == 0)
            self.assertEqual(divisor_sum(n), expected)

    def test_invalid(self):
        for n in (0, -1, True, 2.5, "3", None):
            with self.assertRaises(ValueError):
                divisor_sum(n)
