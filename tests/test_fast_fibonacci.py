import unittest

from algorithm_lab.fast_fibonacci import fast_fibonacci


class FibonacciTests(unittest.TestCase):
    def test_iterative_sequence_oracle(self):
        a, b = 0, 1
        for index in range(1000):
            self.assertEqual(fast_fibonacci(index), a)
            a, b = b, a + b

    def test_cassini_identity_at_large_indices(self):
        for index in [1000, 1001, 10000]:
            self.assertEqual(
                fast_fibonacci(index + 1) * fast_fibonacci(index - 1) - fast_fibonacci(index) ** 2,
                (-1) ** index,
            )
        for index in [-1, True, 2.5]:
            with self.assertRaises(ValueError):
                fast_fibonacci(index)
