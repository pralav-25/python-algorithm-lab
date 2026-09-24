import random
import unittest

from algorithm_lab.weighted_interval_scheduling import weighted_interval_scheduling


class WeightedScheduleTests(unittest.TestCase):
    def test_subset_oracle(self):
        rng = random.Random(159)
        for _ in range(250):
            jobs = []
            for _ in range(rng.randrange(9)):
                start = rng.randrange(-5, 8)
                jobs.append((start, start + rng.randrange(1, 6), rng.randrange(-5, 15)))
            best = 0
            for mask in range(1 << len(jobs)):
                chosen = sorted(job for i, job in enumerate(jobs) if mask & (1 << i))
                if all(a[1] <= b[0] for a, b in zip(chosen, chosen[1:], strict=False)):
                    best = max(best, sum(job[2] for job in chosen))
            total, indices = weighted_interval_scheduling(iter(jobs))
            self.assertEqual(total, best)
            self.assertEqual(total, sum(jobs[i][2] for i in indices))
            self.assertEqual(len(indices), len(set(indices)))
            self.assertTrue(
                all(jobs[a][1] <= jobs[b][0] for a, b in zip(indices, indices[1:], strict=False))
            )

    def test_invalid_and_ties(self):
        self.assertEqual(weighted_interval_scheduling([(0, 2, 3), (0, 2, 3)]), (3, [0]))
        for jobs in [[(0, 0, 1)], [(2, 1, 1)], [(0, 1, True)], [(False, 1, 2)]]:
            with self.assertRaises(ValueError):
                weighted_interval_scheduling(jobs)
