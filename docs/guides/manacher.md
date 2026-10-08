# Reuse mirrored palindrome radii

[Guide index](../README.md) · [Implementation](../../algorithm_lab/manacher.py)

## Reasoning

Inside a known palindrome, a position and its mirror share a guaranteed matching radius until the enclosing boundary is reached. Manacher’s algorithm starts from that guaranteed radius and compares only what remains unknown. Separate odd and even radius arrays avoid inserting reserved separator characters into the input.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.manacher import manacher
>>> manacher("xabccbay")
'abccba'
>>> manacher("a#b#b#a")
'a#b#b#a'
>>> text = "levelxnoon"
>>> answer = manacher(text)
>>> assert answer == "level" and answer == answer[::-1]
>>> manacher("")
''

```

## Boundary to remember

The algorithm finds a contiguous substring, with earliest-start ties. Its linear running time requires extra radius arrays, trading space for the faster bound compared with simple center expansion.

## Practice exercise

Find a palindrome containing null code points and punctuation. Verify its length by direct substring reversal so no reserved-separator assumption can slip into the result.

```pycon
>>> from algorithm_lab.manacher import manacher
>>> text = "\x00a##a\x00|noon"
>>> answer = manacher(text)
>>> assert answer == "\x00a##a\x00"
>>> len(answer)
6
>>> candidates = [
...     text[start:stop]
...     for start in range(len(text))
...     for stop in range(start + 1, len(text) + 1)
...     if text[start:stop] == text[start:stop][::-1]
... ]
>>> assert len(answer) == max(map(len, candidates))

```

The null code point and hash characters are ordinary input characters. Separate odd and even radius arrays avoid treating either as a synthetic delimiter. The winning span has an even center between the two hashes, while the competing noon span is shorter.
