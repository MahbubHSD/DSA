# Leetcode Problem 287: Find the Duplicate Number

arr = [1, 3, 4, 2, 2]


def find_duplicate(arr):
    """
    Find the duplicated value without modifying the array.

    Parameters:
    arr (list): Values from 1 through n with one duplicate.

    Returns:
    int: The duplicated value.
    """
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


if __name__ == "__main__":
    result = find_duplicate(arr)
    print(f"Duplicate value: {result}")