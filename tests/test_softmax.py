import math
import unittest

from algorithm_lab.softmax import softmax


class Tests(unittest.TestCase):
    def test_log_odds_and_output_order(self):
        logits = [4, -3, 1, 4]
        probabilities = softmax(iter(logits))
        self.assertAlmostEqual(math.fsum(probabilities), 1)
        for i in range(len(logits)):
            for j in range(len(logits)):
                self.assertAlmostEqual(
                    math.log(probabilities[i] / probabilities[j]), logits[i] - logits[j]
                )
        self.assertEqual(softmax(reversed(logits)), list(reversed(probabilities)))
        self.assertEqual(logits, [4, -3, 1, 4])

    def test_multiple_maxima_survive_extreme_tail_underflow(self):
        self.assertEqual(softmax([1e308, -1e308, 1e308]), [0.5, 0, 0.5])
        self.assertEqual(softmax([-1e308] * 4), [0.25] * 4)

    def test_probability_and_shift_invariance(self):
        for logits in [[-2, 0, 1], [0], [3, 3, 3], [-50, 50]]:
            expected = [math.exp(v) / sum(math.exp(x) for x in logits) for v in logits]
            for actual, want in zip(softmax(logits), expected, strict=True):
                self.assertAlmostEqual(actual, want)
            for a, b in zip(softmax(logits), softmax([x + 1000 for x in logits]), strict=True):
                self.assertAlmostEqual(a, b)
        self.assertEqual(softmax([-1e308, 1e308]), [0, 1])

    def test_invalid(self):
        for values in [[], [math.nan], [math.inf], [True], [10**1000]]:
            with self.assertRaises(ValueError):
                softmax(values)
