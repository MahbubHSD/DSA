# Leetcode Problem 256: Paint House

costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]


def minimum_paint_cost(costs):
    """Find the minimum cost to paint adjacent houses different colors."""
    totals = [0, 0, 0]
    for red, blue, green in costs:
        totals = [red + min(totals[1], totals[2]), blue + min(totals[0], totals[2]), green + min(totals[0], totals[1])]
    return min(totals)


if __name__ == "__main__":
    print(f"Minimum paint cost: {minimum_paint_cost(costs)}")