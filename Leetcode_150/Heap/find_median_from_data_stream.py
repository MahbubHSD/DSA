# Leetcode Problem 295: Find Median from Data Stream


class MedianFinder:
    """Maintain a data stream's median using two heaps."""

    def __init__(self):
        import heapq

        self.lower = []
        self.upper = []
        self.heapq = heapq

    def add_num(self, number):
        self.heapq.heappush(self.lower, -number)
        if self.upper and -self.lower[0] > self.upper[0]:
            value = -self.heapq.heappop(self.lower)
            self.heapq.heappush(self.upper, value)
        if len(self.lower) > len(self.upper) + 1:
            self.heapq.heappush(self.upper, -self.heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            self.heapq.heappush(self.lower, -self.heapq.heappop(self.upper))

    def find_median(self):
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2


if __name__ == "__main__":
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    print(f"Median: {finder.find_median()}")