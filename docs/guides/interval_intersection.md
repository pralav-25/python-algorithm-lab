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

## Practice exercise

Find the shared integer positions in two coverage maps, including negative coordinates and a shared endpoint. Check the result with ordinary set intersection.

```pycon
>>> from algorithm_lab.interval_intersection import interval_intersection
>>> first, second = [(-4, 0), (3, 6)], [(-2, 4), (6, 8)]
>>> shared = interval_intersection(first, second)
>>> shared
[(-2, 0), (3, 4), (6, 6)]
>>> def positions(intervals):
...     return {point for start, stop in intervals for point in range(start, stop + 1)}
>>> assert positions(shared) == positions(first) & positions(second)

```

The plus one in each range is essential because these intervals are closed. Position 6 appears even though the overlap has zero geometric length. This finite integer oracle checks coverage, while the interval result also keeps its compact ordered representation.
