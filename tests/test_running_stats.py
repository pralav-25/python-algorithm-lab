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

    def test_invalid_observations_do_not_change_existing_state(self):
        stats = RunningStats([1, 2, 3])
        before = stats.count, stats.mean, stats.variance()
        for value in [math.nan, math.inf, -math.inf, True, "4", 10**1000, 1e308]:
            with self.assertRaises(ValueError):
                stats.add(value)
            self.assertEqual((stats.count, stats.mean, stats.variance()), before)
