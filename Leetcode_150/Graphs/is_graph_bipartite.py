# Leetcode Problem 785: Is Graph Bipartite?

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]


def is_bipartite(graph):
    """
    Determine whether an undirected graph can be split into two groups.

    Parameters:
    graph (list): Adjacency lists for each node.

    Returns:
    bool: True when adjacent nodes can receive opposite colors.
    """
    colors = {}
    for start in range(len(graph)):
        if start in colors:
            continue
        colors[start] = 0
        queue = [start]
        for node in queue:
            for neighbor in graph[node]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
    return True


if __name__ == "__main__":
    result = is_bipartite(graph)
    print(f"Graph is bipartite: {result}")