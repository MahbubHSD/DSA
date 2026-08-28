# Leetcode Problem 169: Majority Element

arr = [2, 2, 1, 1, 1, 2, 2]


def majority_element(arr):
    """
    Find the value appearing more than half the time.

    Parameters:
    arr (list): A list containing a guaranteed majority value.

    Returns:
    int: The majority value.
    """
    candidate = count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate


if __name__ == "__main__":
    result = majority_element(arr)
    print(f"Majority element: {result}")