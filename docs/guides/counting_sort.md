# Sort measurements in a compact integer range

[Guide index](../README.md) · [Implementation](../../algorithm_lab/counting_sort.py)

## Reasoning

Counting sort replaces pairwise comparisons with a histogram. Subtracting the minimum gives every signed measurement a nonnegative bucket index. Walking the buckets in order reconstructs the sorted measurements. The benefit comes from a small value range, rather than a small number of distinct values alone.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.counting_sort import counting_sort
>>> temperatures = [-1, 2, -1, 0, 2, -2]
>>> counting_sort(temperatures)
[-2, -1, -1, 0, 2, 2]
>>> assert counting_sort(temperatures) == sorted(temperatures)
>>> counting_sort([7, 7], max_range=1)
[7, 7]
>>> counting_sort([])
[]

```

## Boundary to remember

Two observations a billion units apart still require a huge dense histogram. The max_range guard rejects that allocation; use a comparison sort when the range is sparse.
