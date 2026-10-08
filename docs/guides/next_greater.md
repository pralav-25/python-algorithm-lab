# Find the first later improvement for every position

[Guide index](../README.md) · [Implementation](../../algorithm_lab/next_greater.py)

## Reasoning

Keep unresolved positions on a monotonic stack. A newly encountered larger value answers every smaller position that it pops, and it is their first answer because they have remained unresolved until now. Each position is pushed and popped at most once.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.next_greater import next_greater
>>> values = [5, 1, 4, 4, 7]
>>> indices = next_greater(values)
>>> indices
[4, 2, 4, 4, -1]
>>> [values[index] if index != -1 else None for index in indices]
[7, 4, 7, 7, None]
>>> next_greater([2, 2])
[-1, -1]

```

## Boundary to remember

Results are indices, not the greater values themselves. Equal values do not count as improvements, and -1 must be checked before indexing the input.

## Practice exercise

Find later improvements in a signed series with duplicate low values,
then verify that each answer is the first strictly greater position.

```pycon
>>> from algorithm_lab.next_greater import next_greater
>>> temperatures = [-1, -4, -4, -2, 0, -3]
>>> indices = next_greater(temperatures)
>>> indices
[4, 3, 3, 4, -1, -1]
>>> expected = [
...     next((j for j in range(i + 1, len(temperatures)) if temperatures[j] > value), -1)
...     for i, value in enumerate(temperatures)
... ]
>>> assert indices == expected
>>> waits = [j - i if j != -1 else None for i, j in enumerate(indices)]
>>> waits
[4, 2, 1, 1, None, None]

```

The equal readings at indices one and two cannot answer each other.
Subtracting the current index converts a returned position into a wait;
the missing sentinel must be handled before that subtraction.
