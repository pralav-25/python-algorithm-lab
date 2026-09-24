import random
import unittest

from algorithm_lab.aho_corasick import AhoCorasick


class AhoTests(unittest.TestCase):
    def test_naive_search_oracle(self):
        rng = random.Random(139)
        for _ in range(200):
            patterns = [
                "".join(rng.choice("ab🙂") for _ in range(rng.randrange(1, 6)))
                for _ in range(rng.randrange(10))
            ]
            text = "".join(rng.choice("ab🙂") for _ in range(30))
            matcher = AhoCorasick(iter(patterns))
            expected = [
                (i, i + len(p), j)
                for j, p in enumerate(patterns)
                for i in range(len(text))
                if text.startswith(p, i)
            ]
            actual = matcher.find_all(text)
            self.assertEqual(sorted(actual), sorted(expected))
            self.assertEqual([stop for _, stop, _ in actual], sorted(stop for _, stop, _ in actual))
            self.assertEqual(matcher.find_all(text), actual)
            self.assertEqual(matcher.find_all(""), [])

    def test_invalid_and_duplicates(self):
        for patterns in [[""], [3], ["a", None]]:
            with self.assertRaises(ValueError):
                AhoCorasick(patterns)
        self.assertEqual(sorted(AhoCorasick(["a", "a"]).find_all("a")), [(0, 1, 0), (0, 1, 1)])
