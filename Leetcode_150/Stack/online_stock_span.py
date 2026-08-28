# Leetcode Problem 901: Online Stock Span


class StockSpanner:
    """Return the consecutive span of each incoming stock price."""

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


if __name__ == "__main__":
    spanner = StockSpanner()
    print(f"Stock span: {spanner.next(100)}")