# Leetcode Problem 167: Two Sum II - Input Array Is Sorted

numbers = [2, 7, 11, 15]
target = 9


def two_sum_sorted(numbers, target):
    """
    Find two one-based indices whose values add to target.

    Parameters:
    numbers (list): A sorted list of integers.
    target (int): The required sum.

    Returns:
    list: One-based indices of the matching pair.
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    result = two_sum_sorted(numbers, target)
    print(f"One-based indices: {result}")