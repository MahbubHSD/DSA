# Leetcode Problem 1: Two Sum

arr = [2, 7, 11, 15]
target = 9

def two_sum(arr, target):
    """
    Find two numbers in the array that add up to the target value.

    Parameters:
    arr (list): A list of integers.
    target (int): The target sum for the two numbers.

    Returns:
    list: A list containing the indices of the two numbers that add up to the target value.
          If no such pair exists, returns an empty list.
    """
    num_to_index = {}  # Dictionary to store numbers and their indices

    for index, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]  # Return indices of the two numbers
        num_to_index[num] = index  # Store the index of the current number

    return []  # Return an empty list if no pair is found


if __name__ == "__main__":
    result = two_sum(arr, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")