# Sort signed identifiers one byte at a time

[Guide index](../README.md) · [Implementation](../../algorithm_lab/radix_sort.py)

## Reasoning

Radix sorting groups values by successive low-to-high bytes. Every pass must be stable so ordering established by earlier bytes survives. Shifting keys by the minimum handles negative identifiers without reversing a negative partition. The number of passes depends on the spread of the values, not their absolute common offset.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.radix_sort import radix_sort
>>> identifiers = [257, -256, 0, 256, -1, 257]
>>> radix_sort(identifiers)
[-256, -1, 0, 256, 257, 257]
>>> assert radix_sort(identifiers) == sorted(identifiers)
>>> offset = 10**80
>>> radix_sort([offset + 2, offset, offset + 1]) == [offset, offset + 1, offset + 2]
True

```

## Boundary to remember

This is an integer algorithm, not a comparison sort for arbitrary records. Extremely wide integers need more byte passes even when the input list is short.
