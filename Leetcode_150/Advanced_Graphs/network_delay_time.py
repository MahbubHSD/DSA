# Leetcode Problem 743: Network Delay Time

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2


def network_delay_time(times, n, k):
    """
    Find the time for a signal to reach every node.

    Parameters:
    times (list): Directed edges [source, destination, travel_time].
    n (int): Number of nodes labeled one through n.
    k (int): Starting node.

    Returns:
    int: The greatest shortest-path time, or -1 if a node is unreachable.
    """
    import heapq

    graph = [[] for _ in range(n + 1)]
    for source, destination, duration in times:
        graph[source].append((destination, duration))
    distances = [float("inf")] * (n + 1)
    distances[k] = 0
    queue = [(0, k)]
    while queue:
        distance, node = heapq.heappop(queue)
        if distance > distances[node]:
            continue
        for neighbor, duration in graph[node]:
            next_distance = distance + duration
            if next_distance < distances[neighbor]:
                distances[neighbor] = next_distance
                heapq.heappush(queue, (next_distance, neighbor))
    result = max(distances[1:])
    return -1 if result == float("inf") else result


if __name__ == "__main__":
    result = network_delay_time(times, n, k)
    print(f"Network delay: {result}")