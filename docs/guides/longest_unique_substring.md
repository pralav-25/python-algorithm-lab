# Maintain a window with no repeated characters

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_unique_substring.py)

## Reasoning

When a character repeats inside the current window, advance the start beyond its previous position. Last-seen indices let that jump skip many characters at once. The start never moves backward, so the full scan is linear rather than restarting a search at every possible start.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_unique_substring import longest_unique_substring
>>> longest_unique_substring("abcaef")
'bcaef'
>>> text = "dvdf"
>>> answer = longest_unique_substring(text)
>>> answer, len(set(answer)) == len(answer)
('vdf', True)
>>> longest_unique_substring("")
''

```

## Boundary to remember

Character uniqueness means Unicode code-point uniqueness, not visual or case-insensitive equality. Equal-length windows prefer the earliest start.

## Practice exercise

Handle a repeated character whose previous occurrence has already left the active window. Verify the winning span by enumerating all unique-character substrings.

```pycon
>>> from algorithm_lab.longest_unique_substring import longest_unique_substring
>>> text = "tmmzuxt"
>>> answer = longest_unique_substring(text)
>>> answer
'mzuxt'
>>> spans = [
...     (start, stop)
...     for start in range(len(text))
...     for stop in range(start + 1, len(text) + 1)
...     if len(set(text[start:stop])) == stop - start
... ]
>>> start, stop = min(spans, key=lambda bounds: (-(bounds[1] - bounds[0]), bounds[0]))
>>> assert answer == text[start:stop] and len(answer) == 5

```

The second m advances the window start to position 2. When the final t appears, its earlier copy at position 0 is outside that window and should not shorten or move the window backward. Taking the maximum of the old start and the last-seen boundary preserves this invariant.
