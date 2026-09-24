"""Return each integer position's product excluding itself, without division.

O(n) multiplications, O(n) output space. Empty returns []; singleton returns [1].
Zeros and negative integers are supported. Integer arithmetic cost depends on
operand size; booleans/non-integers raise ValueError.

>>> product_except_self([2, 0, 4])
[0, 8, 0]
"""

from algorithm_lab._validation import integer


def product_except_self(values):
    data = [integer(value) for value in values]
    output = [1] * len(data)
    prefix = 1
    for i, value in enumerate(data):
        output[i] = prefix
        prefix *= value
    suffix = 1
    for i in range(len(data) - 1, -1, -1):
        output[i] *= suffix
        suffix *= data[i]
    return output
