# Leetcode Problem 2: Add Two Numbers


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def add_two_numbers(first, second):
    """
    Add two numbers represented by reversed linked lists.

    Parameters:
    first (ListNode): First reversed digit list.
    second (ListNode): Second reversed digit list.

    Returns:
    ListNode: Reversed digit list containing the sum.
    """
    dummy = ListNode()
    current = dummy
    carry = 0
    while first or second or carry:
        total = carry
        if first:
            total += first.value
            first = first.next
        if second:
            total += second.value
            second = second.next
        carry, digit = divmod(total, 10)
        current.next = ListNode(digit)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    first = ListNode(2, ListNode(4, ListNode(3)))
    second = ListNode(5, ListNode(6, ListNode(4)))
    result = add_two_numbers(first, second)
    print(f"Sum starts with: {result.value}")