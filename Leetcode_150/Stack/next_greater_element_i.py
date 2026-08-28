# Leetcode Problem 496: Next Greater Element I

numbers = [4, 1, 2]
reference = [1, 3, 4, 2]


def next_greater_element(numbers, reference):
    """Find each value's next greater value in reference."""
    stack = []
    greater = {}
    for value in reference:
        while stack and stack[-1] < value:
            greater[stack.pop()] = value
        stack.append(value)
    return [greater.get(value, -1) for value in numbers]


if __name__ == "__main__":
    print(f"Next greater values: {next_greater_element(numbers, reference)}")