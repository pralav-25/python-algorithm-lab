# Track rolling low measurements

[Guide index](../README.md) · [Implementation](../../algorithm_lab/sliding_window_min.py)

## Reasoning

An increasing deque holds candidates that may become a window minimum. A new smaller value makes larger trailing candidates obsolete because it expires later and is already better. Removing expired indices from the front leaves the current minimum available without rescanning the whole window.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.sliding_window_min import sliding_window_min
>>> readings = [5, 2, 4, 1, 3]
>>> sliding_window_min(readings, 3)
[2, 1, 1]
>>> assert sliding_window_min(readings, 2) == [min(readings[i:i+2]) for i in range(4)]
>>> sliding_window_min(readings, 1) == readings
True
>>> sliding_window_min(readings, 5)
[1]

```

## Boundary to remember

The width must fit the data and be positive. The minimum values alone do not identify which occurrence won; this function returns values rather than provenance indices.
