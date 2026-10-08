# Allow one adjacent-character transposition

[Guide index](../README.md) · [Implementation](../../algorithm_lab/optimal_string_alignment.py)

## Reasoning

Alongside insertions, deletions, and substitutions, the recurrence can recognize two adjacent characters in reversed order. Jumping back two positions charges one transposition. This gives a useful spelling-distance model while keeping a straightforward dynamic-programming table.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.optimal_string_alignment import optimal_string_alignment
>>> from algorithm_lab.levenshtein import levenshtein
>>> optimal_string_alignment("form", "from")
1
>>> levenshtein("form", "from")
2
>>> optimal_string_alignment("CA", "ABC")
3
>>> optimal_string_alignment("", "abc")
3

```

## Boundary to remember

Optimal string alignment restricts repeated edits to the same substring. It is not unrestricted Damerau–Levenshtein distance; that distinction can change scores and metric properties.

## Practice exercise

Score two separate adjacent swaps and compare them with a single swap
in the same four-character word.

```pycon
>>> from algorithm_lab.optimal_string_alignment import optimal_string_alignment
>>> optimal_string_alignment("abcd", "badc")
2
>>> optimal_string_alignment("abcd", "abdc")
1
>>> assert optimal_string_alignment("badc", "abcd") == 2
>>> assert optimal_string_alignment("aab", "aba") == 1

```

The `ab` and `cd` transpositions edit disjoint pairs, so both can be used.
Repeated characters still permit an adjacent swap, but these examples
do not imply support for repeatedly editing an overlapping substring.
