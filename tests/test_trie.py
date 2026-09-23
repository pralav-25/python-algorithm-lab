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
