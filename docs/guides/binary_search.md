# Locate the first repeated timestamp

[Guide index](../README.md) · [Implementation](../../algorithm_lab/binary_search.py)

## Reasoning

A sorted event log lets you discard half the remaining candidates at each comparison. To find the first equal timestamp, continue searching to the left after equality instead of returning immediately. This preserves a boundary between values smaller than the target and values that may match, giving logarithmic search without copying the log.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.binary_search import binary_search
>>> timestamps = [5, 9, 9, 12, 18]
>>> binary_search(timestamps, 9)
1
>>> binary_search(timestamps, 10)
-1
>>> import bisect
>>> assert binary_search(timestamps, 9) == bisect.bisect_left(timestamps, 9)
>>> binary_search([], 9)
-1

```

## Boundary to remember

Sorting is a precondition, not a preprocessing step performed by this function. A missing timestamp returns -1, which must be checked before using the result as a Python index.
