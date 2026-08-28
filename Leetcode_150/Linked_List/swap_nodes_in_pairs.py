# Leetcode Problem 24: Swap Nodes in Pairs


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def swap_pairs(head):
    """Swap every adjacent pair of linked-list nodes."""
    dummy = ListNode(next_node=head)
    previous = dummy
    while previous.next and previous.next.next:
        first = previous.next
        second = first.next
        previous.next, second.next, first.next = second, first, second.next
        previous = first
    return dummy.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(f"Swapped head: {swap_pairs(head).value}")