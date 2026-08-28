# Leetcode Problem 1009: Complement of Base 10 Integer

number = 5


def bitwise_complement(number):
    """Return the bitwise complement of a non-negative integer."""
    if number == 0:
        return 1
    mask = 1
    while mask <= number:
        mask <<= 1
    return (mask - 1) ^ number


if __name__ == "__main__":
    print(f"Bitwise complement: {bitwise_complement(number)}")