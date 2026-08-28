# Leetcode Problem 189: Rotate Array

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotate_array(arr, k):
    """
    Rotate an array to the right by k positions in place.

    Parameters:
    arr (list): The array to rotate.
    k (int): Number of right rotations.

    Returns:
    list: The rotated array.
    """
    if arr:
        k %= len(arr)
        arr[:] = arr[-k:] + arr[:-k] if k else arr
    return arr


if __name__ == "__main__":
    result = rotate_array(arr, k)
    print(f"Rotated array: {result}")