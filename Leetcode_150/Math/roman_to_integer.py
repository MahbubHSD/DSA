# Leetcode Problem 13: Roman to Integer

text = "MCMXCIV"


def roman_to_integer(text):
    """Convert a Roman numeral to an integer."""
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for index, character in enumerate(text):
        value = values[character]
        result += -value if index + 1 < len(text) and value < values[text[index + 1]] else value
    return result


if __name__ == "__main__":
    print(f"Integer value: {roman_to_integer(text)}")