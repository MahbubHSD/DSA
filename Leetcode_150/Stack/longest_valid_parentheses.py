# Leetcode Problem 32: Longest Valid Parentheses

text = ")()())"


def longest_valid_parentheses(text):
    """Find the length of the longest valid parentheses substring."""
    stack = [-1]
    best = 0
    for index, character in enumerate(text):
        if character == "(":
            stack.append(index)
        else:
            stack.pop()
            if not stack:
                stack.append(index)
            else:
                best = max(best, index - stack[-1])
    return best


if __name__ == "__main__":
    print(f"Longest valid length: {longest_valid_parentheses(text)}")