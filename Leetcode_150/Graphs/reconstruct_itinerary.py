# Leetcode Problem 332: Reconstruct Itinerary

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]


def reconstruct_itinerary(tickets):
    """
    Reconstruct the lexicographically smallest itinerary using every ticket.

    Parameters:
    tickets (list): Directed flights represented as [from, to].

    Returns:
    list: Airport sequence starting at JFK.
    """
    from collections import defaultdict

    graph = defaultdict(list)
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
    route = []

    def visit(airport):
        while graph[airport]:
            visit(graph[airport].pop())
        route.append(airport)

    visit("JFK")
    return route[::-1]


if __name__ == "__main__":
    result = reconstruct_itinerary(tickets)
    print(f"Itinerary: {result}")