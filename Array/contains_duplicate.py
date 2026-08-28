# Leetcode Problem 217: Contains Duplicate

nums = [1, 2, 3, 1]


def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the list.

    Parameters:
    nums (list): A list of integers.

    Returns:
    bool: True if a duplicate exists, otherwise False.
    """
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    result = contains_duplicate(nums)
    print(f"Contains duplicate: {result}")
