import itertools
import unittest

from algorithm_lab.gray_code import gray_code


class GrayTests(unittest.TestCase):
    def test_reflection_and_hamming_distance(self):
        expected = [0]
        for bits in range(11):
            result = list(gray_code(bits))
            self.assertEqual(result, expected)
            self.assertEqual(set(result), set(range(1 << bits)))
            if bits:
                pairs = zip(result, result[1:] + result[:1], strict=True)
                self.assertTrue(all((a ^ b).bit_count() == 1 for a, b in pairs))
            expected += [value | (1 << bits) for value in reversed(expected)]
        self.assertEqual(list(itertools.islice(gray_code(100), 4)), [0, 1, 3, 2])

    def test_invalid(self):
        for bits in [-1, True, 2.0]:
            with self.assertRaises(ValueError):
                gray_code(bits)
