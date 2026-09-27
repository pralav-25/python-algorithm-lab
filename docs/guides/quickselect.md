# Select a median without sorting everything

[Guide index](../README.md) · [Implementation](../../algorithm_lab/quickselect.py)

## Reasoning

An order statistic needs only one ranked value. Partitioning into smaller, equal, and larger values identifies which region contains that rank; the other regions can be discarded. The equal region matters when many readings repeat. This implementation copies the input, so selecting a value does not rearrange the original observations.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.quickselect import quickselect
>>> readings = [12, 3, 8, 3, 6]
>>> quickselect(readings, len(readings) // 2)
6
>>> assert quickselect(readings, 1) == sorted(readings)[1] == 3
>>> assert readings == [12, 3, 8, 3, 6]
>>> quickselect([42], 0)
42

```

## Boundary to remember

The rank is zero-based and duplicate observations each occupy a rank. Deterministic pivot selection can still take quadratic time on adverse inputs; it is not a worst-case linear selection algorithm.
