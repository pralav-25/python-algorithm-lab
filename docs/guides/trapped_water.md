# Compute the volume between retaining walls

[Guide index](../README.md) · [Implementation](../../algorithm_lab/trapped_water.py)

## Reasoning

At a position, water depth is limited by the lower of the tallest walls to its left and right. A two-pointer scan can settle the side with the lower current boundary because the opposite side already provides a wall high enough. Adding nonnegative depths yields total retained volume.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.trapped_water import trapped_water
>>> trapped_water([4, 1, 1, 4])
6
>>> trapped_water([0, 1, 2, 3])
0
>>> heights = [2, 0, 1, 0, 3]
>>> expected = sum(min(max(heights[:i+1]), max(heights[i:])) - h for i, h in enumerate(heights))
>>> assert trapped_water(heights) == expected == 5

```

## Boundary to remember

This counts volume above unit-width bars, not the maximum rectangle between two selected bars. Leading and trailing lows cannot retain water without enclosing walls.
