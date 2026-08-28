# Brute-force approach for Two Sum

def two_sum_bruteforce(nums, target):
    """
    Check every pair of indices and return the pair that sums to target.
    """
    for left in range(len(nums)):
        for right in range(left + 1, len(nums)):
            if nums[left] + nums[right] == target:
                return [left, right]
    return []


if __name__ == "__main__":
    example = [2, 7, 11, 15]
    target = 9
    print(two_sum_bruteforce(example, target))
