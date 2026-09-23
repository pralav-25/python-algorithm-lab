"""Internal adjacency normalization shared by unweighted graph algorithms."""

from collections.abc import Hashable, Iterable, Mapping


def normalize_graph(graph: Mapping[Hashable, Iterable[Hashable]], *, undirected=False):
    data = {node: list(neighbors) for node, neighbors in graph.items()}
    for neighbors in list(data.values()):
        for neighbor in neighbors:
            data.setdefault(neighbor, [])
    if undirected:
        for node, neighbors in [(node, list(rows)) for node, rows in data.items()]:
            for neighbor in neighbors:
                data[neighbor].append(node)
    return data
