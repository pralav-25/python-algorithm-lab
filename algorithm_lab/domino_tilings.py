"""Count tilings of a 2-by-n rectangle with unlabelled 2-by-1 dominoes.

Width n must be a nonnegative integer; bool is rejected. Dominoes may be
horizontal or vertical, without overlap or holes. Width zero has one empty
tiling. Return an exact integer, counting all arrangements; ties need no
selection. O(n) time and O(1) integer slots, excluding arithmetic and integer
bit storage. No input mutation.

>>> domino_tilings(4)
5
"""

from algorithm_lab._validation import integer


def domino_tilings(n: int) -> int:
    integer(n, "width", minimum=0)
    previous, current = 1, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
