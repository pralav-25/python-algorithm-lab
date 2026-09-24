import unittest

from algorithm_lab.josephus import josephus


class JosephusTests(unittest.TestCase):
    def test_list_elimination_oracle(self):
        for size in range(1, 60):
            for step in [1, 2, 3, 7, 100, 10**30]:
                people, position = list(range(size)), 0
                while len(people) > 1:
                    position = (position + step - 1) % len(people)
                    people.pop(position)
                self.assertEqual(josephus(size, step), people[0])

    def test_invalid(self):
        for size, step in [(0, 1), (1, 0), (-1, 3), (True, 1), (2, 1.5)]:
            with self.assertRaises(ValueError):
                josephus(size, step)
