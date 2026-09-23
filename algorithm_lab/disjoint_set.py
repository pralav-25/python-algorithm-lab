"""Disjoint sets on vertices 0 through size-1 with union by size and path compression.

Construction and storage use O(n); find/union are amortized O(alpha(n)), where
alpha is the inverse Ackermann function. groups scans all vertices. Invalid
indices raise ValueError; union returns whether two components actually merged.

>>> groups = DisjointSet(4)
>>> groups.union(0, 2)
True
>>> groups.component_size(2)
2
"""


class DisjointSet:
    def __init__(self, size: int):
        if isinstance(size, bool) or not isinstance(size, int) or size < 0:
            raise ValueError("size must be a nonnegative integer")
        self._parent = list(range(size))
        self._sizes = [1] * size
        self._components = size

    def __len__(self) -> int:
        return len(self._parent)

    @property
    def components(self) -> int:
        return self._components

    def find(self, vertex: int) -> int:
        if isinstance(vertex, bool) or not isinstance(vertex, int) or not 0 <= vertex < len(self):
            raise ValueError("vertex is out of range")
        while vertex != self._parent[vertex]:
            self._parent[vertex] = self._parent[self._parent[vertex]]
            vertex = self._parent[vertex]
        return vertex

    def union(self, first: int, second: int) -> bool:
        a, b = self.find(first), self.find(second)
        if a == b:
            return False
        if self._sizes[a] < self._sizes[b]:
            a, b = b, a
        self._parent[b] = a
        self._sizes[a] += self._sizes[b]
        self._components -= 1
        return True

    def connected(self, first: int, second: int) -> bool:
        return self.find(first) == self.find(second)

    def component_size(self, vertex: int) -> int:
        return self._sizes[self.find(vertex)]

    def groups(self) -> list[frozenset[int]]:
        result = {}
        for vertex in range(len(self)):
            result.setdefault(self.find(vertex), set()).add(vertex)
        return [frozenset(group) for group in result.values()]
