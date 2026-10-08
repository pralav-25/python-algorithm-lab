# Give frequent symbols shorter prefix codes

[Guide index](../README.md) · [Implementation](../../algorithm_lab/huffman_codes.py)

## Reasoning

Huffman coding repeatedly merges the two least frequent subtrees. Their
leaves gain one bit of depth, while more frequent symbols stay closer to the
root. Marking the two branches 0 and 1 produces a prefix-free binary code with
minimum weighted length. Building the tree takes O(n log n) time; emitting the
code strings also costs their total output length.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.huffman_codes import huffman_codes
>>> weights = {"a": 5, "b": 2, "c": 1}
>>> codes = huffman_codes(weights)
>>> codes
{'c': '00', 'b': '01', 'a': '1'}
>>> sum(weights[symbol] * len(code) for symbol, code in codes.items())
11
>>> all(not right.startswith(left) for a, left in codes.items() for b, right in codes.items() if a != b)
True
>>> huffman_codes({"only": 12})
{'only': '0'}

```

## Boundary to remember

Weights must be positive integers, excluding booleans. Equal weights use
mapping insertion order, and a single symbol receives the nonempty code '0'.
The returned strings are a codebook: this routine does not pack bits or store
the codebook alongside encoded data.

## Practice exercise

Build a codebook for a short message, encode it, and decode the bit string using prefix recognition. Compare the encoded size with a fixed two-bit code for its four symbols.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.huffman_codes import huffman_codes
>>> message = "mississippi"
>>> book = huffman_codes(Counter(message))
>>> encoded = "".join(book[letter] for letter in message)
>>> reverse = {bits: letter for letter, bits in book.items()}
>>> prefix, decoded = "", []
>>> for bit in encoded:
...     prefix += bit
...     if prefix in reverse:
...         decoded.append(reverse[prefix])
...         prefix = ""
>>> "".join(decoded)
'mississippi'
>>> assert prefix == ""
>>> len(encoded), 2 * len(message)
(21, 22)

```

A prefix-free code lets the decoder emit a symbol as soon as its complete code appears; it never needs to guess a longer interpretation. The one-bit saving counts payload only. A real file must also describe the codebook and account for byte packing.
