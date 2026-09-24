"""Undoable disjoint sets on 0..size-1, using union by size without compression.

find/union O(log n), snapshot O(1), rollback O(number of undone merges), space
O(n). A snapshot is a history length valid on the current history branch;
a discarded branch's tokens must not be reused. Redundant unions add no history.

>>> groups = RollbackDisjointSet(3)
>>> token = groups.snapshot()
>>> groups.union(0, 1)
True
>>> groups.rollback(token)
>>> groups.components
3
"""

from algorithm_lab._validation import index, integer


class RollbackDisjointSet:
    def __init__(self, size):
        integer(size, "size", minimum=0)
        self._parent = list(range(size))
        self._size = [1] * size
        self._history = []
        self._components = size

    @property
    def components(self):
        return self._components

    def find(self, vertex):
        index(vertex, len(self._parent))
        while vertex != self._parent[vertex]:
            vertex = self._parent[vertex]
        return vertex

    def union(self, first, second):
        a, b = self.find(first), self.find(second)
        if a == b:
            return False
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._history.append((a, b, self._size[a]))
        self._parent[b] = a
        self._size[a] += self._size[b]
        self._components -= 1
        return True

    def snapshot(self):
        return len(self._history)

    def rollback(self, token):
        index(token, len(self._history), allow_end=True)
        while len(self._history) > token:
            a, b, size = self._history.pop()
            self._parent[b] = b
            self._size[a] = size
            self._components += 1
