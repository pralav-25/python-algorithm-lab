# Explore one branch before returning to alternatives

[Guide index](../README.md) · [Implementation](../../algorithm_lab/depth_first_search.py)

## Reasoning

A stack records vertices waiting to be visited. Pushing neighbors in
reverse order makes the next pop follow the original adjacency order. A visited
set prevents cycles and repeated edges from emitting a vertex twice. The
iterative traversal avoids Python's recursion limit and uses O(V + E) time
and space, including the normalized input snapshot.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.depth_first_search import depth_first_search
>>> graph = {"a": ["b", "c"], "b": ["d", "a"], "c": ["d"], "d": []}
>>> depth_first_search(graph, "a")
['a', 'b', 'd', 'c']
>>> depth_first_search(graph, "d")
['d']
>>> depth_first_search({}, "new")
['new']

```

## Boundary to remember

The result is a visitation order, not a path: consecutive emitted vertices
need not share an edge after the traversal returns to another branch. Edges
remain directed, and an absent starting vertex is treated as isolated. Use
[BFS shortest path](bfs_shortest_path.md) when a shortest route is required.

## Practice exercise

Traverse a folder graph with a shortcut and a back-link. Check that every reachable folder is visited once, then demonstrate why preorder is not a route.

```pycon
>>> from algorithm_lab.depth_first_search import depth_first_search
>>> folders = {"root": ["docs", "src"], "docs": ["draft"], "draft": ["root"], "src": []}
>>> visited = depth_first_search(folders, "root")
>>> visited
['root', 'docs', 'draft', 'src']
>>> assert len(visited) == len(set(visited)) == 4
>>> assert "src" not in folders["draft"]

```

After exploring the draft, DFS resumes at the root's pending source folder. The resulting consecutive preorder entries need not share an edge, so this sequence must not be presented as a navigable path.
