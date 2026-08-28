# Leetcode Problem 238: Product of Array Except Self

arr = [1, 2, 3, 4]


def product_except_self(arr):
    """
    Return the product of every array value except the value at each index.

    Parameters:
    arr (list): A list of integers.

    Returns:
    list: Products excluding the value at each corresponding index.
    """
    products = [1] * len(arr)
    prefix_product = 1

    for index, num in enumerate(arr):
        products[index] = prefix_product
        prefix_product *= num

    suffix_product = 1
    for index in range(len(arr) - 1, -1, -1):
        products[index] *= suffix_product
        suffix_product *= arr[index]

    return products


if __name__ == "__main__":
    result = product_except_self(arr)
    print(f"Products except self: {result}")