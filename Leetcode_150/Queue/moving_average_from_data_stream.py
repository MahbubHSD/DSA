# Leetcode Problem 346: Moving Average from Data Stream


class MovingAverage:
    """Calculate a fixed-size moving average of a data stream."""

    def __init__(self, size):
        from collections import deque

        self.size = size
        self.values = deque()
        self.total = 0

    def next(self, value):
        self.values.append(value)
        self.total += value
        if len(self.values) > self.size:
            self.total -= self.values.popleft()
        return self.total / len(self.values)


if __name__ == "__main__":
    average = MovingAverage(3)
    print(f"Moving average: {average.next(1)}")