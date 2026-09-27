# Combine closed coverage ranges

[Guide index](../README.md) · [Implementation](../../algorithm_lab/merge_intervals.py)

## Reasoning

After sorting by the starting endpoint, only the last merged interval can overlap the next range. Extend that interval’s end when needed; otherwise start a new component. This scan works because no later start can bridge a gap that the current start already leaves open.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.merge_intervals import merge_intervals
>>> ranges = [(7, 9), (0, 4), (4, 8), (12, 12)]
>>> merge_intervals(ranges)
[(0, 9), (12, 12)]
>>> merged = merge_intervals(ranges)
>>> assert merge_intervals(merged) == merged
>>> merge_intervals([])
[]

```

## Boundary to remember

These are closed intervals: ranges meeting at a single endpoint overlap. Scheduling uses half-open intervals instead, where one activity may start exactly when another ends.
