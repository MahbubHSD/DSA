# Leetcode Problem 12: Integer to Roman

number = 1994


def integer_to_roman(number):
    """Convert an integer from 1 through 3999 to Roman numerals."""
    symbols = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))
    result = ""
    for value, symbol in symbols:
        count, number = divmod(number, value)
        result += symbol * count
    return result


if __name__ == "__main__":
    print(f"Roman numeral: {integer_to_roman(number)}")