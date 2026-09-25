import unittest

from algorithm_lab.divisor_sieve import divisor_sieve


class Tests(unittest.TestCase):
    def test_trial_division_oracle(self):
        result = divisor_sieve(200)
        for n in range(1, 201):
            self.assertEqual(result[n], [d for d in range(1, n + 1) if n % d == 0])
        self.assertEqual(divisor_sieve(0), [[]])
        result[1].append(99)
        self.assertNotIn(99, result[2])

    def test_invalid(self):
        for n in [-1, True, "3"]:
            with self.assertRaises(ValueError):
                divisor_sieve(n)
