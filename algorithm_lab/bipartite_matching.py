"""Return a mapping from left vertices to distinct matched right vertices.

Input maps left labels to right neighbors; the two sides are separate namespaces
and may share labels. Duplicate edges collapse. Ties follow traversal order.
Iterative augmenting paths take O(L*(V+E)) time, O(V+E) space.

>>> bipartite_matching({'a': [1, 2], 'b': [1]})
{'a': 2, 'b': 1}
"""

from collections import deque


def bipartite_matching(graph):
    data = {left: list(dict.fromkeys(neighbors)) for left, neighbors in graph.items()}
    left_match, right_match = {}, {}
    for root in data:
        queue, seen_left, parent_right = deque([root]), {root}, {}
        found = False
        while queue and not found:
            left = queue.popleft()
            for right in data[left]:
                if right in parent_right:
                    continue
                parent_right[right] = left
                if right not in right_match:
                    found = True
                    break
                next_left = right_match[right]
                if next_left not in seen_left:
                    seen_left.add(next_left)
                    queue.append(next_left)
        if found:
            while True:
                left = parent_right[right]
                previous = left_match.get(left)
                had_previous = left in left_match
                left_match[left], right_match[right] = right, left
                if not had_previous:
                    break
                right = previous
    return left_match
