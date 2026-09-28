import random
import unittest

from algorithm_lab.trie import Trie


class TrieTests(unittest.TestCase):
    def test_set_oracle_after_mixed_operations(self):
        rng = random.Random(42)
        trie, expected = Trie(), set()
        for _ in range(300):
            word = "".join(rng.choices("abé", k=rng.randrange(6)))
            if rng.randrange(2):
                trie.add(word)
                expected.add(word)
            else:
                self.assertEqual(trie.discard(word), word in expected)
                expected.discard(word)
            self.assertEqual(len(trie), len(expected))
            self.assertEqual(trie.words(), sorted(expected))
            self.assertEqual(
                trie.words("a", limit=3), sorted(w for w in expected if w.startswith("a"))[:3]
            )
            self.assertEqual(word in trie, word in expected)

    def test_deep_word_prefix_and_invalid_limit(self):
        word = "a" * 1500
        trie = Trie(["", word, "car", "cart"])
        self.assertTrue(trie.discard("car"))
        self.assertIn("cart", trie)
        self.assertEqual(trie.words(word), [word])
        self.assertEqual(trie.words("missing"), [])
        self.assertEqual(trie.words(limit=0), [])
        for limit in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                trie.words(limit=limit)
        with self.assertRaises(TypeError):
            trie.add(123)

    def test_unicode_forms_case_and_null_characters_remain_distinct(self):
        composed, decomposed = "\u00e9", "e\u0301"
        values = ["", "e", composed, decomposed, "A", "a", "\0", "\0x", "\U0001f600"]
        trie = Trie(values)
        self.assertEqual(trie.words(), sorted(values))
        self.assertEqual(trie.words("e"), ["e", decomposed])
        self.assertTrue(trie.discard(composed))
        self.assertIn(decomposed, trie)
        self.assertNotIn(composed, trie)
        self.assertTrue(trie.discard("\0"))
        self.assertEqual(trie.words("\0"), ["\0x"])
        self.assertTrue(trie.discard(""))
        self.assertEqual(len(trie), len(values) - 3)
        self.assertIn("\U0001f600", trie)

    def test_every_prefix_limit_after_deleting_a_shared_branch(self):
        values = {"", "a", "ab", "abc", "abd", "b", "ba"}
        trie = Trie(values)
        self.assertTrue(trie.discard("ab"))
        values.remove("ab")
        for prefix in ("", "a", "ab", "abc", "b", "missing"):
            expected = sorted(word for word in values if word.startswith(prefix))
            for limit in range(len(values) + 2):
                self.assertEqual(trie.words(prefix, limit=limit), expected[:limit])
        self.assertFalse(trie.discard("ab"))
        self.assertEqual(trie.words(), sorted(values))
