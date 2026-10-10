import unittest

from algorithm_lab.jacobi_symbol import jacobi_symbol


def factor_and_count_residues(value, modulus):
    result = 1
    prime = 3
    while modulus > 1:
        if modulus % prime:
            prime += 2
            continue
        residue = value % prime
        squares = {number * number % prime for number in range(1, prime)}
        term = 0 if residue == 0 else (1 if residue in squares else -1)
        while modulus % prime == 0:
            modulus //= prime
            result *= term
        prime += 2
    return result


class Tests(unittest.TestCase):
    def test_factor_and_residue_oracle(self):
        for modulus in range(1, 100, 2):
            for value in range(-100, 101):
                self.assertEqual(
                    jacobi_symbol(value, modulus), factor_and_count_residues(value, modulus)
                )

    def test_composite_caveat(self):
        self.assertEqual(jacobi_symbol(2, 9), 1)
        self.assertNotIn(2, {value * value % 9 for value in range(9)})

    def test_invalid(self):
        for args in ((True, 3), (1.5, 3), (1, 0), (1, -3), (1, 2), (1, True), (1, 3.5)):
            with self.assertRaises(ValueError):
                jacobi_symbol(*args)
