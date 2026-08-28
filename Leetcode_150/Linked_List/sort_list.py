# Leetcode Problem 148: Sort List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def sort_list(head):
    """
    Sort a linked list in ascending order.

    Parameters:
    head (ListNode): The list head.

    Returns:
    ListNode: The sorted list head.
    """
    if not head or not head.next:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    first = sort_list(head)
    second = sort_list(second)
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


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    result = sort_list(head)
    print(f"Sorted head value: {result.value}")