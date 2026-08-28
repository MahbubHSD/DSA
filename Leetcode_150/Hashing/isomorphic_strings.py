# Leetcode Problem 205: Isomorphic Strings

first = "egg"
second = "add"


def is_isomorphic(first, second):
    """Determine whether characters map one-to-one between two strings."""
    if len(first) != len(second):
        return False
    forward, backward = {}, {}
    for left, right in zip(first, second):
        if forward.get(left, right) != right or backward.get(right, left) != left:
            return False
        forward[left] = right
        backward[right] = left
    return True


if __name__ == "__main__":
    print(f"Strings are isomorphic: {is_isomorphic(first, second)}")