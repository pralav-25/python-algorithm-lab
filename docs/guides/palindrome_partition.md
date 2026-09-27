# Use the fewest palindromic pieces

[Guide index](../README.md) · [Implementation](../../algorithm_lab/palindrome_partition.py)

## Reasoning

First identify which substrings are palindromes. Then, for each prefix endpoint, try every final palindromic piece and add one to the best partition of what precedes it. Predecessor boundaries recover the chosen pieces after the minimum count is known.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.palindrome_partition import palindrome_partition
>>> text = 'aabcc'
>>> pieces = palindrome_partition(text)
>>> pieces
['aa', 'b', 'cc']
>>> assert ''.join(pieces) == text and all(piece == piece[::-1] for piece in pieces)
>>> palindrome_partition('radar')
['radar']
>>> palindrome_partition('')
[]

```

## Boundary to remember

The objective is the number of pieces, not their individual lengths. Taking the longest available palindrome greedily can miss a better complete partition.
