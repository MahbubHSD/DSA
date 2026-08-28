# Leetcode Problem 338: Counting Bits

n = 5


def counting_bits(n):
    """
    Count set bits for every integer from zero through n.

    Parameters:
    n (int): The inclusive upper bound.

    Returns:
    list: Set-bit counts for each integer.
    """
    counts = [0] * (n + 1)
    for value in range(1, n + 1):
        counts[value] = counts[value >> 1] + (value & 1)
    return counts


if __name__ == "__main__":
    result = counting_bits(n)
    print(f"Bit counts: {result}")