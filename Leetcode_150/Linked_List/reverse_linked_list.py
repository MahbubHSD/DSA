# Leetcode Problem 206: Reverse Linked List


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def reverse_linked_list(head):
    """
    Reverse a singly linked list in place.

    Parameters:
    head (ListNode): The first list node.

    Returns:
    ListNode: The new head node.
    """
    previous = None
    current = head
    while current:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


def build_list(values):
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def list_values(head):
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values


if __name__ == "__main__":
    result = reverse_linked_list(build_list([1, 2, 3, 4, 5]))
    print(f"Reversed list: {list_values(result)}")