# Leetcode Problem 1192: Critical Connections in a Network

n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]


def critical_connections(n, connections):
    """
    Find edges whose removal disconnects an undirected network.

    Parameters:
    n (int): Number of network nodes.
    connections (list): Undirected edges.

    Returns:
    list: All bridge edges.
    """
    graph = [[] for _ in range(n)]
    for first, second in connections:
        graph[first].append(second)
        graph[second].append(first)
    discovery = [-1] * n
    low = [0] * n
    bridges = []
    time = 0

    def visit(node, parent):
        nonlocal time
        discovery[node] = low[node] = time
        time += 1
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if discovery[neighbor] == -1:
                visit(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], discovery[neighbor])

    visit(0, -1)
    return bridges


if __name__ == "__main__":
    result = critical_connections(n, connections)
    print(f"Critical connections: {result}")