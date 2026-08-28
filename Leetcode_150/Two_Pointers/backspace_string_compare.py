# Leetcode Problem 844: Backspace String Compare

first = "ab#c"
second = "ad#c"


def backspace_compare(first, second):
    """Compare strings after applying # as a backspace."""
    def build(text):
        result = []
        for character in text:
            if character == "#":
                if result:
                    result.pop()
            else:
                result.append(character)
        return result

    return build(first) == build(second)


if __name__ == "__main__":
    print(f"Strings match: {backspace_compare(first, second)}")