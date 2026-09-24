"""Stack supporting push, pop, peek and minimum in O(1) time; O(n) space.

Values must be mutually comparable with a total order. Empty reads raise
IndexError. Duplicate minima remain valid after one copy is popped.

>>> stack = MinStack()
>>> for value in [3, 1, 1]: stack.push(value)
>>> stack.pop(), stack.minimum()
(1, 1)
"""


class MinStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, value):
        minimum = min(value, self._data[-1][1]) if self._data else value
        self._data.append((value, minimum))

    def pop(self):
        return self._data.pop()[0]

    def peek(self):
        return self._data[-1][0]

    def minimum(self):
        return self._data[-1][1]
