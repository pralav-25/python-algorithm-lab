import itertools
import unittest

from algorithm_lab.word_break_count import word_break_count


class Tests(unittest.TestCase):
    def test_all_boundary_subsets(self):
        dictionaries = [[], ["a"], ["a", "aa"], ["a", "b", "ab"], ["ab", "ba", "aba"]]
        for size in range(6):
            for chars in itertools.product("ab", repeat=size):
                text = "".join(chars)
                for words in dictionaries:
                    expected = int(not text)
                    if text:
                        for mask in range(1 << (size - 1)):
                            cuts = [0] + [i for i in range(1, size) if mask >> (i - 1) & 1] + [size]
                            expected += all(
                                text[left:right] in words
                                for left, right in zip(cuts, cuts[1:], strict=False)
                            )
                    original = words[:]
                    self.assertEqual(word_break_count(text, iter(words + words)), expected)
                    self.assertEqual(words, original)
        self.assertEqual(word_break_count("🙂🙂", ["🙂", "🙂🙂"]), 2)

    def test_validates_empty_text(self):
        for words in [[""], ["a", 1], [None], [True]]:
            with self.assertRaises(ValueError):
                word_break_count("", words)
        with self.assertRaises(ValueError):
            word_break_count(None, ["a"])
