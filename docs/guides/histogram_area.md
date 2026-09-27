# Find a rectangle spanning several bars

[Guide index](../README.md) · [Implementation](../../algorithm_lab/histogram_area.py)

## Reasoning

A bar’s height can support a rectangle until a shorter bar blocks it on either side. A monotonic stack discovers those limiting boundaries when heights decrease. Popping a bar computes the widest rectangle for which that bar is the limiting height, so all candidates are covered in linear time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.histogram_area import histogram_area
>>> histogram_area([3, 3, 3, 1])
9
>>> histogram_area([5, 1, 5])
5
>>> histogram_area([0, 0])
0
>>> histogram_area([])
0

```

## Boundary to remember

Bars have unit width and nonnegative integer heights. The highest individual bar need not belong to the largest-area rectangle; several shorter bars can win together.
