# Split a total into unordered positive pieces

[Guide index](../README.md) · [Implementation](../../algorithm_lab/integer_partitions.py)

## Reasoning

Keeping parts nonincreasing removes permutations of the same partition from consideration. After choosing a part, later parts are bounded by it and must sum to the remaining total. This yields every unordered decomposition once while generating answers lazily.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.integer_partitions import integer_partitions
>>> partitions = list(integer_partitions(5))
>>> len(partitions)
7
>>> assert all(sum(parts) == 5 and list(parts) == sorted(parts, reverse=True) for parts in partitions)
>>> assert len(set(partitions)) == len(partitions)
>>> list(integer_partitions(0))
[()]

```

## Boundary to remember

Lazy output does not remove combinatorial growth or recursive depth limits. Zero has one valid decomposition, the empty tuple; it does not have zero decompositions.
