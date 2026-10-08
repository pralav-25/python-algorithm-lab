# Traverse every directed edge exactly once

[Guide index](../README.md) · [Implementation](../../algorithm_lab/eulerian_trail.py)

## Reasoning

Hierholzer's algorithm follows unused edges until it cannot continue,
then adds vertices to the route while unwinding. Reversing that accumulated
route splices the traversals into one trail. Degree checks choose an appropriate
start, and the final edge count detects disconnected edge-bearing components.
The complete procedure takes O(V + E) time and space.

## Worked example

Run these statements from the repository root.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.eulerian_trail import eulerian_trail
>>> graph = {"a": ["b", "b"], "b": ["a"], "alone": []}
>>> route = eulerian_trail(graph)
>>> route
['a', 'b', 'a', 'b']
>>> Counter(zip(route, route[1:])) == Counter([("a", "b"), ("a", "b"), ("b", "a")])
True
>>> eulerian_trail({"alone": []})
[]

```

## Boundary to remember

Parallel edges and self-loops are real edges and must all be consumed.
Isolated vertices do not prevent a trail. With no edges the answer is empty;
incompatible degrees or disconnected edges raise ValueError. No particular
valid trail is promised when several exist.

## Practice exercise

A message trace must consume a self-delivery and a round trip exactly once. Check the returned trace by counting transitions rather than choosing one valid order.

```pycon
>>> from collections import Counter
>>> from algorithm_lab.eulerian_trail import eulerian_trail
>>> deliveries = {"a": ["a", "b"], "b": ["a"]}
>>> trace = eulerian_trail(deliveries)
>>> consumed = Counter(zip(trace, trace[1:]))
>>> expected = Counter(
...     (sender, receiver) for sender, receivers in deliveries.items() for receiver in receivers
... )
>>> assert consumed == expected
>>> assert len(trace) == 4 and trace[0] == trace[-1]

```

A self-loop counts as one real directed edge. Transition multisets preserve both loop identity and edge multiplicity, whereas a set of visited vertices would not prove that every delivery was consumed exactly once.
