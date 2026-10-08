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

## Practice exercise

Split seven identical units among exactly three nonempty groups, each holding at most three units. Compare the restricted partitions with a combinations-based enumeration.

```pycon
>>> from itertools import combinations_with_replacement
>>> from algorithm_lab.integer_partitions import integer_partitions
>>> allowed = [parts for parts in integer_partitions(7) if len(parts) == 3 and max(parts) <= 3]
>>> allowed
[(3, 3, 1), (3, 2, 2)]
>>> oracle = {
...     tuple(reversed(parts))
...     for parts in combinations_with_replacement(range(1, 4), 3)
...     if sum(parts) == 7
... }
>>> assert set(allowed) == oracle

```

Groups are indistinguishable, so rearranging (3, 2, 2) creates no new allocation. The independent oracle starts with nondecreasing combinations and reverses them to match the partition convention. Filtering is convenient for this small total but still generates all unrestricted partitions first.
