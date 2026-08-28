# Leetcode Problem 20: Valid Parentheses

text = "()[]{}"


def is_valid_parentheses(text):
    """
    Determine whether every bracket is correctly opened and closed.

    Parameters:
    text (str): A string containing brackets.

    Returns:
    bool: True when the brackets are balanced and properly nested.
    """
    pairs = {")": "(", "]": "[", "}": "{"
    }
    stack = []
    for character in text:
        if character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
        else:
            stack.append(character)
    return not stack


if __name__ == "__main__":
    result = is_valid_parentheses(text)
    print(f"Parentheses are valid: {result}")