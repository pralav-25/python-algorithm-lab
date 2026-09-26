import itertools
import unittest

from algorithm_lab.word_break import word_break


class Tests(unittest.TestCase):
    def test_all_partitions_oracle(self):
        words = {"a", "ab", "ba", "bb", "aba"}
        for n in range(8):
            for letters in itertools.product("ab", repeat=n):
                text = "".join(letters)
                partitions = []
                for mask in range(1 << max(0, n - 1)):
                    cuts = [0] + [i for i in range(1, n) if mask & (1 << (i - 1))] + [n]
                    parts = [text[a:b] for a, b in zip(cuts, cuts[1:], strict=False)] if n else []
                    if all(word in words for word in parts):
                        partitions.append(parts)
                actual = word_break(text, iter(words))
                if partitions:
                    self.assertIsNotNone(actual)
                    self.assertEqual("".join(actual), text)
                    self.assertTrue(all(word in words for word in actual))
                    self.assertEqual(len(actual), min(map(len, partitions)))
                else:
                    self.assertIsNone(actual)

    def test_ties_and_invalid(self):
        self.assertEqual(word_break("aaaa", ["a", "aa", "aaa"]), ["a", "aaa"])
        self.assertEqual(word_break("", []), [])
        for words in [[""], [1], [None]]:
            with self.assertRaises(ValueError):
                word_break("a", words)
