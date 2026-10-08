# Allocate a fixed total under individual caps

[Guide index](../README.md) · [Implementation](../../algorithm_lab/bounded_compositions.py)

## Reasoning

A composition assigns an amount to each labeled position. At every prefix, the chosen amounts reduce the remaining total, while the remaining caps bound what can still be achieved. Pruning impossible prefixes and using an explicit stack enumerates only feasible allocations without recursive call depth.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.bounded_compositions import bounded_compositions
>>> from itertools import product
>>> caps = [1, 2, 2]
>>> allocations = list(bounded_compositions(3, caps))
>>> expected = [row for row in product(*(range(cap + 1) for cap in caps)) if sum(row) == 3]
>>> assert allocations == expected
>>> list(bounded_compositions(0, [])), list(bounded_compositions(1, []))
([()], [])

```

## Boundary to remember

Positions are labeled, so swapping allocations between two positions usually creates a different result. This is different from an integer partition, where part order is ignored.

## Practice exercise

Allocate five units across bins capped at two, one, and three. Enumerate the allocations by considering where the single unused unit can remain.

```pycon
>>> from algorithm_lab.bounded_compositions import bounded_compositions
>>> allocations = list(bounded_compositions(5, [2, 1, 3]))
>>> allocations
[(1, 1, 3), (2, 0, 3), (2, 1, 2)]
>>> assert all(sum(row) == 5 for row in allocations)

```

The caps sum to six, so every allocation leaves exactly one unit of slack. Each of the three bins can hold that slack, giving three labeled allocations.
