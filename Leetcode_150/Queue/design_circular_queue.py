# Leetcode Problem 622: Design Circular Queue


class MyCircularQueue:
    """Fixed-size FIFO queue backed by a circular array."""

    def __init__(self, capacity):
        self.values = [0] * capacity
        self.front_index = 0
        self.size = 0

    def en_queue(self, value):
        if self.is_full():
            return False
        index = (self.front_index + self.size) % len(self.values)
        self.values[index] = value
        self.size += 1
        return True

    def de_queue(self):
        if self.is_empty():
            return False
        self.front_index = (self.front_index + 1) % len(self.values)
        self.size -= 1
        return True

    def front(self):
        return -1 if self.is_empty() else self.values[self.front_index]

    def rear(self):
        if self.is_empty():
            return -1
        return self.values[(self.front_index + self.size - 1) % len(self.values)]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.values)


if __name__ == "__main__":
    queue = MyCircularQueue(3)
    queue.en_queue(1)
    queue.en_queue(2)
    print(f"Queue rear: {queue.rear()}")