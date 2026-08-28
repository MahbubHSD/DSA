# Leetcode Problem 281: Zigzag Iterator


class ZigzagIterator:
    """Iterate through multiple lists in alternating order."""

    def __init__(self, first, second):
        from collections import deque

        self.queue = deque(deque(values) for values in (first, second) if values)

    def next(self):
        values = self.queue.popleft()
        value = values.popleft()
        if values:
            self.queue.append(values)
        return value

    def has_next(self):
        return bool(self.queue)


if __name__ == "__main__":
    iterator = ZigzagIterator([1, 2], [3, 4, 5, 6])
    print(f"First value: {iterator.next()}")