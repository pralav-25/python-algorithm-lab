# Prune a board search with occupied lines

[Guide index](../README.md) · [Implementation](../../algorithm_lab/n_queens.py)

## Reasoning

Place one queen per row and track occupied columns and both diagonal directions with bit masks. A candidate position can be rejected before exploring any deeper rows if one of those lines is already occupied. Backtracking then visits only partial placements that might still lead to a solution.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.n_queens import n_queens
>>> placements = list(n_queens(4))
>>> len(placements)
2
>>> assert all(len(set(p)) == len(p) for p in placements)
>>> assert all(
...     abs(a - b) != abs(p[a] - p[b]) for p in placements for a in range(4) for b in range(a + 1, 4)
... )
>>> list(n_queens(2)), list(n_queens(0))
([], [()])

```

## Boundary to remember

The output tuple gives one column for each row; it is not a list of arbitrary coordinates. Counting and enumerating are different tasks, and storing all placements quickly becomes expensive.
