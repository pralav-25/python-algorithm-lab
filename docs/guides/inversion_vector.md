# Explain each position’s contribution to ranking disorder

[Guide index](../README.md) · [Implementation](../../algorithm_lab/inversion_vector.py)

## Reasoning

Scan from right to left while a Fenwick tree stores counts of values already seen. Coordinate compression maps large signed values to compact ranks, and a prefix query counts only strictly smaller ranks. This refines the total inversion count into one contribution per original position.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.inversion_vector import inversion_vector
>>> values = [4, 2, 2, 1]
>>> counts = inversion_vector(values)
>>> counts
[3, 1, 1, 0]
>>> assert counts == [sum(other < value for other in values[i + 1 :]) for i, value in enumerate(values)]
>>> inversion_vector([])
[]

```

## Boundary to remember

Equal values do not count as smaller. Compression must preserve order, not numeric distance, because the query concerns relative rank rather than arithmetic gaps.
