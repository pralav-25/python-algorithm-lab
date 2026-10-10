import itertools
import unittest

from algorithm_lab.digit_sum import digit_sum


class Tests(unittest.TestCase):
    def test_positional_digit_oracle(self):
        for base in range(2, 9):
            for digits in itertools.product(range(base), repeat=3):
                value = sum(digit * base**place for place, digit in enumerate(digits))
                self.assertEqual(digit_sum(value, base), sum(digits))
                self.assertEqual(digit_sum(-value, base), sum(digits))

    def test_decimal_and_large_base(self):
        for value in range(-500, 501):
            self.assertEqual(digit_sum(value), sum(map(int, str(abs(value)))))
        self.assertEqual(digit_sum(12, 100), 12)

    def test_invalid(self):
        for args in ((True,), (1.5,), (None,), (2, 1), (2, True), (2, 2.5)):
            with self.assertRaises(ValueError):
                digit_sum(*args)
