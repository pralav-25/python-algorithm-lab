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

## Practice exercise

Choose a best run from a series with several equal totals, and verify the
API's preference for the earliest start and then the earliest stop.

```pycon
>>> from algorithm_lab.max_subarray import max_subarray
>>> changes = [0, 3, -3, 3]
>>> max_subarray(changes)
(3, 0, 2)
>>> candidates = [
...     (sum(changes[i:j]), i, j) for i in range(len(changes)) for j in range(i + 1, len(changes) + 1)
... ]
>>> expected = min(candidates, key=lambda row: (-row[0], row[1], row[2]))
>>> assert max_subarray(changes) == expected

```

Keeping a zero prefix preserves the earlier starting index. Replacing the
best result on an equal total would incorrectly favor a later stopping
position, even though the numeric maximum stayed correct.
