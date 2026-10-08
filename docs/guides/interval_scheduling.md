# Fit the greatest number of appointments

[Guide index](../README.md) · [Implementation](../../algorithm_lab/interval_scheduling.py)

## Reasoning

Choosing the earliest finishing available appointment leaves at least as much time for every future choice as any alternative first appointment. Repeating this exchange argument proves the greedy strategy for maximizing the number of compatible activities. Sorting by finish time is the expensive step.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.interval_scheduling import interval_scheduling
>>> appointments = [(0, 10), (1, 3), (3, 6), (6, 8)]
>>> selected = interval_scheduling(appointments)
>>> selected
[(1, 3), (3, 6), (6, 8)]
>>> assert all(a[1] <= b[0] for a, b in zip(selected, selected[1:]))
>>> interval_scheduling([])
[]

```

## Boundary to remember

The objective is count, not revenue or total occupied time. Every interval has positive duration and half-open endpoints; weighted interval scheduling solves a different optimization problem.

## Practice exercise

Select as many short workshops as possible from five competing slots. Prove the returned count is optimal by checking every subset of this small schedule.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.interval_scheduling import interval_scheduling
>>> slots = [(0, 4), (0, 2), (2, 3), (3, 5), (4, 6)]
>>> selected = interval_scheduling(slots)
>>> selected
[(0, 2), (2, 3), (3, 5)]
>>> def compatible(group):
...     ordered = sorted(group)
...     return all(left[1] <= right[0] for left, right in zip(ordered, ordered[1:]))
>>> optimum = max(
...     size
...     for size in range(len(slots) + 1)
...     if any(compatible(group) for group in combinations(slots, size))
... )
>>> assert len(selected) == optimum == 3

```

The exhaustive oracle tests feasibility without copying the earliest-finish rule. More than one optimal schedule can exist; the implementation's specific selection is valid, while optimality concerns its count. Adjacent endpoints remain compatible because the intervals are half-open.
