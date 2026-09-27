# Count assignments where nobody keeps their own item

[Guide index](../README.md) · [Implementation](../../algorithm_lab/derangements.py)

## Reasoning

A derangement is a permutation with no fixed positions. Choosing where the first item goes leads to two cases: its destination either sends an item back, or participates in a longer cycle. Those cases produce the recurrence using the two previous counts without enumerating all permutations.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.derangements import derangements
>>> from itertools import permutations
>>> derangements(4)
9
>>> brute = sum(all(i != value for i, value in enumerate(order)) for order in permutations(range(4)))
>>> assert derangements(4) == brute
>>> derangements(0), derangements(1)
(1, 0)

```

## Boundary to remember

The objects are distinct. The empty permutation contributes one valid assignment, while a single object has no valid derangement.
