# Leetcode Problem 290: Word Pattern

pattern = "abba"
text = "dog cat cat dog"


def follows_pattern(pattern, text):
    """Determine whether words follow a bijective character pattern."""
    words = text.split()
    if len(pattern) != len(words):
        return False
    return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))


if __name__ == "__main__":
    print(f"Follows pattern: {follows_pattern(pattern, text)}")