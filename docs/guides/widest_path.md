# Maximize the weakest edge along a route

[Guide index](../README.md) · [Implementation](../../algorithm_lab/widest_path.py)

## Reasoning

A route's capacity is its smallest edge capacity. Extending a route
therefore takes min(current capacity, next edge), and competing routes keep
the maximum of those candidates. A priority queue processes the strongest
known bottleneck first. This takes O((V + E) log(V + E)) time and identifies
the best single route for a capacity-constrained transfer.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.widest_path import widest_path
>>> graph = {"s": [("t", 3), ("a", 8)], "a": [("t", 5), ("z", 0)], "island": []}
>>> capacities = widest_path(graph, "s")
>>> capacities["t"], capacities["z"], capacities["island"], capacities["s"]
(5, 0, -1, inf)
>>> widest_path({}, "alone")
{'alone': inf}

```

## Boundary to remember

Zero means a reachable route whose bottleneck is zero; -1 means no route.
The source has infinite capacity for its empty path. All edge capacities must
be finite and nonnegative. This selects a single route's bottleneck;
[maximum flow](max_flow.md) can combine throughput across several routes.
