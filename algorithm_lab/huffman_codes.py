"""Optimal binary prefix codes for a mapping of symbols to positive integer weights.

Symbols are arbitrary hashable objects; weights exclude bool. Equal weights are
resolved by insertion order, with newly merged nodes placed after existing nodes.
Empty input returns {}; a single symbol receives '0'. Building the tree costs
O(n log n); emitting codes costs O(total output length), with the same output
space plus O(n) tree space. Traversal is iterative.

>>> huffman_codes({'a': 5, 'b': 2, 'c': 1})
{'c': '00', 'b': '01', 'a': '1'}
"""

import heapq
from itertools import count

from algorithm_lab._validation import integer


def huffman_codes(frequencies):
    serial, queue = count(), []
    for symbol, weight in frequencies.items():
        integer(weight, "weight", minimum=1)
        queue.append((weight, next(serial), (symbol, None, None)))
    heapq.heapify(queue)
    if not queue:
        return {}
    while len(queue) > 1:
        first, _, left = heapq.heappop(queue)
        second, _, right = heapq.heappop(queue)
        heapq.heappush(queue, (first + second, next(serial), (None, left, right)))
    stack, codes = [(queue[0][2], "")], {}
    while stack:
        (symbol, left, right), prefix = stack.pop()
        if left is None:
            codes[symbol] = prefix or "0"
        else:
            stack.append((right, prefix + "1"))
            stack.append((left, prefix + "0"))
    return codes
