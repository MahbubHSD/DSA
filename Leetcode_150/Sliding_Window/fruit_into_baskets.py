# Leetcode Problem 904: Fruit Into Baskets

fruits = [1, 2, 1]


def total_fruit(fruits):
    """Find the longest subarray containing at most two distinct values."""
    from collections import defaultdict

    counts = defaultdict(int)
    left = result = 0
    for right, fruit in enumerate(fruits):
        counts[fruit] += 1
        while len(counts) > 2:
            counts[fruits[left]] -= 1
            if counts[fruits[left]] == 0:
                del counts[fruits[left]]
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == "__main__":
    print(f"Maximum fruit count: {total_fruit(fruits)}")