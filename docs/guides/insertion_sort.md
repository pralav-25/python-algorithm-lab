# Insertion sort returning a new ascending list.

[Guide index](../README.md) · [Implementation](../../algorithm_lab/insertion_sort.py)

## Reasoning

After each pass, the processed prefix is sorted. Take the next item and shift larger prefix items one place right until its insertion point opens; this preserves the relative order of items whose keys compare equal.

## Worked example

The implementation's small example shows the return value directly:

```python
from algorithm_lab.insertion_sort import insertion_sort

print(repr(insertion_sort([4, -2, 4, 1])))  # [-2, 1, 4, 4]
```

## Boundary to remember

The function returns a new list and does not mutate the input. It is stable, but reverse-sorted data still requires quadratic comparisons and shifts.

## Practice exercise

Sort a short list of records by a key while retaining original order among equal keys.
