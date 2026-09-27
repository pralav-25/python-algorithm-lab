# Search a sorted cycle without unrotating it

[Guide index](../README.md) · [Implementation](../../algorithm_lab/rotated_search.py)

## Reasoning

Splitting a rotated strictly increasing sequence at its midpoint leaves at least one sorted half. Compare the target with that half’s bounds to decide whether to keep it or discard it. This restores binary search’s ability to remove half the candidates despite the single wraparound.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.rotated_search import rotated_search
>>> base = [2, 5, 9, 14, 20]
>>> rotated = base[3:] + base[:3]
>>> rotated_search(rotated, 5)
3
>>> assert all(rotated[rotated_search(rotated, value)] == value for value in base)
>>> rotated_search(rotated, 7), rotated_search([], 7)
(-1, -1)

```

## Boundary to remember

The contract requires distinct values. With duplicates, equal endpoints can hide which half contains the rotation, so this logarithmic decision rule is not sufficient.
