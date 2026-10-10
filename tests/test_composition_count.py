import unittest

from algorithm_lab.composition_count import composition_count


def compositions(n):
    if n == 0:
        yield ()
    for first in range(1, n + 1):
        for rest in compositions(n - first):
            yield (first,) + rest


class Tests(unittest.TestCase):
    def test_recursive_enumeration(self):
        for n in range(10):
            values = list(compositions(n))
            self.assertEqual(composition_count(n), len(values))
            for parts in range(n + 3):
                self.assertEqual(
                    composition_count(n, parts), sum(len(value) == parts for value in values)
                )

    def test_invalid(self):
        for args in ((-1,), (True,), (1.5,), (3, -1), (3, True), (3, "2")):
            with self.assertRaises(ValueError):
                composition_count(*args)
