# Expand around the center of a mirror

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_palindrome.py)

## Reasoning

Every palindrome has either one central character or a central gap. Expanding while the two sides match finds the longest palindrome for each center. Checking both center types avoids losing even-length answers. Earliest-start tie handling makes the chosen substring reproducible.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_palindrome import longest_palindrome
>>> longest_palindrome("xracecary")
'racecar'
>>> longest_palindrome("zabbaq")
'abba'
>>> result = longest_palindrome("noonthenlevel")
>>> assert result == result[::-1] and result in "noonthenlevel"
>>> longest_palindrome("")
''

```

## Boundary to remember

The answer must be contiguous. A longest palindromic subsequence can skip characters and is a separate dynamic-programming problem; center expansion does not solve it.

## Practice exercise

Choose the earliest winner when a text contains two equally long palindromic spans. Verify the choice by listing all palindromic intervals.

```pycon
>>> from algorithm_lab.longest_palindrome import longest_palindrome
>>> text = "rotor#refer"
>>> answer = longest_palindrome(text)
>>> answer
'rotor'
>>> spans = [
...     (start, stop)
...     for start in range(len(text))
...     for stop in range(start + 1, len(text) + 1)
...     if text[start:stop] == text[start:stop][::-1]
... ]
>>> start, stop = min(spans, key=lambda bounds: (-(bounds[1] - bounds[0]), bounds[0]))
>>> assert answer == text[start:stop]
>>> assert len(answer) == 5

```

Both rotor and refer have length five, so merely checking maximal length would miss the tie rule. Ordering candidates by descending length and then ascending start independently verifies the reproducible choice. The differing letters around the separator prevent a longer palindrome spanning both words.
