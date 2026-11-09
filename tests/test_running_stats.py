import math
import random
import statistics
import unittest

from algorithm_lab.running_stats import RunningStats


class RunningStatsTests(unittest.TestCase):
    def test_statistics_module_oracle_for_every_prefix(self):
        rng = random.Random(74)
        values, stats = [], RunningStats()
        for _ in range(150):
            value = rng.uniform(-1000, 1000)
            values.append(value)
            stats.add(value)
            self.assertEqual(stats.count, len(values))
            self.assertAlmostEqual(stats.mean, statistics.mean(values), places=10)
            self.assertAlmostEqual(stats.variance(), statistics.pvariance(values), places=7)
            if len(values) > 1:
                self.assertAlmostEqual(
                    stats.variance(sample=True), statistics.variance(values), places=7
                )

    def test_offset_constant_and_empty_streams(self):
        values = [1_000_000 + i / 4 for i in range(50)]
        self.assertAlmostEqual(
            RunningStats(values).variance(), statistics.pvariance(values), places=10
        )
        self.assertEqual(RunningStats([4] * 100).variance(sample=True), 0)
        with self.assertRaises(ValueError):
            _ = RunningStats().mean
        with self.assertRaises(ValueError):
            RunningStats().variance()
        with self.assertRaises(ValueError):
            RunningStats([1]).variance(sample=True)

    def test_variance_preserves_small_differences_at_large_offsets(self):
        for offset in [1e16, -1e16]:
            values = [offset, offset + 2, offset + 4, offset + 6]
            stats = RunningStats()
            for count, value in enumerate(values, 1):
                stats.add(value)
                prefix = values[:count]
                self.assertEqual(stats.mean, statistics.mean(prefix))
                self.assertEqual(stats.variance(), statistics.pvariance(prefix))
                if count > 1:
                    self.assertEqual(stats.variance(sample=True), statistics.variance(prefix))

    def test_invalid_observations_do_not_change_existing_state(self):
        stats = RunningStats([1, 2, 3])
        before = stats.count, stats.mean, stats.variance()
        for value in [math.nan, math.inf, -math.inf, True, "4", 10**1000, 1e308]:
            with self.assertRaises(ValueError):
                stats.add(value)
            self.assertEqual((stats.count, stats.mean, stats.variance()), before)
