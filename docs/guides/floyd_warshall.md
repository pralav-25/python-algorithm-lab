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
