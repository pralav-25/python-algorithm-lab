import unittest

from algorithm_lab.digital_root import digital_root


def repeated_sum(value, base):
    value = abs(value)
    while value >= base:
        digits = []
        while value:
            digits.append(value % base)
            value //= base
        value = sum(digits)
    return value


class Tests(unittest.TestCase):
    def test_repeated_digit_sum_oracle(self):
        for base in range(2, 18):
            for value in range(-500, 501):
                self.assertEqual(digital_root(value, base), repeated_sum(value, base))

    def test_large_integer_and_default(self):
        value = 10**200 - 1
        self.assertEqual(digital_root(value), 9)
        self.assertEqual(digital_root(123), 6)

    def test_invalid(self):
        for args in ((True,), (1.5,), (None,), (2, 1), (2, True), (2, 2.5)):
            with self.assertRaises(ValueError):
                digital_root(*args)
