# Count partitions with a fixed number of groups

[Guide index](../README.md) · [Implementation](../../algorithm_lab/stirling_second.py)

## Reasoning

Adding one distinct item to a partition either puts it into one of k existing groups or makes a new singleton group beside a partition into k-1 groups. These two disjoint cases produce the Stirling recurrence. Rolling rows compute the count without enumerating all group memberships.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.stirling_second import stirling_second
>>> stirling_second(4, 2)
7
>>> assert all(stirling_second(n, 2) == 2 ** (n - 1) - 1 for n in range(2, 9))
>>> sum(stirling_second(4, k) for k in range(5))
15
>>> stirling_second(0, 0), stirling_second(3, 4)
(1, 0)

```

## Boundary to remember

Groups are nonempty and unlabeled. Assigning names to the groups would multiply the count by k factorial, so distinguish partitions from labeled assignments.
