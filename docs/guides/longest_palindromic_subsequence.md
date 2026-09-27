# Keep a mirror while allowing deleted characters

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_palindromic_subsequence.py)

## Reasoning

For an interval with equal endpoints, those characters can surround a palindromic solution inside it. With unequal endpoints, at least one endpoint must be dropped. Comparing the two smaller intervals yields an optimal length and enough information to reconstruct a palindrome in the original order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_palindromic_subsequence import longest_palindromic_subsequence
>>> text = 'character'
>>> answer = longest_palindromic_subsequence(text)
>>> len(answer), answer == answer[::-1]
(5, True)
>>> remaining = iter(text)
>>> assert all(any(item == wanted for item in remaining) for wanted in answer)
>>> longest_palindromic_subsequence('')
''

```

## Boundary to remember

A subsequence may skip characters, unlike a palindromic substring. Equal-length choices drop the right endpoint, so a different implementation may return another equally long witness.
