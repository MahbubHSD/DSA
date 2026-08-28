# Leetcode Problem 19: Remove Nth Node From End of List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def remove_nth_from_end(head, n):
    """
    Remove the nth node from the end of a linked list.

    Parameters:
    head (ListNode): The list head.
    n (int): One-based position from the end.

    Returns:
    ListNode: The updated list head.
    """
    dummy = ListNode(next_node=head)
    left = right = dummy
    for _ in range(n):
        right = right.next
    while right and right.next:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3)))
    result = remove_nth_from_end(head, 2)
    print(f"New head value: {result.value}")