# Leetcode Problem 1493: Longest Subarray of 1's After Deleting One Element

arr = [1, 1, 0, 1]


def longest_subarray(arr):
    """Find the longest ones subarray after deleting exactly one value."""
    left = zeroes = result = 0
    for right, value in enumerate(arr):
        zeroes += value == 0
        while zeroes > 1:
            zeroes -= arr[left] == 0
            left += 1
        result = max(result, right - left)
    return result


if __name__ == "__main__":
    print(f"Longest subarray: {longest_subarray(arr)}")