# Leetcode Problem 34: Find First and Last Position of Element in Sorted Array

arr = [5, 7, 7, 8, 8, 10]
target = 8


def search_range(arr, target):
    """Return the first and last index of target in a sorted array."""
    def boundary(find_first):
        left, right = 0, len(arr) - 1
        result = -1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == target:
                result = middle
                if find_first:
                    right = middle - 1
                else:
                    left = middle + 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return result

    return [boundary(True), boundary(False)]


if __name__ == "__main__":
    print(f"Target range: {search_range(arr, target)}")