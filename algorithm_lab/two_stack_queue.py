"""Queue from two stacks: amortized O(1) enqueue/dequeue/peek and O(n) space.

One transfer can take O(n), but each item transfers at most once. Empty reads
raise IndexError. Any Python object, including None, can be stored.

>>> queue = TwoStackQueue()
>>> queue.enqueue(1); queue.enqueue(2)
>>> queue.dequeue(), queue.peek()
(1, 2)
"""


class TwoStackQueue:
    def __init__(self):
        self._incoming, self._outgoing = [], []

    def __len__(self):
        return len(self._incoming) + len(self._outgoing)

    def enqueue(self, value):
        self._incoming.append(value)

    def _transfer(self):
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())

    def dequeue(self):
        self._transfer()
        return self._outgoing.pop()

    def peek(self):
        self._transfer()
        return self._outgoing[-1]
