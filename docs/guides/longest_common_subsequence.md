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

## Practice exercise

Find how many insertion and deletion edits are needed to reconcile two character-order revisions. Independently enumerate their shared subsequences to verify the kept length.

```pycon
>>> from itertools import combinations
>>> from algorithm_lab.longest_common_subsequence import longest_common_subsequence
>>> old, new = "CABD", "ACBD"
>>> kept = longest_common_subsequence(old, new)
>>> def subsequences(text):
...     return {"".join(chars) for size in range(len(text) + 1) for chars in combinations(text, size)}
>>> shared = subsequences(old) & subsequences(new)
>>> assert kept in shared
>>> assert len(kept) == max(map(len, shared)) == 3
>>> len(old) + len(new) - 2 * len(kept)
2

```

Keep the common three-character subsequence, delete the one unmatched old character, and insert the unmatched new character. A longer shared witness would reduce this cost, but the exhaustive set rules one out. This metric counts substitutions as a deletion plus an insertion.
