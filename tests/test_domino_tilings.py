import unittest

from algorithm_lab.domino_tilings import domino_tilings


class Tests(unittest.TestCase):
    @staticmethod
    def board_oracle(width):
        cells = frozenset((row, column) for row in range(2) for column in range(width))

        def place(remaining):
            if not remaining:
                return 1
            row, column = min(remaining)
            total = 0
            for other in [(row + 1, column), (row, column + 1)]:
                if other in remaining:
                    total += place(remaining - {(row, column), other})
            return total

        return place(cells)

    def test_exact_cover_enumeration(self):
        for width in range(10):
            self.assertEqual(domino_tilings(width), self.board_oracle(width))
        self.assertEqual(domino_tilings(20), 10946)

    def test_invalid(self):
        for value in [-1, True, False, 2.0, None, "2"]:
            with self.assertRaises(ValueError):
                domino_tilings(value)
