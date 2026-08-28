# Leetcode Problem 1049: Last Stone Weight II

stones = [2, 7, 4, 1, 8, 1]


def last_stone_weight(stones):
    """Find the smallest possible final stone weight."""
    target = sum(stones) // 2
    possible = {0}
    for stone in stones:
        possible |= {value + stone for value in possible if value + stone <= target}
    return sum(stones) - 2 * max(possible)


if __name__ == "__main__":
    print(f"Smallest final stone: {last_stone_weight(stones)}")