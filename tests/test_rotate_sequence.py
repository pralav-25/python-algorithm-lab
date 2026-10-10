import unittest

from algorithm_lab.rotate_sequence import rotate_sequence


class RotationTests(unittest.TestCase):
    def test_modular_destination_oracle(self):
        for n in range(12):
            data = list(range(n))
            for steps in range(-30, 31):
                expected = [None] * n
                for i, value in enumerate(data):
                    expected[(i + steps) % n] = value
                self.assertEqual(rotate_sequence(iter(data), steps), expected)
                self.assertEqual(data, list(range(n)))

    def test_identity_objects_and_validation(self):
        values = [object(), object(), object()]
        result = rotate_sequence(values, 10**100)
        self.assertEqual(result, [values[2], values[0], values[1]])
        self.assertIsNot(result, values)
        self.assertEqual(rotate_sequence([], -8), [])
        for bad in [True, 1.2, "2"]:
            with self.assertRaises(ValueError):
                rotate_sequence([], bad)
