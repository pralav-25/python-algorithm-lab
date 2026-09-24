"""LRU cache with expected O(1) get/put and O(capacity) space.

Keys are hashable. get raises KeyError on a miss; None is a valid value.
put returns an evicted (key, value) pair or None. Updating a key refreshes it.
Capacity must be positive. items returns a snapshot from least to most recent.

>>> cache = LRUCache(1)
>>> cache.put('a', None)
>>> cache.put('b', 2)
('a', None)
"""

from collections import OrderedDict

from algorithm_lab._validation import integer


class LRUCache:
    def __init__(self, capacity):
        self._capacity = integer(capacity, "capacity", minimum=1)
        self._data = OrderedDict()

    def __len__(self):
        return len(self._data)

    def get(self, key):
        value = self._data[key]
        self._data.move_to_end(key)
        return value

    def put(self, key, value):
        self._data[key] = value
        self._data.move_to_end(key)
        if len(self._data) > self._capacity:
            return self._data.popitem(last=False)
        return None

    def items(self):
        return list(self._data.items())
