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
