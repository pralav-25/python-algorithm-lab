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

## Practice exercise

Calculate an exact median for an even sample by selecting both central
ranks, and verify every rank on the same duplicate-containing sample.

```pycon
>>> from algorithm_lab.quickselect import quickselect
>>> from fractions import Fraction
>>> readings = [10, -5, 2, 7, 2, 5]
>>> middle = len(readings) // 2
>>> median = Fraction(quickselect(readings, middle - 1) + quickselect(readings, middle), 2)
>>> median
Fraction(7, 2)
>>> assert [quickselect(readings, rank) for rank in range(len(readings))] == sorted(readings)
>>> assert readings == [10, -5, 2, 7, 2, 5]

```

For an even number of readings, one selected value is not the median;
the two central values are averaged. Both copies of two occupy ranks,
so deduplicating before selection would change those central positions.
