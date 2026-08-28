# Leetcode Problem 18: 4Sum

arr = [1, 0, -1, 0, -2, 2]
target = 0


def four_sum(arr, target):
    """
    Find unique quadruplets whose values add up to target.

    Parameters:
    arr (list): A list of integers.
    target (int): The required sum.

    Returns:
    list: Unique matching quadruplets.
    """
    arr.sort()
    result = []
    for first in range(len(arr) - 3):
        if first and arr[first] == arr[first - 1]:
            continue
        for second in range(first + 1, len(arr) - 2):
            if second > first + 1 and arr[second] == arr[second - 1]:
                continue
            left, right = second + 1, len(arr) - 1
            while left < right:
                total = arr[first] + arr[second] + arr[left] + arr[right]
                if total == target:
                    result.append([arr[first], arr[second], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


if __name__ == "__main__":
    result = four_sum(arr, target)
    print(f"Matching quadruplets: {result}")