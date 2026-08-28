# Leetcode Problem 981: Time Based Key-Value Store


class TimeMap:
    """Store values by key and retrieve the latest value at a timestamp."""

    def __init__(self):
        self.values = {}

    def set(self, key, value, timestamp):
        self.values.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        entries = self.values.get(key, [])
        left, right = 0, len(entries) - 1
        result = ""
        while left <= right:
            middle = (left + right) // 2
            if entries[middle][0] <= timestamp:
                result = entries[middle][1]
                left = middle + 1
            else:
                right = middle - 1
        return result


if __name__ == "__main__":
    store = TimeMap()
    store.set("foo", "bar", 1)
    print(f"Stored value: {store.get('foo', 1)}")