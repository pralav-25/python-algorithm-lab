"""Compute LCP with each suffix's lexicographic predecessor; first entry is zero.

O(n) time and space given a correct suffix array, which must be a permutation
of 0..len(text)-1 in lexicographic suffix order. Permutation shape is checked;
lexicographic ordering is a precondition. Empty text/array returns [].

>>> lcp_array('banana', [5, 3, 1, 0, 4, 2])
[0, 1, 3, 0, 0, 2]
"""

from algorithm_lab._validation import index


def lcp_array(text, suffixes):
    order = list(suffixes)
    n = len(text)
    if len(order) != n:
        raise ValueError("suffix array must contain every offset")
    for position in order:
        index(position, n)
    if len(set(order)) != n:
        raise ValueError("suffix array must be a permutation")
    ranks = [0] * n
    for rank, position in enumerate(order):
        ranks[position] = rank
    result, length = [0] * n, 0
    for i in range(n):
        rank = ranks[i]
        if rank == 0:
            length = 0
            continue
        j = order[rank - 1]
        while i + length < n and j + length < n and text[i + length] == text[j + length]:
            length += 1
        result[rank] = length
        length = max(0, length - 1)
    return result
