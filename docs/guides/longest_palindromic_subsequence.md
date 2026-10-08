# Keep a mirror while allowing deleted characters

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_palindromic_subsequence.py)

## Reasoning

For an interval with equal endpoints, those characters can surround a palindromic solution inside it. With unequal endpoints, at least one endpoint must be dropped. Comparing the two smaller intervals yields an optimal length and enough information to reconstruct a palindrome in the original order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_palindromic_subsequence import longest_palindromic_subsequence
>>> text = "character"
>>> answer = longest_palindromic_subsequence(text)
>>> len(answer), answer == answer[::-1]
(5, True)
>>> remaining = iter(text)
>>> assert all(any(item == wanted for item in remaining) for wanted in answer)
>>> longest_palindromic_subsequence("")
''

```

## Boundary to remember

A subsequence may skip characters, unlike a palindromic substring. Equal-length choices drop the right endpoint, so a different implementation may return another equally long witness.

## Practice exercise

Find the minimum number of character deletions needed to make agbdba palindromic. Verify the longest retained palindrome with a small exhaustive oracle.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.longest_palindromic_subsequence import longest_palindromic_subsequence
>>> text = "agbdba"
>>> kept = longest_palindromic_subsequence(text)
>>> kept
'abdba'
>>> subsequences = {
...     "".join(chars) for size in range(len(text) + 1) for chars in combinations(text, size)
... }
>>> palindromes = {part for part in subsequences if part == part[::-1]}
>>> assert kept in palindromes and len(kept) == max(map(len, palindromes))
>>> len(text) - len(kept)
1

```

Deleting g leaves a five-character palindrome without rearranging anything. Every retained palindrome is a subsequence, so maximizing its length minimizes the deletions. A substring search would only see a shorter contiguous mirror and would overestimate the required deletion count.
