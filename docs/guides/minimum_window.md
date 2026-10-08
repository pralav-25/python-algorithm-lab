# Cover a required multiset in the shortest span

[Guide index](../README.md) · [Implementation](../../algorithm_lab/minimum_window.py)

## Reasoning

Grow a window until every required character count is satisfied, then shrink its left edge while coverage remains valid. A count of unmet requirements distinguishes useful additions from surplus copies. Both boundaries move only forward, so even repeated characters can be handled in linear expected time.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.minimum_window import minimum_window
>>> minimum_window("AAABBC", "AABC")
'AABBC'
>>> from collections import Counter
>>> result = minimum_window("CABABAC", "AABC")
>>> assert not (Counter("AABC") - Counter(result))
>>> minimum_window("abc", "zz")
''
>>> minimum_window("abc", "")
''

```

## Boundary to remember

Requirements are a multiset: requiring two A characters cannot be satisfied by one A. An empty result may mean an empty requirement or that no covering window exists.

## Practice exercise

Find the earliest shortest window for repeated Unicode code points,
then check it against all substrings of a short text.

```pycon
>>> from algorithm_lab.minimum_window import minimum_window
>>> from collections import Counter
>>> text, required = "αββαγβαβ", "αββ"
>>> answer = minimum_window(text, required)
>>> answer
'αββ'
>>> covers = [
...     (j - i, i, text[i:j])
...     for i in range(len(text))
...     for j in range(i + 1, len(text) + 1)
...     if not (Counter(required) - Counter(text[i:j]))
... ]
>>> assert answer == min(covers)[2]

```

One beta is insufficient even though all distinct required characters
would be present. Python string indices count code points, and an equal
length later window must not replace the earliest valid one.
