import itertools
import unittest

from algorithm_lab.catalan_triangle import catalan_triangle


class Tests(unittest.TestCase):
    def test_ballot_path_enumeration(self):
        for n in range(7):
            expected = []
            for k in range(n + 1):
                count = 0
                for down_positions in itertools.combinations(range(n + k), k):
                    downs = set(down_positions)
                    height = 0
                    for position in range(n + k):
                        height += -1 if position in downs else 1
                        if height < 0:
                            break
                    else:
                        count += 1
                expected.append(count)
            self.assertEqual(catalan_triangle(n), expected)

    def test_fresh_result_and_invalid(self):
        row = catalan_triangle(3)
        row[0] = 999
        self.assertEqual(catalan_triangle(3), [1, 3, 5, 5])
        for n in (-1, True, 1.5, "3", None):
            with self.assertRaises(ValueError):
                catalan_triangle(n)
