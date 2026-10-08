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

## Practice exercise

Count five-person gift exchanges that forbid self-assignment. Check the recurrence against a bounded explicit enumeration of all recipient permutations.

```pycon
>>> from itertools import permutations
>>> from algorithm_lab.derangements import derangements
>>> assignments = [
...     order
...     for order in permutations(range(5))
...     if all(person != recipient for person, recipient in enumerate(order))
... ]
>>> len(assignments)
44
>>> assert derangements(5) == len(assignments)
>>> assert derangements(5) == 4 * (derangements(4) + derangements(3))

```

A recipient permutation also prevents two people from receiving the same gift. Checking only the no-self rule on arbitrary recipient lists would allow collisions and count a different exchange problem.
