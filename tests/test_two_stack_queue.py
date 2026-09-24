import random
import unittest
from collections import deque

from algorithm_lab.two_stack_queue import TwoStackQueue


class QueueTests(unittest.TestCase):
    def test_against_deque(self):
        rng = random.Random(117)
        queue, model = TwoStackQueue(), deque()
        for _ in range(500):
            if rng.randrange(2):
                value = rng.choice([None, "a", 3])
                queue.enqueue(value)
                model.append(value)
            elif model:
                self.assertEqual(queue.peek(), model[0])
                self.assertEqual(queue.dequeue(), model.popleft())
            else:
                for operation in [queue.peek, queue.dequeue]:
                    with self.assertRaises(IndexError):
                        operation()
            self.assertEqual(len(queue), len(model))
