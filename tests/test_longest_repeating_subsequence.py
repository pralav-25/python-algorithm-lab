import itertools
import unittest

from algorithm_lab.longest_repeating_subsequence import longest_repeating_subsequence


class Tests(unittest.TestCase):
    def test_subsequence_pair_enumeration(self):
        for size in range(6):
            for chars in itertools.product("ab", repeat=size):
                text = "".join(chars)
                expected = 0
                for length in range(1, size + 1):
                    indices = list(itertools.combinations(range(size), length))
                    for first, second in itertools.product(indices, repeat=2):
                        if all(
                            i != j and text[i] == text[j]
                            for i, j in zip(first, second, strict=True)
                        ):
                            expected = length
                self.assertEqual(longest_repeating_subsequence(text), expected)
        self.assertEqual(longest_repeating_subsequence("🙂a🙂a"), 2)

    def test_invalid(self):
        for value in [None, [], b"a", True]:
            with self.assertRaises(ValueError):
                longest_repeating_subsequence(value)
