# Divide distinct positions into unlabeled groups

[Guide index](../README.md) · [Implementation](../../algorithm_lab/set_partitions.py)

## Reasoning

Assign each new position to an existing block or begin the next block. Ordering blocks by their first member prevents group labels from producing duplicate answers. This enumerates groupings of distinct positions, unlike integer partitions, which only retain group sizes.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.set_partitions import set_partitions
>>> groups = list(set_partitions(3))
>>> len(groups)
5
>>> assert all(
...     sorted(item for block in partition for item in block) == [0, 1, 2] for partition in groups
... )
>>> assert len(set(groups)) == len(groups)
>>> list(set_partitions(0))
[()]

```

## Boundary to remember

The number of partitions grows as a Bell number, so enumeration is practical only for small sets. Equal-valued objects should still be assigned distinct positions if they represent distinct entities.
