# Count repeated transitions with matrix powers

[Guide index](../README.md) · [Implementation](../../algorithm_lab/matrix_power.py)

## Reasoning

An adjacency matrix’s kth power counts walks of length k. More generally, matrix powers compose the same linear transition repeatedly. Exponentiation by squaring groups those compositions according to exponent bits, using far fewer matrix products than multiplying one transition at a time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.matrix_power import matrix_power
>>> swap = [[0, 1], [1, 0]]
>>> matrix_power(swap, 2)
[[1, 0], [0, 1]]
>>> matrix_power(swap, 3)
[[0, 1], [1, 0]]
>>> assert matrix_power(swap, 0) == [[1, 0], [0, 1]]
>>> matrix_power([], 7)
[]

```

## Boundary to remember

The zeroth power is the identity, representing no transition. This routine uses dense integer matrices; the size of exact walk counts can grow even when the matrix dimensions stay small.

## Practice exercise

Count three-edge walks from vertex 0 to vertex 2 and verify the count by enumerating vertex sequences. Include walks that revisit vertices.

```pycon
>>> from itertools import product
>>> from algorithm_lab.matrix_power import matrix_power
>>> edges = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]
>>> counts = matrix_power(edges, 3)
>>> counts
[[1, 1, 1], [0, 1, 1], [1, 0, 1]]
>>> walks = [
...     path
...     for path in product(range(3), repeat=4)
...     if path[0] == 0 and path[-1] == 2 and all(edges[a][b] for a, b in zip(path, path[1:]))
... ]
>>> walks
[(0, 2, 0, 2)]
>>> assert counts[0][2] == len(walks) == 1

```

Three edges require four vertex positions. The counted walk revisits vertex 0 and uses the 0-to-2 edge twice; matrix powers count walks rather than only simple paths. Enumerating all four-position sequences is an independent small-graph check of that interpretation.
