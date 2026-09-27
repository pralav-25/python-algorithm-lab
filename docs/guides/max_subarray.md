# Find the strongest contiguous run

[Guide index](../README.md) · [Implementation](../../algorithm_lab/max_subarray.py)

## Reasoning

At each position, the best run ending there either extends the previous run or starts with the current value. A negative accumulated prefix cannot improve a future total, which is the key observation behind Kadane’s algorithm. Tracking slice boundaries alongside the sum gives a useful witness, not just a score.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.max_subarray import max_subarray
>>> changes = [4, -7, 3, 5, -2]
>>> total, start, stop = max_subarray(changes)
>>> total, changes[start:stop]
(8, [3, 5])
>>> assert total == sum(changes[start:stop])
>>> max_subarray([-8, -2, -5])
(-2, 1, 2)

```

## Boundary to remember

The chosen slice is nonempty: an all-negative series returns its least-negative entry. Stop indices are exclusive, and this problem differs from selecting any disconnected profitable observations.
