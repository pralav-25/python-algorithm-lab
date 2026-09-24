import random
import unittest

from algorithm_lab.ordered_multiset import OrderedMultiset


class MultisetTests(unittest.TestCase):
    def test_model(self):
        rng = random.Random(118)
        values, model = OrderedMultiset(), []
        for _ in range(300):
            value = rng.randrange(-6, 7)
            if rng.randrange(2):
                values.add(value)
                model.append(value)
            else:
                present = value in model
                self.assertEqual(values.discard(value), present)
                if present:
                    model.remove(value)
            self.assertEqual(values.count(value), model.count(value))
            self.assertEqual(values.rank(value), sum(v < value for v in model))
            self.assertEqual([values.select(i) for i in range(len(values))], sorted(model))

    def test_selection_validation(self):
        values = OrderedMultiset([1])
        for position in [-1, 1, True, 0.0]:
            with self.assertRaises(ValueError):
                values.select(position)
