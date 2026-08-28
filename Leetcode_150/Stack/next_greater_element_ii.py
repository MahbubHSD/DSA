# Leetcode Problem 503: Next Greater Element II

arr = [1, 2, 1]


def next_greater_circular(arr):
    """Find next greater values while treating arr as circular."""
    result = [-1] * len(arr)
    stack = []
    for index in range(2 * len(arr)):
        actual = index % len(arr)
        while stack and arr[stack[-1]] < arr[actual]:
            result[stack.pop()] = arr[actual]
        if index < len(arr):
            stack.append(actual)
    return result


if __name__ == "__main__":
    print(f"Circular next greater values: {next_greater_circular(arr)}")