import random
import unittest

from algorithm_lab.longest_common_substring import longest_common_substring as common


class CommonSubstringTests(unittest.TestCase):
    def test_all_substrings_oracle(self):
        rng = random.Random(39)
        for _ in range(200):
            a = "".join(rng.choices("abc🙂", k=rng.randrange(10)))
            b = "".join(rng.choices("abc🙂", k=rng.randrange(10)))
            options = [
                a[i:j] for i in range(len(a) + 1) for j in range(i, len(a) + 1) if a[i:j] in b
            ]
            self.assertEqual(common(a, b), max(options, key=len))

    def test_ties_are_resolved_in_first_string(self):
        self.assertEqual(common("abxcd", "cdxab"), "ab")
        self.assertEqual(common("", "abc"), "")
        self.assertEqual(common("ab", "xy"), "")
