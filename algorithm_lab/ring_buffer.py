"""Bounded FIFO with O(1) append/popleft and O(capacity) storage.

Appending when full raises OverflowError without dropping data. Empty reads
raise IndexError. to_list returns a snapshot in FIFO order. None is valid data.

>>> buffer = RingBuffer(2)
>>> buffer.append('a'); buffer.append('b')
>>> buffer.popleft()
'a'
>>> buffer.append('c'); buffer.to_list()
['b', 'c']
"""

from algorithm_lab._validation import integer


class RingBuffer:
    def __init__(self, capacity):
        self._data = [None] * integer(capacity, "capacity", minimum=1)
        self._head = self._size = 0

    def __len__(self):
        return self._size

    def append(self, value):
        if self._size == len(self._data):
            raise OverflowError("buffer is full")
        self._data[(self._head + self._size) % len(self._data)] = value
        self._size += 1

    def popleft(self):
        if not self._size:
            raise IndexError("buffer is empty")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % len(self._data)
        self._size -= 1
        return value

    def to_list(self):
        return [self._data[(self._head + i) % len(self._data)] for i in range(self._size)]
