# Leetcode Problem 350: Intersection of Two Arrays II

first = [1, 2, 2, 1]
second = [2, 2]


def intersect_arrays(first, second):
    """Return the multiset intersection of two arrays."""
    from collections import Counter

    counts = Counter(first)
    result = []
    for value in second:
        if counts[value]:
            result.append(value)
            counts[value] -= 1
    return result


if __name__ == "__main__":
    print(f"Array intersection: {intersect_arrays(first, second)}")