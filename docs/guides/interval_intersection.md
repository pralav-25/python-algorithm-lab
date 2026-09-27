# Intersect two sorted coverage maps

[Guide index](../README.md) · [Implementation](../../algorithm_lab/interval_intersection.py)

## Reasoning

The overlap between two current intervals runs from the larger start to the smaller end. After recording a valid overlap, advance the interval that ends first because it cannot meet any later interval from the other list. Two forward pointers therefore cover all intersections in linear time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.interval_intersection import interval_intersection
>>> left, right = [(0, 3), (6, 10)], [(2, 7), (10, 12)]
>>> interval_intersection(left, right)
[(2, 3), (6, 7), (10, 10)]
>>> assert interval_intersection(left, right) == interval_intersection(right, left)
>>> interval_intersection(left, [])
[]

```

## Boundary to remember

Each input list must already be sorted and internally disjoint with strict gaps. Intervals are closed, so a single shared endpoint is a valid output interval.
