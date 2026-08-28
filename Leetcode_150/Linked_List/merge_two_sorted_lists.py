# Leetcode Problem 21: Merge Two Sorted Lists


class ListNode:
    """A node in a singly linked list."""

    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def merge_two_lists(first, second):
    """
    Merge two sorted linked lists into one sorted list.

    Parameters:
    first (ListNode): The first sorted list.
    second (ListNode): The second sorted list.

    Returns:
    ListNode: The head of the merged sorted list.
    """
    dummy = ListNode()
    current = dummy
    while first and second:
        if first.value <= second.value:
            current.next, first = first, first.next
        else:
            current.next, second = second, second.next
        current = current.next
    current.next = first or second
    return dummy.next


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
    first = build_list([1, 2, 4])
    second = build_list([1, 3, 4])
    result = merge_two_lists(first, second)
    print(f"Merged list: {list_values(result)}")