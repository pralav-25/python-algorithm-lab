# Maintain a window with no repeated characters

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_unique_substring.py)

## Reasoning

When a character repeats inside the current window, advance the start beyond its previous position. Last-seen indices let that jump skip many characters at once. The start never moves backward, so the full scan is linear rather than restarting a search at every possible start.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_unique_substring import longest_unique_substring
>>> longest_unique_substring('abcaef')
'bcaef'
>>> text = 'dvdf'
>>> answer = longest_unique_substring(text)
>>> answer, len(set(answer)) == len(answer)
('vdf', True)
>>> longest_unique_substring('')
''

```

## Boundary to remember

Character uniqueness means Unicode code-point uniqueness, not visual or case-insensitive equality. Equal-length windows prefer the earliest start.
