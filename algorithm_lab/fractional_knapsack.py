"""Maximize value when arbitrary fractions of items can be selected.

items are (positive integer weight, nonnegative integer value); capacity is a
nonnegative integer. Returns (Fraction total_value, fractions in original order).
Density ties use original order; zero-value items are left unselected. O(n log n)
sorts/comparisons and O(n) space, excluding rational-arithmetic bit costs.

>>> fractional_knapsack([(10, 60), (20, 100), (30, 120)], 50)
(Fraction(240, 1), [Fraction(1, 1), Fraction(1, 1), Fraction(2, 3)])
"""

from fractions import Fraction

from algorithm_lab._validation import integer


def fractional_knapsack(items, capacity):
    integer(capacity, "capacity", minimum=0)
    data = [(integer(w, "weight", minimum=1), integer(v, "value", minimum=0)) for w, v in items]
    order = sorted(range(len(data)), key=lambda i: Fraction(data[i][1], data[i][0]), reverse=True)
    fractions = [Fraction(0)] * len(data)
    value = Fraction(0)
    for i in order:
        weight, benefit = data[i]
        if capacity == 0 or benefit == 0:
            break
        taken = min(capacity, weight)
        fractions[i] = Fraction(taken, weight)
        value += fractions[i] * benefit
        capacity -= taken
    return value, fractions
