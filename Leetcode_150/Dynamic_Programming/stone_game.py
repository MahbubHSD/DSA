# Leetcode Problem 877: Stone Game

piles = [5, 3, 4, 5]


def stone_game(piles):
    """Determine whether the first player can win the optimal stone game."""
    difference = piles[:]
    for length in range(2, len(piles) + 1):
        for left in range(len(piles) - length + 1):
            right = left + length - 1
            difference[left] = max(piles[left] - difference[left + 1], piles[right] - difference[left])
    return difference[0] > 0


if __name__ == "__main__":
    print(f"First player wins: {stone_game(piles)}")