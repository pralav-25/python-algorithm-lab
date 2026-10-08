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

## Practice exercise

Merge overlapping signed coordinate ranges and verify that their covered
integer points are preserved.

```pycon
>>> from algorithm_lab.merge_intervals import merge_intervals
>>> spans = [(-4, -1), (7, 9), (-2, 2), (8, 8)]
>>> combined = merge_intervals(spans)
>>> combined
[(-4, 2), (7, 9)]
>>> original_points = {x for start, end in spans for x in range(start, end + 1)}
>>> merged_points = {x for start, end in combined for x in range(start, end + 1)}
>>> assert original_points == merged_points
>>> assert all(left[1] < right[0] for left, right in zip(combined, combined[1:]))

```

The singleton at eight is already contained in a larger interval and
adds no component. Closed endpoints require `end + 1` when checking
integer coverage, and negative coordinates use the same ordering rules.
