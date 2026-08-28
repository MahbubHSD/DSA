# Leetcode Problem 841: Keys and Rooms

rooms = [[1], [2], [3], []]


def can_visit_all_rooms(rooms):
    """Determine whether every room is reachable from room zero."""
    seen = {0}
    stack = [0]
    while stack:
        for key in rooms[stack.pop()]:
            if key not in seen:
                seen.add(key)
                stack.append(key)
    return len(seen) == len(rooms)


if __name__ == "__main__":
    print(f"All rooms reachable: {can_visit_all_rooms(rooms)}")