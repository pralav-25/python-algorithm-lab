# Count unique strings rather than index selections

[Guide index](../README.md) · [Implementation](../../algorithm_lab/count_distinct_subsequences.py)

## Reasoning

Adding a new character can append it to every previously known subsequence, initially doubling the count. If the character appeared before, some resulting strings were already formed from that earlier occurrence. Subtracting its previous contribution removes exactly those duplicate strings.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.count_distinct_subsequences import count_distinct_subsequences
>>> text = 'abab'
>>> strings = {''.join(char for i, char in enumerate(text) if mask & (1 << i)) for mask in range(1 << len(text))}
>>> count_distinct_subsequences(text)
12
>>> assert count_distinct_subsequences(text) == len(strings)
>>> count_distinct_subsequences('aaaa'), count_distinct_subsequences('')
(5, 1)

```

## Boundary to remember

The empty string is included once. Repeated characters distinguish this problem from counting all subsets of positions, which would simply give a power of two.
