import itertools
import random
import unittest
from collections import Counter

from algorithm_lab.reservoir_sample import reservoir_sample


class ScriptedRandom:
    def __init__(self, choices):
        self.choices = iter(choices)

    def randrange(self, stop):
        value = next(self.choices)
        assert 0 <= value < stop
        return value


class ReservoirTests(unittest.TestCase):
    def test_exact_uniformity_over_every_small_random_branch(self):
        counts = Counter()
        for choices in itertools.product(range(3), range(4)):
            result = reservoir_sample(range(4), 2, rng=ScriptedRandom(choices))
            counts[tuple(sorted(result))] += 1
        self.assertEqual(counts, Counter({pair: 2 for pair in itertools.combinations(range(4), 2)}))

    def test_seed_reproducibility_and_input_positions(self):
        a = reservoir_sample(range(100), 8, rng=random.Random(8))
        b = reservoir_sample(range(100), 8, rng=random.Random(8))
        self.assertEqual(a, b)
        self.assertEqual(len(set(a)), 8)
        self.assertEqual(reservoir_sample(["x", "x"], 2), ["x", "x"])
        self.assertEqual(reservoir_sample([], 2), [])

    def test_zero_does_not_consume_and_bad_sizes(self):
        stream = iter([1, 2])
        self.assertEqual(reservoir_sample(stream, 0), [])
        self.assertEqual(next(stream), 1)
        for size in [-1, True, 1.5]:
            with self.assertRaises(ValueError):
                reservoir_sample([], size)

    def test_each_post_fill_draw_uses_the_number_of_seen_positions(self):
        class RecordingRandom:
            def __init__(self):
                self.stops = []

            def randrange(self, stop):
                self.stops.append(stop)
                return stop - 1  # Always reject the arriving item after filling.

        rng = RecordingRandom()
        seen = []

        def stream():
            for value in range(10):
                seen.append(value)
                yield value

        self.assertEqual(reservoir_sample(stream(), 3, rng=rng), [0, 1, 2])
        self.assertEqual(seen, list(range(10)))
        self.assertEqual(rng.stops, list(range(4, 11)))

    def test_sampling_does_not_change_the_module_random_state(self):
        state = random.getstate()
        reservoir_sample(range(20), 3, rng=random.Random(11))
        self.assertEqual(random.getstate(), state)
        reservoir_sample(range(20), 3)
        self.assertEqual(random.getstate(), state)
