# Leetcode Problem 190: Reverse Bits

number = 43261596


def reverse_bits(number):
    """
    Reverse the bits of a 32-bit unsigned integer.

    Parameters:
    number (int): A 32-bit unsigned integer.

    Returns:
    int: The integer represented by reversed bits.
    """
    result = 0
    for _ in range(32):
        result = (result << 1) | (number & 1)
        number >>= 1
    return result


if __name__ == "__main__":
    result = reverse_bits(number)
    print(f"Reversed bits: {result}")