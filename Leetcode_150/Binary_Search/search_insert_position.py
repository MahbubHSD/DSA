# Leetcode Problem 35: Search Insert Position

arr = [1, 3, 5, 6]
target = 5


def search_insert(arr, target):
    """Return target's index or its insertion index in a sorted array."""
    left, right = 0, len(arr)
    while left < right:
        middle = (left + right) // 2
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left


if __name__ == "__main__":
    print(f"Insert position: {search_insert(arr, target)}")