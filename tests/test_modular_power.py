import unittest

from algorithm_lab.modular_power import modular_power


class ModularPowerTests(unittest.TestCase):
    def test_builtin_pow_oracle(self):
        for base in range(-12, 13):
            for exponent in range(16):
                for modulus in range(1, 20):
                    self.assertEqual(
                        modular_power(base, exponent, modulus), pow(base, exponent, modulus)
                    )
        self.assertEqual(modular_power(17, 10**50, 1000000007), pow(17, 10**50, 1000000007))

    def test_zero_and_invalid_arguments(self):
        self.assertEqual(modular_power(0, 0, 7), 1)
        self.assertEqual(modular_power(2, 0, 1), 0)
        for args in [(2, -1, 3), (2, 3, 0), (2, True, 3), (2.5, 2, 3)]:
            with self.assertRaises(ValueError):
                modular_power(*args)
