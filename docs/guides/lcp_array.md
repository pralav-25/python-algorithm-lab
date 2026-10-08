# Measure shared prefixes between neighboring suffixes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/lcp_array.py)

## Reasoning

Lexicographically adjacent suffixes reveal repeated fragments through their longest common prefix. Kasai’s scan uses the fact that removing a leading character shortens a known common prefix by at most one, so it can reuse work while visiting text positions rather than suffix order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.suffix_array import suffix_array
>>> from algorithm_lab.lcp_array import lcp_array
>>> text = "caba"
>>> order = suffix_array(text)
>>> lcp_array(text, order)
[0, 1, 0, 0]
>>> lcp_array("aaaa", suffix_array("aaaa"))
[0, 1, 2, 3]
>>> lcp_array("", [])
[]

```

## Boundary to remember

A valid suffix-array permutation is not enough: it must also be lexicographically sorted. The routine checks the permutation shape but relies on correct ordering as a precondition.

## Practice exercise

Use adjacent-suffix prefix lengths to count distinct nonempty substrings, then verify the count by explicitly collecting every substring of a short text.

```pycon
>>> from algorithm_lab.suffix_array import suffix_array
>>> from algorithm_lab.lcp_array import lcp_array
>>> text = "ababa"
>>> lengths = lcp_array(text, suffix_array(text))
>>> lengths
[0, 1, 3, 0, 2]
>>> distinct_count = len(text) * (len(text) + 1) // 2 - sum(lengths)
>>> distinct_count
9
>>> explicit = {
...     text[start:stop] for start in range(len(text)) for stop in range(start + 1, len(text) + 1)
... }
>>> assert distinct_count == len(explicit)

```

A suffix contributes all its prefixes except those already shared with its lexicographic predecessor. There are fifteen substring positions before accounting for duplication; the six shared-prefix contributions reduce that to nine distinct strings. The explicit set uses direct slicing rather than suffix-array reasoning.
