import unittest

from algorithm_lab.mobius_sieve import mobius_sieve


class Tests(unittest.TestCase):
    def test_divisor_identity(self):
        values = mobius_sieve(500)
        self.assertEqual(mobius_sieve(0), [0])
        for n in range(1, 501):
            self.assertEqual(sum(values[d] for d in range(1, n + 1) if n % d == 0), int(n == 1))

    def test_invalid(self):
        for n in [-1, True, 2.5]:
            with self.assertRaises(ValueError):
                mobius_sieve(n)
