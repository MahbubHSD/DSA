# Leetcode Problem 160: Intersection of Two Linked Lists


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def get_intersection_node(first, second):
    """
    Find the first shared node of two singly linked lists.

    Parameters:
    first (ListNode): First list head.
    second (ListNode): Second list head.

    Returns:
    ListNode: Shared node, or None when lists do not intersect.
    """
    left, right = first, second
    while left is not right:
        left = left.next if left else second
        right = right.next if right else first
    return left


if __name__ == "__main__":
    shared = ListNode(8)
    first = ListNode(4, shared)
    second = ListNode(5, shared)
    result = get_intersection_node(first, second)
    print(f"Intersection value: {result.value}")