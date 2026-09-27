# Cover a target range using the fewest available spans

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_interval_cover.py)

## Reasoning

At the current covered boundary, inspect every interval that starts no later and choose the one reaching farthest. Any solution must extend from that boundary, and the farthest choice leaves no less coverage for later steps. If no interval extends coverage, the target contains a gap.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.minimum_interval_cover import minimum_interval_cover
>>> spans = [(0, 3), (0, 5), (4, 8), (7, 10)]
>>> minimum_interval_cover(spans, 0, 10)
[1, 2, 3]
>>> minimum_interval_cover([(0, 2), (3, 5)], 0, 5) is None
True
>>> minimum_interval_cover([(0, 2), (2, 5)], 0, 5)
[0, 1]

```

## Boundary to remember

Intervals and the target are closed, so touching endpoints maintain continuous coverage. Returned indices refer to the original interval list, and None indicates a gap rather than an empty successful cover.
