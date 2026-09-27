# Keep shared content while allowing skipped characters

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_common_subsequence.py)

## Reasoning

Matching final characters can extend a shared subsequence of shorter prefixes. Otherwise, dropping a character from one side or the other leaves two smaller candidate problems. The length table guides traceback to a witness that appears in both inputs in order, even when there are gaps.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_common_subsequence import longest_common_subsequence
>>> longest_common_subsequence("AXBYCZ", "ABC")
'ABC'
>>> answer = longest_common_subsequence("schedule", "school")
>>> def is_subsequence(part, whole):
...     items = iter(whole)
...     return all(any(value == wanted for value in items) for wanted in part)
>>> assert is_subsequence(answer, "schedule") and is_subsequence(answer, "school")
>>> longest_common_subsequence("", "ABC")
''

```

## Boundary to remember

Subsequences need not be contiguous. Equal-length traceback choices can yield different valid answers across implementations, so test witness validity and optimal length when a unique answer is not guaranteed.
