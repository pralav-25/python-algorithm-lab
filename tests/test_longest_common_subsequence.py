import itertools
import random
import unittest

from algorithm_lab.longest_common_subsequence import longest_common_subsequence as lcs


def is_subsequence(candidate, text):
    remaining = iter(text)
    return all(any(char == other for other in remaining) for char in candidate)


class LCSTests(unittest.TestCase):
    def test_subsequence_enumeration_oracle(self):
        rng = random.Random(47)
        for _ in range(70):
            a = "".join(rng.choices("abc", k=rng.randrange(8)))
            b = "".join(rng.choices("abc", k=rng.randrange(8)))
            best = max(
                (
                    n
                    for n in range(len(a) + 1)
                    for candidate in itertools.combinations(a, n)
                    if is_subsequence(candidate, b)
                ),
                default=0,
            )
            result = lcs(a, b)
            self.assertEqual(len(result), best)
            self.assertTrue(is_subsequence(result, a) and is_subsequence(result, b))

    def test_empty_and_unicode(self):
        self.assertEqual(lcs("", "abc"), "")
        self.assertEqual(lcs("🙂é🙂", "é🙂"), "é🙂")
