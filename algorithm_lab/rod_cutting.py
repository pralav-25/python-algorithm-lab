"""Optimal complete rod cutting with a length witness.

prices[i-1] gives an integer price for length i, excluding bool. The rod has
length len(prices) and must be completely sold, even with negative prices.
Return (revenue, piece_lengths), preferring the smallest first cut on ties.
Empty prices returns (0, []). O(n^2) time and O(n) space.

>>> rod_cutting([1, 5, 8, 9])
(10, [2, 2])
"""

from algorithm_lab._validation import integer


def rod_cutting(prices):
    prices = list(prices)
    for price in prices:
        integer(price, "price")
    scores, cuts = [0], [0]
    for length in range(1, len(prices) + 1):
        best, cut = max(
            (prices[size - 1] + scores[length - size], -size) for size in range(1, length + 1)
        )
        scores.append(best)
        cuts.append(-cut)
    remaining, pieces = len(prices), []
    while remaining:
        pieces.append(cuts[remaining])
        remaining -= cuts[remaining]
    return scores[-1], pieces
