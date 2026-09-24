"""Return the index of the first strictly greater value to each position's right.

-1 marks missing neighbors. O(n) comparisons and O(n) space. Values must have a
total order. Equal values are not greater, and input is not modified.

>>> next_greater([2, 2, 1, 3])
[3, 3, 3, -1]
"""


def next_greater(values):
    data = list(values)
    result, stack = [-1] * len(data), []
    for i, value in enumerate(data):
        while stack and data[stack[-1]] < value:
            result[stack.pop()] = i
        stack.append(i)
    return result
