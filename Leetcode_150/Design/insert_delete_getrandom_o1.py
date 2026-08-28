# Leetcode Problem 380: Insert Delete GetRandom O(1)


class RandomizedSet:
    """Set supporting average constant-time insert, remove, and random lookup."""

    def __init__(self):
        self.values = []
        self.positions = {}

    def insert(self, value):
        if value in self.positions:
            return False
        self.positions[value] = len(self.values)
        self.values.append(value)
        return True

    def remove(self, value):
        if value not in self.positions:
            return False
        index = self.positions.pop(value)
        last = self.values.pop()
        if index < len(self.values):
            self.values[index] = last
            self.positions[last] = index
        return True

    def get_random(self):
        import random

        return random.choice(self.values)


if __name__ == "__main__":
    values = RandomizedSet()
    values.insert(1)
    print(f"Random value: {values.get_random()}")