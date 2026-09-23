import itertools
import unittest

from algorithm_lab.kmp_search import kmp_search


class KMPTests(unittest.TestCase):
    def test_exhaustive_small_strings(self):
        texts = ["".join(chars) for n in range(7) for chars in itertools.product("ab", repeat=n)]
        patterns = ["".join(chars) for n in range(4) for chars in itertools.product("ab", repeat=n)]
        for text in texts:
            for pattern in patterns:
                expected = [i for i in range(len(text) + 1) if text.startswith(pattern, i)]
                self.assertEqual(kmp_search(text, pattern), expected)

    def test_unicode_and_fallbacks(self):
        self.assertEqual(kmp_search("🙂a🙂a🙂", "🙂a🙂"), [0, 2])
        self.assertEqual(kmp_search("abababac", "ababac"), [2])
