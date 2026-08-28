# Leetcode Problem 69: Sqrt(x)

x = 8


def integer_sqrt(x):
    """Return the integer square root of a non-negative integer."""
    left, right = 0, x
    while left <= right:
        middle = (left + right) // 2
        square = middle * middle
        if square == x:
            return middle
        if square < x:
            left = middle + 1
        else:
            right = middle - 1
    return right


if __name__ == "__main__":
    print(f"Integer square root: {integer_sqrt(x)}")