# Evict the entry untouched for the longest time

[Guide index](../README.md) · [Implementation](../../algorithm_lab/lru_cache.py)

## Reasoning

Keep entries ordered from least to most recently used. A successful get
or put moves that key to the newest end. If insertion exceeds capacity, remove
the oldest entry. An ordered dictionary gives expected O(1) lookup and update
with O(capacity) space. Returning an evicted pair makes disposal explicit.

## Worked example

Run these statements from the repository root.

```pycon
>>> from algorithm_lab.lru_cache import LRUCache
>>> cache = LRUCache(2)
>>> cache.put("a", None)
>>> cache.put("b", 2)
>>> cache.get("a") is None
True
>>> cache.put("c", 3)
('b', 2)
>>> cache.items()
[('a', None), ('c', 3)]
>>> cache.put("a", 4)
>>> cache.items()
[('c', 3), ('a', 4)]

```

## Boundary to remember

None is a stored value, not a missing-entry marker; a miss raises KeyError.
Updating a key refreshes recency without growing the cache. items returns a
snapshot list in eviction order, and reading that snapshot does not refresh
entries. Capacity must be a positive integer.
