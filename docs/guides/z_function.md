# Reuse a prefix-match window across a string

[Guide index](../README.md) · [Implementation](../../algorithm_lab/z_function.py)

## Reasoning

The Z value at a position measures how much of the whole string’s prefix starts there. A known matching interval lets later positions reuse earlier Z values until they reach its right boundary; only fresh characters beyond that boundary need comparison. This avoids rescanning long repeated prefixes.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.z_function import z_function
>>> z_function("ababx")
[0, 0, 2, 0, 0]
>>> text = "aaabaaab"
>>> values = z_function(text)
>>> assert all(text[:length] == text[i : i + length] for i, length in enumerate(values))
>>> z_function("")
[]

```

## Boundary to remember

This implementation defines Z[0] as zero, whereas some references use the full string length. Do not mix those conventions when comparing arrays or constructing downstream formulas.
