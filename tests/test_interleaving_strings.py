import itertools
import unittest

from algorithm_lab.interleaving_strings import interleaving_strings


class Tests(unittest.TestCase):
    def test_position_assignment_oracle(self):
        words = ["".join(chars) for n in range(3) for chars in itertools.product("ab", repeat=n)]
        for first, second in itertools.product(words, repeat=2):
            possible = set()
            size = len(first) + len(second)
            for selected in itertools.combinations(range(size), len(first)):
                selected = set(selected)
                one, two, result = iter(first), iter(second), []
                for index in range(size):
                    result.append(next(one) if index in selected else next(two))
                possible.add("".join(result))
            for chars in itertools.product("ab", repeat=size):
                result = "".join(chars)
                self.assertEqual(interleaving_strings(first, second, result), result in possible)
        self.assertTrue(interleaving_strings("🙂a", "β", "🙂βa"))
        self.assertFalse(interleaving_strings("a", "b", "a"))

    def test_invalid(self):
        for args in [(None, "", ""), ("", [], ""), ("", "", b"")]:
            with self.assertRaises(ValueError):
                interleaving_strings(*args)
