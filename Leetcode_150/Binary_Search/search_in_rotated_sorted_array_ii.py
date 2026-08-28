# Leetcode Problem 81: Search in Rotated Sorted Array II

arr = [2, 5, 6, 0, 0, 1, 2]
target = 0


def search_rotated_with_duplicates(arr, target):
    """Search for target in a rotated sorted array with duplicates."""
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return True
        if arr[left] == arr[middle] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] <= arr[middle]:
            if arr[left] <= target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        elif arr[middle] < target <= arr[right]:
            left = middle + 1
        else:
            right = middle - 1
    return False


if __name__ == "__main__":
    print(f"Target found: {search_rotated_with_duplicates(arr, target)}")