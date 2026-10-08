# Sort priorities while preserving arrival order

[Guide index](../README.md) · [Implementation](../../algorithm_lab/merge_sort.py)

## Reasoning

Merge sort divides records into sorted halves and repeatedly chooses the smaller leading key. Choosing from the left half on a tie preserves earlier arrival order, which makes stable sorting useful for queue priorities. Evaluating each key once also avoids repeating an expensive extraction during comparisons.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.merge_sort import merge_sort
>>> jobs = [("first", 2), ("urgent", 1), ("second", 2)]
>>> merge_sort(jobs, key=lambda job: job[1])
[('urgent', 1), ('first', 2), ('second', 2)]
>>> assert merge_sort(jobs, key=lambda job: job[1]) == sorted(jobs, key=lambda job: job[1])
>>> assert jobs[0] == ("first", 2)
>>> merge_sort([])
[]

```

## Boundary to remember

Equal keys preserve their input order, but the keys still need a consistent total order. The returned list is new; references to the records themselves are not deep copies.

## Practice exercise

Sort words without regard to case while checking stable ties and one key
evaluation per input word.

```pycon
>>> from algorithm_lab.merge_sort import merge_sort
>>> words = ["pear", "Apple", "PEAR", "apricot"]
>>> calls = []
>>> def folded(word):
...     calls.append(word)
...     return word.casefold()
>>> merge_sort(words, key=folded)
['Apple', 'apricot', 'pear', 'PEAR']
>>> assert calls == words
>>> assert words == ["pear", "Apple", "PEAR", "apricot"]

```

The two pear spellings have equal keys, so their arrival order survives.
Comparing whole decorated tuples instead of only their keys could reorder
them by spelling; evaluating keys while merging would also repeat calls.
