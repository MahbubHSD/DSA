# Leetcode Problem 684: Redundant Connection

edges = [[1, 2], [1, 3], [2, 3]]


def redundant_connection(edges):
    """
    Find the edge that creates a cycle in an almost-tree graph.

    Parameters:
    edges (list): Undirected edges with one extra edge.

    Returns:
    list: The redundant edge.
    """
    parent = list(range(len(edges) + 1))

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    for first, second in edges:
        first_root, second_root = find(first), find(second)
        if first_root == second_root:
            return [first, second]
        parent[first_root] = second_root
    return []


if __name__ == "__main__":
    result = redundant_connection(edges)
    print(f"Redundant edge: {result}")