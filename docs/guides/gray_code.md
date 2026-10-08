# Enumerate bit patterns with one-bit transitions

[Guide index](../README.md) · [Implementation](../../algorithm_lab/gray_code.py)

## Reasoning

Reflecting the previous bit-width sequence and prefixing its two halves constructs a Gray ordering. Equivalently, XOR a binary index with that index shifted right once. Neighboring outputs then differ in exactly one bit, which is useful when a state update should change only one Boolean choice.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.gray_code import gray_code
>>> codes = list(gray_code(3))
>>> codes
[0, 1, 3, 2, 6, 7, 5, 4]
>>> assert sorted(codes) == list(range(8))
>>> assert all((left ^ right).bit_count() == 1 for left, right in zip(codes, codes[1:] + codes[:1]))
>>> list(gray_code(0))
[0]

```

## Boundary to remember

A Gray ordering is not numeric sort order. There are still exponentially many states even though the generator stores only a small amount of working state.

## Practice exercise

Visit every subset of two goods while updating its total weight by changing just one good at a time. Compare the incremental totals with direct subset sums.

```pycon
>>> from algorithm_lab.gray_code import gray_code
>>> weights = [5, 7]
>>> masks = list(gray_code(len(weights)))
>>> total, totals = 0, [0]
>>> for previous, current in zip(masks, masks[1:]):
...     changed = previous ^ current
...     bit = changed.bit_length() - 1
...     total += weights[bit] if current & changed else -weights[bit]
...     totals.append(total)
>>> totals
[0, 5, 12, 7]
>>> assert totals == [sum(w for bit, w in enumerate(weights) if mask & (1 << bit)) for mask in masks]

```

The XOR identifies the one toggled membership bit; its new state decides whether to add or subtract the corresponding weight. This application avoids recomputing each sum from scratch, although enumerating every subset still takes exponential time.
