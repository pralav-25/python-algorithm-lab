import random
import unittest

from algorithm_lab.min_stack import MinStack


class MinStackTests(unittest.TestCase):
    def test_stack_model(self):
        rng = random.Random(114)
        stack, data = MinStack(), []
        for _ in range(500):
            if not data or rng.randrange(3):
                value = rng.randrange(-3, 4)
                stack.push(value)
                data.append(value)
            else:
                self.assertEqual(stack.pop(), data.pop())
            self.assertEqual(len(stack), len(data))
            if data:
                self.assertEqual(stack.peek(), data[-1])
                self.assertEqual(stack.minimum(), min(data))

    def test_empty_and_incomparable(self):
        stack = MinStack()
        for operation in [stack.pop, stack.peek, stack.minimum]:
            with self.assertRaises(IndexError):
                operation()
        stack.push(1)
        with self.assertRaises(TypeError):
            stack.push("x")
        self.assertEqual(len(stack), 1)
