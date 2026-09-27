# Find an uninterrupted shared text fragment

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_common_substring.py)

## Reasoning

A matching character extends the common suffix ending at the previous pair of positions. A mismatch resets that suffix length to zero, because a substring cannot skip characters. Remembering the largest suffix length and its endpoint reconstructs the best contiguous match with only rolling rows.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_common_substring import longest_common_substring
>>> longest_common_substring("pre-token-post", "a-token-b")
'-token-'
>>> fragment = longest_common_substring("ABXCD", "ABYCD")
>>> fragment
'AB'
>>> assert fragment in "ABXCD" and fragment in "ABYCD"
>>> longest_common_substring("abc", "XYZ")
''

```

## Boundary to remember

A subsequence algorithm would allow gaps and can return a longer but invalid answer for this task. Ties here prefer the earliest starting position in the first string.
