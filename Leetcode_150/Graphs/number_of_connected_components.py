# Leetcode Problem 323: Number of Connected Components in an Undirected Graph

n = 5
edges = [[0, 1], [1, 2], [3, 4]]


def connected_components(n, edges):
    """
    Count connected components in an undirected graph.

    Parameters:
    n (int): Number of nodes labeled zero through n - 1.
    edges (list): Undirected graph edges.

    Returns:
    int: Number of connected components.
    """
    parent = list(range(n))

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    components = n
    for first, second in edges:
        first_root, second_root = find(first), find(second)
        if first_root != second_root:
            parent[first_root] = second_root
            components -= 1
    return components


if __name__ == "__main__":
    result = connected_components(n, edges)
    print(f"Connected components: {result}")