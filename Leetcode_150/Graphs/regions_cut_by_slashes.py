# Leetcode Problem 959: Regions Cut By Slashes

grid = [" /", "/ "]


def regions_by_slashes(grid):
    """Count regions formed by slash characters in a square grid."""
    size = len(grid)
    parent = list(range(size * size * 4))

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first, second):
        first, second = find(first), find(second)
        if first != second:
            parent[first] = second

    for row in range(size):
        for column in range(size):
            base = (row * size + column) * 4
            if grid[row][column] == "/":
                union(base, base + 3)
                union(base + 1, base + 2)
            elif grid[row][column] == "\\":
                union(base, base + 1)
                union(base + 2, base + 3)
            else:
                union(base, base + 1)
                union(base + 1, base + 2)
                union(base + 2, base + 3)
            if row:
                union(base, base - size * 4 + 2)
            if column:
                union(base + 3, base - 4 + 1)
    return len({find(node) for node in range(len(parent))})


if __name__ == "__main__":
    print(f"Slash regions: {regions_by_slashes(grid)}")