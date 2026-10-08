# Separate equal keys during partition sorting

[Guide index](../README.md) · [Implementation](../../algorithm_lab/quick_sort.py)

## Reasoning

Three-way partitioning splits values into smaller, equal, and larger regions around a pivot. The equal region already belongs together and requires no further partitioning, which is especially useful when many values repeat. An explicit work stack avoids recursive call depth.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.quick_sort import quick_sort
>>> values = [8, 2, 8, -1, 8, 2]
>>> quick_sort(values)
[-1, 2, 2, 8, 8, 8]
>>> assert quick_sort(iter(values)) == sorted(values)
>>> assert values == [8, 2, 8, -1, 8, 2]
>>> quick_sort([])
[]

```

## Boundary to remember

The middle-position pivot does not guarantee balanced partitions for every input. Worst-case quadratic work remains possible, and equal-key records are not promised stable ordering.

## Practice exercise

Sort tuple records by their complete lexicographic order and check that
partitioning retains every duplicate record.

```pycon
>>> from algorithm_lab.quick_sort import quick_sort
>>> from collections import Counter
>>> records = [(2, "z"), (1, "b"), (1, "a"), (2, "z"), (0, "c")]
>>> ordered = quick_sort(iter(records))
>>> ordered
[(0, 'c'), (1, 'a'), (1, 'b'), (2, 'z'), (2, 'z')]
>>> assert ordered == sorted(records)
>>> assert Counter(ordered) == Counter(records)
>>> assert records[0] == (2, "z")

```

Equal first components do not make two tuples equal: the second component
breaks the tie. The three-way equal partition must retain both copies of
`(2, "z")`; the API has no separate key function for field-only sorting.
