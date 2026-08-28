# Leetcode Problem 611: Valid Triangle Number

arr = [2, 2, 3, 4]


def valid_triangle_number(arr):
    """Count triples that can form a non-degenerate triangle."""
    arr.sort()
    count = 0
    for right in range(len(arr) - 1, 1, -1):
        left, middle = 0, right - 1
        while left < middle:
            if arr[left] + arr[middle] > arr[right]:
                count += middle - left
                middle -= 1
            else:
                left += 1
    return count


if __name__ == "__main__":
    print(f"Valid triangles: {valid_triangle_number(arr)}")