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
