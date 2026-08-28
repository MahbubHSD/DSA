# Sorting-based approach for Contains Duplicate

def contains_duplicate_sort(nums):
    """
    Sort the list and check adjacent values for equality.
    """
    sorted_nums = sorted(nums)
    for index in range(len(sorted_nums) - 1):
        if sorted_nums[index] == sorted_nums[index + 1]:
            return True
    return False


if __name__ == "__main__":
    print(contains_duplicate_sort([1, 2, 3, 1]))
    print(contains_duplicate_sort([1, 2, 3, 4]))
