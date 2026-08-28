# Leetcode Problem 303: Range Sum Query - Immutable


class NumArray:
    """Answer repeated inclusive range-sum queries."""

    def __init__(self, numbers):
        self.prefix = [0]
        for number in numbers:
            self.prefix.append(self.prefix[-1] + number)

    def sum_range(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    numbers = NumArray([-2, 0, 3, -5, 2, -1])
    print(f"Range sum: {numbers.sum_range(0, 2)}")