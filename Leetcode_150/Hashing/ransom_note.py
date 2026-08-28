# Leetcode Problem 383: Ransom Note

ransom = "aa"
magazine = "aab"


def can_construct(ransom, magazine):
    """Determine whether ransom can be made from magazine characters."""
    from collections import Counter

    return not (Counter(ransom) - Counter(magazine))


if __name__ == "__main__":
    print(f"Can construct note: {can_construct(ransom, magazine)}")