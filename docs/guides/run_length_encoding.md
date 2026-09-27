# Compress runs without ambiguous digit parsing

[Guide index](../README.md) · [Implementation](../../algorithm_lab/run_length_encoding.py)

## Reasoning

Run-length encoding records a symbol with the number of times it repeats consecutively. Structured (symbol, count) pairs let digits and Unicode symbols remain ordinary data rather than part of an ambiguous text format. The benefit depends on long runs; alternating symbols can require more representation space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.run_length_encoding import encode_runs, decode_runs
>>> text = "11100🙂🙂🙂"
>>> runs = encode_runs(text)
>>> runs
[('1', 3), ('0', 2), ('🙂', 3)]
>>> assert decode_runs(runs) == text
>>> decode_runs([], max_output=0)
''

```

## Boundary to remember

Decoding is proportional to expanded output size, not encoded size. The max_output limit protects against a tiny run list requesting an enormous allocation.
