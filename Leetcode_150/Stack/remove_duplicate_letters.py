# Leetcode Problem 316: Remove Duplicate Letters

text = "cbacdcbc"


def remove_duplicate_letters(text):
    """Return the smallest lexicographic string containing each letter once."""
    from collections import Counter

    remaining = Counter(text)
    stack = []
    used = set()
    for character in text:
        remaining[character] -= 1
        if character in used:
            continue
        while stack and character < stack[-1] and remaining[stack[-1]]:
            used.remove(stack.pop())
        stack.append(character)
        used.add(character)
    return "".join(stack)


if __name__ == "__main__":
    print(f"Unique letters: {remove_duplicate_letters(text)}")