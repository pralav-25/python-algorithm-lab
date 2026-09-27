# Extract maxima into their final sorted positions

[Guide index](../README.md) · [Implementation](../../algorithm_lab/heap_sort.py)

## Reasoning

A max heap keeps each parent at least as large as its children. Its root is therefore the largest remaining value. Swapping that root to the end, shortening the heap, and restoring the parent rule grows a sorted suffix. Heap construction followed by repeated extraction gives a predictable n log n bound.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.heap_sort import heap_sort
>>> scores = [11, -4, 11, 2, 0]
>>> heap_sort(scores)
[-4, 0, 2, 11, 11]
>>> assert heap_sort(scores) == sorted(scores)
>>> assert scores == [11, -4, 11, 2, 0]
>>> heap_sort([])
[]

```

## Boundary to remember

Heap sort can reorder equal-key records. The sorting workspace is constant only after accounting for the new list copied from the caller; total extra storage here includes that output copy.
