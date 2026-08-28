# Leetcode Problem 141: Linked List Cycle


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def has_cycle(head):
    """
    Determine whether a linked list contains a cycle.

    Parameters:
    head (ListNode): The list head.

    Returns:
    bool: True when a node can be reached again.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    first = ListNode(1)
    first.next = ListNode(2, first)
    print(f"List has cycle: {has_cycle(first)}")