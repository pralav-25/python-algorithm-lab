import itertools
import unittest

from algorithm_lab.multinomial_coefficient import multinomial_coefficient


class Tests(unittest.TestCase):
    def test_distinct_word_enumeration(self):
        for counts in itertools.product(range(3), repeat=3):
            values = tuple(symbol for symbol, count in enumerate(counts) for _ in range(count))
            expected = len(set(itertools.permutations(values)))
            self.assertEqual(multinomial_coefficient(counts), expected)

    def test_empty_generator_and_unchanged(self):
        self.assertEqual(multinomial_coefficient([]), 1)
        values = [2, 1, 0]
        self.assertEqual(multinomial_coefficient(iter(values)), 3)
        self.assertEqual(values, [2, 1, 0])

    def test_invalid(self):
        for counts in ([-1], [True], [1.5], ["2"], [None]):
            with self.assertRaises(ValueError):
                multinomial_coefficient(counts)
