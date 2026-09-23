"""A Unicode word set backed by a trie, including the empty word.

Add, membership, and discard take O(L) expected time. Completions are iterative,
sort child edges, and construct visited prefixes; their cost includes that text.
Returned words use Python's lexicographic order. No normalization is performed.

>>> words = Trie(['car', 'cat', 'cat', 'dog'])
>>> words.words('ca')
['car', 'cat']
>>> words.discard('car')
True
"""

from collections.abc import Iterable


class Trie:
    def __init__(self, words: Iterable[str] = ()):
        self._root = {}
        self._size = 0
        for word in words:
            self.add(word)

    def __len__(self) -> int:
        return self._size

    def _node(self, word: str):
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        node = self._root
        for char in word:
            if char not in node:
                return None
            node = node[char]
        return node

    def __contains__(self, word: str) -> bool:
        node = self._node(word)
        return node is not None and "" in node

    def add(self, word: str) -> None:
        if not isinstance(word, str):
            raise TypeError("word must be a string")
        node = self._root
        for char in word:
            node = node.setdefault(char, {})
        if "" not in node:
            node[""] = True
            self._size += 1

    def discard(self, word: str) -> bool:
        if word not in self:
            return False
        node, parents = self._root, []
        for char in word:
            parents.append((node, char))
            node = node[char]
        del node[""]
        self._size -= 1
        for parent, char in reversed(parents):
            if parent[char]:
                break
            del parent[char]
        return True

    def words(self, prefix: str = "", *, limit: int | None = None) -> list[str]:
        if limit is not None and (
            isinstance(limit, bool) or not isinstance(limit, int) or limit < 0
        ):
            raise ValueError("limit must be a nonnegative integer or None")
        node = self._node(prefix)
        if node is None or limit == 0:
            return []
        stack, result = [(node, prefix)], []
        while stack:
            node, word = stack.pop()
            if "" in node:
                result.append(word)
                if limit is not None and len(result) >= limit:
                    break
            stack.extend(
                (node[char], word + char)
                for char in sorted((key for key in node if key), reverse=True)
            )
        return result
