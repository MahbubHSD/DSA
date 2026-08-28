def three_sum(arr, target):
    """
    Find all unique triplets in the array that sum up to the target value.

    Parameters:
    arr (list): A list of integers.
    target (int): The target sum for the triplets.

    Returns:
    list: A list of unique triplets that sum up to the target value.
    """
    arr.sort()  # Sort the array to facilitate the two-pointer approach
    triplets = []
    n = len(arr)

    for i in range(n - 2):
        # Skip duplicate values for the first element of the triplet
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                triplets.append((arr[i], arr[left], arr[right]))
                # Skip duplicates for the second element of the triplet
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Skip duplicates for the third element of the triplet
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets