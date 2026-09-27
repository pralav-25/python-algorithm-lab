# Measure shared prefixes between neighboring suffixes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/lcp_array.py)

## Reasoning

Lexicographically adjacent suffixes reveal repeated fragments through their longest common prefix. Kasai’s scan uses the fact that removing a leading character shortens a known common prefix by at most one, so it can reuse work while visiting text positions rather than suffix order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.suffix_array import suffix_array
>>> from algorithm_lab.lcp_array import lcp_array
>>> text = 'caba'
>>> order = suffix_array(text)
>>> lcp_array(text, order)
[0, 1, 0, 0]
>>> lcp_array('aaaa', suffix_array('aaaa'))
[0, 1, 2, 3]
>>> lcp_array('', [])
[]

```

## Boundary to remember

A valid suffix-array permutation is not enough: it must also be lexicographically sorted. The routine checks the permutation shape but relies on correct ordering as a precondition.
