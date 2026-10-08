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

## Practice exercise

Compare two rearranged tag strings and observe how reversing the argument order changes an equal-length witness. Verify that both answers have the optimal shared length.

```pycon
>>> from algorithm_lab.longest_common_substring import longest_common_substring
>>> first, second = "east-west", "west-east"
>>> forward = longest_common_substring(first, second)
>>> backward = longest_common_substring(second, first)
>>> forward, backward
('east', 'west')
>>> common = {
...     first[start:stop]
...     for start in range(len(first))
...     for stop in range(start + 1, len(first) + 1)
...     if first[start:stop] in second
... }
>>> assert len(forward) == len(backward) == max(map(len, common)) == 4

```

Both tags provide four-character matches, but the earliest occurrence in the first argument determines which one is returned. The optimal length is symmetric even when the actual witness is not. The exhaustive substring set supplies a check that no longer continuous fragment is shared.
