import random
import unittest

from algorithm_lab.lru_cache import LRUCache


class LRUTests(unittest.TestCase):
    def test_against_list_model(self):
        rng = random.Random(113)
        cache, model = LRUCache(4), []
        for _ in range(200):
            key = rng.randrange(8)
            keys = [k for k, _ in model]
            if rng.randrange(2):
                value = rng.choice([None, 0, 3])
                if key in keys:
                    model.pop(keys.index(key))
                model.append((key, value))
                evicted = model.pop(0) if len(model) > 4 else None
                self.assertEqual(cache.put(key, value), evicted)
            elif key in keys:
                row = model.pop(keys.index(key))
                model.append(row)
                self.assertEqual(cache.get(key), row[1])
            else:
                with self.assertRaises(KeyError):
                    cache.get(key)
            self.assertEqual(cache.items(), model)
            self.assertEqual(len(cache), len(model))

    def test_capacity(self):
        for capacity in [0, -1, True, 1.5]:
            with self.assertRaises(ValueError):
                LRUCache(capacity)

    def test_items_snapshot_does_not_mutate_entries_or_refresh_recency(self):
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        snapshot = cache.items()
        snapshot.reverse()
        snapshot.append(("injected", 3))
        self.assertEqual(cache.items(), [("a", 1), ("b", 2)])
        self.assertEqual(cache.put("c", 3), ("a", 1))
        self.assertEqual(snapshot, [("b", 2), ("a", 1), ("injected", 3)])

    def test_missing_get_leaves_eviction_order_unchanged(self):
        cache = LRUCache(2)
        cache.put(None, None)
        cache.put("b", 2)
        for key in ("missing", 7, ("absent",)):
            with self.assertRaises(KeyError):
                cache.get(key)
            self.assertEqual(cache.items(), [(None, None), ("b", 2)])
        self.assertEqual(cache.put("c", 3), (None, None))

    def test_capacity_one_update_does_not_evict_itself(self):
        cache = LRUCache(1)
        self.assertIsNone(cache.put("key", 1))
        self.assertIsNone(cache.put("key", None))
        self.assertEqual(len(cache), 1)
        self.assertIsNone(cache.get("key"))
        self.assertEqual(cache.put("new", 2), ("key", None))
