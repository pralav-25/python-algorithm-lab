import itertools
import unittest

from algorithm_lab.narayana_number import narayana_number


class Tests(unittest.TestCase):
    def test_dyck_path_enumeration(self):
        for n in range(7):
            counts = [0] * (n + 2)
            for path in itertools.product((1, -1), repeat=2 * n):
                heights = list(itertools.accumulate(path, initial=0))
                if heights[-1] != 0 or min(heights) < 0:
                    continue
                peaks = sum(pair == (1, -1) for pair in itertools.pairwise(path))
                counts[peaks] += 1
            for k, expected in enumerate(counts):
                self.assertEqual(narayana_number(n, k), expected)

    def test_invalid(self):
        for args in ((-1, 0), (0, -1), (True, 0), (1, True), (1.5, 0), (1, None)):
            with self.assertRaises(ValueError):
                narayana_number(*args)
