# Leetcode Problem 209: Minimum Size Subarray Sum

target = 7
arr = [2, 3, 1, 2, 4, 3]


def minimum_subarray_length(target, arr):
    """Find the shortest positive-value subarray with sum at least target."""
    left = total = 0
    best = len(arr) + 1
    for right, value in enumerate(arr):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= arr[left]
            left += 1
    return 0 if best == len(arr) + 1 else best


if __name__ == "__main__":
    print(f"Minimum subarray length: {minimum_subarray_length(target, arr)}")