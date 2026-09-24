"""Return (maximum_flow, source_side_of_minimum_cut) for integer capacities.

Input maps nodes to neighbor: nonnegative integer capacity. Reverse edges and
loops are allowed; zero capacities are ignored during traversal. Source/sink
must be distinct vertices in the graph. O(V*E²) time, O(V+E) space. Input unchanged.

>>> max_flow({'s': {'t': 7}}, 's', 't')
(7, frozenset({'s'}))
"""

from collections import deque

from algorithm_lab._validation import integer


def max_flow(graph, source, sink):
    residual = {node: {} for node in graph}
    for node, neighbors in graph.items():
        for neighbor, capacity in neighbors.items():
            integer(capacity, "capacity", minimum=0)
            residual.setdefault(neighbor, {})
            residual[node][neighbor] = residual[node].get(neighbor, 0) + capacity
            residual[neighbor].setdefault(node, 0)
    if source == sink or source not in residual or sink not in residual:
        raise ValueError("source and sink must be distinct graph vertices")
    total = 0
    while True:
        parent, queue = {source: source}, deque([source])
        while queue and sink not in parent:
            node = queue.popleft()
            for neighbor, capacity in residual[node].items():
                if capacity > 0 and neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        if sink not in parent:
            return total, frozenset(parent)
        amount, node = None, sink
        while node != source:
            capacity = residual[parent[node]][node]
            amount = capacity if amount is None else min(amount, capacity)
            node = parent[node]
        node = sink
        while node != source:
            previous = parent[node]
            residual[previous][node] -= amount
            residual[node][previous] += amount
            node = previous
        total += amount
