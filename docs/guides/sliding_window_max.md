# Track rolling peak measurements

[Guide index](../README.md) · [Implementation](../../algorithm_lab/sliding_window_max.py)

## Reasoning

The deque keeps candidate indices in decreasing value order. A new larger value makes smaller candidates at the back useless: they expire earlier and can never win. Expired indices leave the front. Each index enters and leaves at most once, giving linear total work across all windows.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.sliding_window_max import sliding_window_max
>>> readings = [8, 2, 8, 1, 3]
>>> sliding_window_max(readings, 3)
[8, 8, 8]
>>> assert sliding_window_max(readings, 2) == [max(readings[i:i+2]) for i in range(4)]
>>> sliding_window_max(readings, 1) == readings
True
>>> sliding_window_max(readings, len(readings))
[8]

```

## Boundary to remember

Window size counts consecutive observations, not elapsed time. The size must be between one and the input length; repeated maxima must remain valid until their own positions expire.
