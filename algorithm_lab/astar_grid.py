"""Find a shortest four-neighbor path on a rectangular binary grid, or None.

0/False means open; 1/True means blocked. Coordinates are (row, column). Invalid
shapes, cells, or coordinates raise ValueError; blocked endpoints return None.
Manhattan distance is admissible for unit moves. Time O(V log V), space O(V).
Ties are deterministic by cost then coordinates; inputs are not changed.

>>> astar_grid([[0, 0], [1, 0]], (0, 0), (1, 1))
[(0, 0), (0, 1), (1, 1)]
"""

import heapq


def astar_grid(grid, start, goal):
    if not grid or not grid[0] or any(len(row) != len(grid[0]) for row in grid):
        raise ValueError("grid must be a nonempty rectangle")
    if any(type(cell) not in (int, bool) or cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("grid cells must be 0 or 1")
    rows, columns = len(grid), len(grid[0])

    def position(pair):
        try:
            row, column = pair
        except (TypeError, ValueError) as exc:
            raise ValueError("coordinates must contain two integers") from exc
        if (
            any(isinstance(x, bool) or not isinstance(x, int) for x in (row, column))
            or not 0 <= row < rows
            or not 0 <= column < columns
        ):
            raise ValueError("coordinate is outside the grid")
        return row, column

    start, goal = position(start), position(goal)
    if grid[start[0]][start[1]] or grid[goal[0]][goal[1]]:
        return None

    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    queue, distances, previous = [(heuristic(start), 0, start)], {start: 0}, {}
    while queue:
        _, distance, node = heapq.heappop(queue)
        if distance != distances[node]:
            continue
        if node == goal:
            result = [node]
            while node in previous:
                node = previous[node]
                result.append(node)
            return result[::-1]
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            child = node[0] + dr, node[1] + dc
            r, c = child
            if not 0 <= r < rows or not 0 <= c < columns or grid[r][c]:
                continue
            candidate = distance + 1
            if child not in distances or candidate < distances[child]:
                distances[child], previous[child] = candidate, node
                heapq.heappush(queue, (candidate + heuristic(child), candidate, child))
    return None
