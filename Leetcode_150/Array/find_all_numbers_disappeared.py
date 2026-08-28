# Leetcode Problem 448: Find All Numbers Disappeared in an Array

arr = [4, 3, 2, 7, 8, 2, 3, 1]


def disappeared_numbers(arr):
    """Return values from 1 through n that are absent from arr."""
    for value in arr:
        index = abs(value) - 1
        if arr[index] > 0:
            arr[index] *= -1
    return [index + 1 for index, value in enumerate(arr) if value > 0]


if __name__ == "__main__":
    print(f"Missing values: {disappeared_numbers(arr)}")