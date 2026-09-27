# Group words by character multiplicity

[Guide index](../README.md) · [Implementation](../../algorithm_lab/anagram_groups.py)

## Reasoning

Sorting a word’s characters creates a signature shared by exactly those words with the same character counts. Mapping each signature to its first-created group preserves group arrival order and the original order within a group. Repeated input words remain repeated records.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.anagram_groups import anagram_groups
>>> anagram_groups(['stop', 'pots', 'tops', 'spot', 'cat'])
[['stop', 'pots', 'tops', 'spot'], ['cat']]
>>> anagram_groups(['ab', 'aab', 'ba', 'ab'])
[['ab', 'ba', 'ab'], ['aab']]
>>> anagram_groups(['', ''])
[['', '']]
>>> anagram_groups([])
[]

```

## Boundary to remember

A set of characters is not a sufficient signature: it loses repeated-letter counts. Matching is case-sensitive and performs no Unicode normalization.
