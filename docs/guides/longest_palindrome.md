# Expand around the center of a mirror

[Guide index](../README.md) · [Implementation](../../algorithm_lab/longest_palindrome.py)

## Reasoning

Every palindrome has either one central character or a central gap. Expanding while the two sides match finds the longest palindrome for each center. Checking both center types avoids losing even-length answers. Earliest-start tie handling makes the chosen substring reproducible.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.longest_palindrome import longest_palindrome
>>> longest_palindrome('xracecary')
'racecar'
>>> longest_palindrome('zabbaq')
'abba'
>>> result = longest_palindrome('noonthenlevel')
>>> assert result == result[::-1] and result in 'noonthenlevel'
>>> longest_palindrome('')
''

```

## Boundary to remember

The answer must be contiguous. A longest palindromic subsequence can skip characters and is a separate dynamic-programming problem; center expansion does not solve it.
