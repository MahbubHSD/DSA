# Leetcode Problem 1004: Max Consecutive Ones III

arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2


def longest_ones(arr, k):
    """Find the longest ones subarray after flipping at most k zeroes."""
    left = zeroes = result = 0
    for right, value in enumerate(arr):
        zeroes += value == 0
        while zeroes > k:
            zeroes -= arr[left] == 0
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    print(f"Longest ones: {longest_ones(arr, k)}")