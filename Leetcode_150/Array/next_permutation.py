# Leetcode Problem 31: Next Permutation

arr = [1, 2, 3]


def next_permutation(arr):
    """
    Rearrange the array into its next lexicographically greater permutation.

    Parameters:
    arr (list): Values to rearrange in place.

    Returns:
    list: The next permutation, or the first permutation when none is greater.
    """
    index = len(arr) - 2
    while index >= 0 and arr[index] >= arr[index + 1]:
        index -= 1
    if index >= 0:
        swap = len(arr) - 1
        while arr[swap] <= arr[index]:
            swap -= 1
        arr[index], arr[swap] = arr[swap], arr[index]
    arr[index + 1:] = reversed(arr[index + 1:])
    return arr


if __name__ == "__main__":
    result = next_permutation(arr)
    print(f"Next permutation: {result}")