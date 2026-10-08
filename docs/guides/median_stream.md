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

## Practice exercise

Track measurements near a very large integer and verify their even-count
median without introducing floating-point rounding.

```pycon
>>> from algorithm_lab.median_stream import MedianStream
>>> from fractions import Fraction
>>> baseline = 10**30
>>> observations = [baseline + 4, baseline - 2, baseline + 1, baseline - 1]
>>> readings = MedianStream()
>>> for observation in observations:
...     readings.add(observation)
>>> ordered = sorted(observations)
>>> expected = Fraction(ordered[1] + ordered[2], 2)
>>> assert readings.median() == expected == baseline
>>> readings.add(baseline - 7)
>>> assert readings.median() == baseline - 1

```

An even-count median averages the two heap boundaries exactly. Converting
the observations to floats before averaging can erase their small offsets
from the baseline; `Fraction` retains them.
