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
