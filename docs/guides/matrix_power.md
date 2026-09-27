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
