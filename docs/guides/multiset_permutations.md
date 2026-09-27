# Enumerate distinct arrangements of repeated values

[Guide index](../README.md) · [Implementation](../../algorithm_lab/multiset_permutations.py)

## Reasoning

Starting from sorted values and repeatedly taking the next lexicographic arrangement visits each distinct value arrangement once. Equal elements do not receive separate identities, so the generator avoids the redundant outputs produced by permuting labeled positions and deduplicating afterward.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.multiset_permutations import multiset_permutations
>>> from itertools import permutations
>>> values = [1, 2, 2, 3]
>>> results = list(multiset_permutations(values))
>>> len(results)
12
>>> assert results == sorted(set(permutations(values)))
>>> list(multiset_permutations([]))
[()]

```

## Boundary to remember

The output count can still be enormous. Lazy iteration saves retained output storage, but it cannot eliminate the work required to visit each distinct arrangement.
