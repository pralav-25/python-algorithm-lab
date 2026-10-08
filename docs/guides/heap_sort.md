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

## Practice exercise

Sort a one-use event stream by timestamp and then event name, retaining duplicate records. Verify the multiplicities without depending on heap operations.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.heap_sort import heap_sort
>>> events = [("09:10", "review"), ("08:50", "build"), ("09:10", "deploy"), ("08:50", "build")]
>>> stream = iter(events)
>>> ordered = heap_sort(stream)
>>> ordered
[('08:50', 'build'), ('08:50', 'build'), ('09:10', 'deploy'), ('09:10', 'review')]
>>> assert Counter(ordered) == Counter(events)
>>> assert all(left <= right for left, right in zip(ordered, ordered[1:]))
>>> list(stream)
[]

```

Tuples use their full lexicographic order, so event names break equal-timestamp ties. That behavior does not establish stability by timestamp alone. Copying the iterable consumes a generator once, while the sorted output still retains every duplicate.
