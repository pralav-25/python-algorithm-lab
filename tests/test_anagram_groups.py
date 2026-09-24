import random
import unittest
from collections import Counter

from algorithm_lab.anagram_groups import anagram_groups


class AnagramTests(unittest.TestCase):
    def test_counter_oracle(self):
        rng = random.Random(137)
        words = ["".join(rng.choice("ab🙂") for _ in range(rng.randrange(8))) for _ in range(200)]
        expected = []
        for word in words:
            for group in expected:
                if Counter(word) == Counter(group[0]):
                    group.append(word)
                    break
            else:
                expected.append([word])
        self.assertEqual(anagram_groups(iter(words)), expected)
        self.assertEqual(anagram_groups(["", "", "A", "a"]), [["", ""], ["A"], ["a"]])
        with self.assertRaises(ValueError):
            anagram_groups([1])
