# Share word prefixes while preserving whole-word membership

[Guide index](../README.md) · [Implementation](../../algorithm_lab/trie.py)

## Reasoning

Each edge stores one character and each terminal marker records a complete
word. Common prefixes share nodes, so adding, finding, or deleting a word of
length L takes expected O(L) time. Deletion prunes only unused suffix nodes.
Completion traverses the selected prefix subtree and sorts child edges to
return words in lexicographic order.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.trie import Trie
>>> words = Trie(["", "car", "cart", "cat", "cat"])
>>> len(words), "ca" in words, "" in words
(4, False, True)
>>> words.words("ca", limit=2)
['car', 'cart']
>>> words.discard("car")
True
>>> words.words("ca")
['cart', 'cat']
>>> words.words("missing")
[]

```

## Boundary to remember

A prefix is not automatically a stored word. Duplicate insertions do not
increase size, and the empty string is a valid word. Strings are compared as
Unicode code points without case folding or normalization. Completion cost
includes visited prefixes, sorting, and output text; it is not constant time.
