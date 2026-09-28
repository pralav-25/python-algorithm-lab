# Keep an exact median between two balanced heaps

[Guide index](../README.md) · [Implementation](../../algorithm_lab/median_stream.py)

## Reasoning

A max-heap holds the lower half of the observations and a min-heap holds
the upper half. Moving boundary values keeps the lower heap equal in size or
one item larger. The middle value or middle pair is therefore always available
at the heap roots. Each insertion takes O(log n); median queries take O(1),
and retaining all observations requires O(n) space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.median_stream import MedianStream
>>> stream = MedianStream()
>>> for value in [8, 1, 4]:
...     stream.add(value)
>>> stream.median()
Fraction(4, 1)
>>> stream.add(5)
>>> stream.median()
Fraction(9, 2)
>>> len(stream)
4

```

## Boundary to remember

Only integers are accepted, excluding booleans. Fractions preserve the
exact midpoint of large integers, avoiding float rounding. Querying an empty
stream raises ValueError. There is no deletion or fixed-size rolling window;
the median covers every observation added so far.
