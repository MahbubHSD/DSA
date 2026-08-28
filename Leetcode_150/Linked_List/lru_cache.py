# Leetcode Problem 146: LRU Cache


class LRUCache:
    """Least-recently-used cache with bounded capacity."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.values = {}

    def get(self, key):
        if key not in self.values:
            return -1
        value = self.values.pop(key)
        self.values[key] = value
        return value

    def put(self, key, value):
        if key in self.values:
            self.values.pop(key)
        self.values[key] = value
        if len(self.values) > self.capacity:
            self.values.pop(next(iter(self.values)))


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"Cached value: {cache.get(1)}")