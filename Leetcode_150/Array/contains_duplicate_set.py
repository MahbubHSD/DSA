# Set-based approach for Contains Duplicate

def contains_duplicate_set(nums):
    """
    Return True if any value appears more than once.
    """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(contains_duplicate_set([1, 2, 3, 1]))
    print(contains_duplicate_set([1, 2, 3, 4]))
