# Segment text using the fewest dictionary words

[Guide index](../README.md) · [Implementation](../../algorithm_lab/word_break.py)

## Reasoning

At each text endpoint, consider dictionary words that could end there and combine them with the best segmentation of the preceding prefix. Storing the best word count and predecessor boundary reconstructs an optimal segmentation, including cases where greedily taking the longest first word gets stuck.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.word_break import word_break
>>> dictionary = ['cats', 'cat', 'sand', 'dog', 'catsand']
>>> pieces = word_break('catsanddog', dictionary)
>>> pieces
['catsand', 'dog']
>>> assert ''.join(pieces) == 'catsanddog' and all(piece in dictionary for piece in pieces)
>>> word_break('bird', dictionary) is None
True
>>> word_break('', dictionary)
[]

```

## Boundary to remember

Dictionary words are exact nonempty strings, with no automatic case folding. None means segmentation is impossible, while [] is the valid segmentation of empty text.
