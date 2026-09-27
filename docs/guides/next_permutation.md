# Advance one step in lexicographic order

[Guide index](../README.md) · [Implementation](../../algorithm_lab/next_permutation.py)

## Reasoning

Find the rightmost place where the sequence can increase. Swapping that pivot with the smallest larger value in its suffix makes the smallest possible increase; reversing the remaining decreasing suffix puts it in its smallest order. Repeated values work without generating duplicate permutations.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.next_permutation import next_permutation
>>> order = [1, 3, 2]
>>> next_permutation(order)
[2, 1, 3]
>>> assert order == [1, 3, 2]
>>> next_permutation([1, 1, 2])
[1, 2, 1]
>>> next_permutation([3, 2, 1]) is None
True

```

## Boundary to remember

The descending arrangement has no successor and returns None. The function does not wrap around to the first arrangement, and it leaves the original input unchanged.
