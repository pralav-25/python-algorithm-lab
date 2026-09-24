import random
import unittest
from collections import deque

from algorithm_lab.ring_buffer import RingBuffer


class RingTests(unittest.TestCase):
    def test_wraparound_model(self):
        rng = random.Random(116)
        buffer, model = RingBuffer(3), deque()
        for _ in range(400):
            if rng.randrange(2):
                value = rng.choice([None, 1, 2])
                if len(model) == 3:
                    with self.assertRaises(OverflowError):
                        buffer.append(value)
                else:
                    buffer.append(value)
                    model.append(value)
            elif model:
                self.assertEqual(buffer.popleft(), model.popleft())
            else:
                with self.assertRaises(IndexError):
                    buffer.popleft()
            self.assertEqual(buffer.to_list(), list(model))
            self.assertEqual(len(buffer), len(model))

    def test_capacity(self):
        for value in [0, -1, True, 0.5]:
            with self.assertRaises(ValueError):
                RingBuffer(value)
