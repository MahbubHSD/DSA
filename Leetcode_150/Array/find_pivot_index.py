# Leetcode Problem 724: Find Pivot Index

arr = [1, 7, 3, 6, 5, 6]


def pivot_index(arr):
    """Return the index where left and right sums are equal."""
    total = sum(arr)
    left = 0
    for index, value in enumerate(arr):
        if left == total - left - value:
            return index
        left += value
    return -1


if __name__ == "__main__":
    print(f"Pivot index: {pivot_index(arr)}")