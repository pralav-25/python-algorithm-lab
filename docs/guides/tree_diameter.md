# Find a longest tree route with two breadth-first searches

[Guide index](../README.md) · [Implementation](../../algorithm_lab/tree_diameter.py)

## Reasoning

Start anywhere in a tree and find a farthest vertex. That vertex is an
endpoint of some diameter. A second breadth-first search from it reaches the
other endpoint, and predecessor pointers reconstruct the route. The unique
path structure of a tree makes the two-search method work in O(V + E) time
and space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.tree_diameter import tree_diameter
>>> graph = {"a": ["b"], "b": ["c"], "c": ["d"]}
>>> route = tree_diameter(graph)
>>> route
['d', 'c', 'b', 'a']
>>> len(route) - 1
3
>>> tree_diameter({"only": []})
['only']
>>> tree_diameter({})
[]

```

## Boundary to remember

The returned value is a vertex path, so its edge length is len(path) - 1
for a nonempty result. Edges are undirected and unweighted; duplicate listings
collapse. Cycles, self-loops, and disconnected graphs are rejected. Ties follow
traversal order rather than a sorted endpoint rule.
