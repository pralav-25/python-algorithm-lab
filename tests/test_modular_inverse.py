import unittest

from algorithm_lab.modular_inverse import modular_inverse


class Tests(unittest.TestCase):
    def test_exhaustive_oracle(self):
        for modulus in range(2, 40):
            for value in range(-40, 40):
                candidates = [x for x in range(modulus) if value * x % modulus == 1]
                if candidates:
                    self.assertEqual(modular_inverse(value, modulus), candidates[0])
                else:
                    with self.assertRaises(ValueError):
                        modular_inverse(value, modulus)

    def test_invalid(self):
        for args in [(True, 3), (2, 1), (2, 3.0)]:
            with self.assertRaises(ValueError):
                modular_inverse(*args)
