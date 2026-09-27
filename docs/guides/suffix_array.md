# Index suffixes without storing every substring

[Guide index](../README.md) · [Implementation](../../algorithm_lab/suffix_array.py)

## Reasoning

Sort suffixes by short prefix ranks, then double the prefix length and sort pairs of ranks. Once ranks distinguish all suffixes, their order represents the lexicographic order of complete suffix strings. The index stores positions rather than the quadratic collection of copied suffix strings.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.suffix_array import suffix_array
>>> text = "caba"
>>> order = suffix_array(text)
>>> [text[i:] for i in order]
['a', 'aba', 'ba', 'caba']
>>> assert order == sorted(range(len(text)), key=lambda i: text[i:])
>>> suffix_array("")
[]

```

## Boundary to remember

The empty suffix is not included. Ordering follows Python Unicode code points, which differs from locale-aware dictionary ordering and does not normalize equivalent-looking strings.
