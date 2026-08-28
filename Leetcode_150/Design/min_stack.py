# Leetcode Problem 155: Min Stack


class MinStack:
    """Stack supporting constant-time minimum lookup."""

    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, value):
        self.values.append(value)
        current_minimum = min(value, self.minimums[-1]) if self.minimums else value
        self.minimums.append(current_minimum)

    def pop(self):
        self.minimums.pop()
        return self.values.pop()

    def top(self):
        return self.values[-1]

    def get_min(self):
        return self.minimums[-1]


if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(f"Minimum value: {stack.get_min()}")