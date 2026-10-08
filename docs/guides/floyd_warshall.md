# Allow one more intermediate vertex at each stage

[Guide index](../README.md) · [Implementation](../../algorithm_lab/floyd_warshall.py)

## Reasoning

At stage k, the distance from i to j is the best route whose intermediate
vertices come from the first k choices. Such a route either avoids k or joins
the best i-to-k and k-to-j routes. This recurrence fills an all-pairs matrix in
O(V cubed) time and O(V squared) space. A negative final diagonal identifies
a negative cycle.

## Worked example

Run these statements from the repository root.

```pycon
>>> from math import inf
>>> from algorithm_lab.floyd_warshall import floyd_warshall
>>> roads = [[0, 4, 10], [inf, 0, -2], [inf, inf, 0]]
>>> floyd_warshall(roads)
[[0, 4, 2], [inf, 0, -2], [inf, inf, 0]]
>>> roads[0][2]
10
>>> floyd_warshall([[-1]])
Traceback (most recent call last):
...
ValueError: graph contains a negative cycle

```

## Boundary to remember

Input must be square. Positive infinity means a missing edge; a positive
diagonal is replaced by zero because staying put costs nothing. Negative edges
are allowed, but a negative cycle anywhere is rejected. The input is copied,
and the result contains distances rather than reconstructed routes.

## Practice exercise

Find the cheapest route from warehouse 0 to warehouse 3 when the best trip requires two intermediate warehouses. Keep unreachable reverse trips distinguishable from zero-cost trips.

```pycon
>>> from math import inf
>>> from algorithm_lab.floyd_warshall import floyd_warshall
>>> costs = [[0, 7, 1, inf], [inf, 0, inf, 2], [inf, 2, 0, 9], [inf, inf, inf, 0]]
>>> distances = floyd_warshall(costs)
>>> distances[0]
[0, 3, 1, 5]
>>> assert distances[0][3] == costs[0][2] + costs[2][1] + costs[1][3]
>>> assert distances[3][0] == inf
>>> assert distances[3][3] == 0

```

The direct 2-to-3 edge costs 9, but the route through warehouse 1 costs 4. Combining that improvement with 0-to-2 produces cost 5. Intermediate vertices can appear in a different order from their indices; successive matrix stages still discover the complete route.
