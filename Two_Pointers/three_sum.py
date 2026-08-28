# Leetcode Problem 15: 3Sum

arr = [-1, 0, 1, 2, -1, -4]


def three_sum(arr):
    """
    Find unique triplets whose values add up to zero.

    Parameters:
    arr (list): A list of integers.

    Returns:
    list: Unique zero-sum triplets.
    """
    arr.sort()
    triplets = []
    for index in range(len(arr) - 2):
        if index and arr[index] == arr[index - 1]:
            continue
        left, right = index + 1, len(arr) - 1
        while left < right:
            total = arr[index] + arr[left] + arr[right]
            if total == 0:
                triplets.append([arr[index], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == "__main__":
    result = three_sum(arr)
    print(f"Zero-sum triplets: {result}")