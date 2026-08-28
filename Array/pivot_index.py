# Leetcode Problem 724: Find Pivot Index

nums = [1, 7, 3, 6, 5, 6]


def pivot_index(nums):
    """Return the index where the left sum equals the right sum."""
    total = sum(nums)
    left_sum = 0

    for index, value in enumerate(nums):
        if left_sum == total - left_sum - value:
            return index
        left_sum += value

    return -1


if __name__ == "__main__":
    print(f"Pivot index: {pivot_index(nums)}")
