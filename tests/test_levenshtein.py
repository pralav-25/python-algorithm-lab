import functools
import random
import unittest

from algorithm_lab.levenshtein import levenshtein


@functools.cache
def oracle(a, b):
    if not a or not b:
        return len(a) + len(b)
    return min(1 + oracle(a[1:], b), 1 + oracle(a, b[1:]), (a[0] != b[0]) + oracle(a[1:], b[1:]))


class LevenshteinTests(unittest.TestCase):
    def test_recursive_oracle_and_symmetry(self):
        rng = random.Random(3)
        for _ in range(100):
            a = "".join(rng.choices("abé", k=rng.randrange(7)))
            b = "".join(rng.choices("abé", k=rng.randrange(7)))
            self.assertEqual(levenshtein(a, b), oracle(a, b))
            self.assertEqual(levenshtein(a, b), levenshtein(b, a))

    def test_known_cases(self):
        self.assertEqual(levenshtein("kitten", "sitting"), 3)
        self.assertEqual(levenshtein("ab", "ba"), 2)
        self.assertEqual(levenshtein("", "🙂"), 1)
