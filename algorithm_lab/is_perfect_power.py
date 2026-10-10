"""Decide whether n=a**b for integers a>=2 and b>=2.

n is an integer >1 excluding bool. Return a bool, without choosing among tied
representations. Binary searches for each possible exponent use O(log(n)**2)
integer power comparisons and O(1) integers of storage; power and big-integer
costs are additional. All comparisons are exact, with no floating-point roots.

>>> is_perfect_power(81)
True
>>> is_perfect_power(82)
False
"""

from algorithm_lab._validation import integer


def is_perfect_power(n):
    integer(n, "n", minimum=2)
    bits = n.bit_length()
    for exponent in range(2, bits):
        low, high = 2, 1 << ((bits + exponent - 1) // exponent)
        while low <= high:
            middle = (low + high) // 2
            power = middle**exponent
            if power == n:
                return True
            if power < n:
                low = middle + 1
            else:
                high = middle - 1
    return False
