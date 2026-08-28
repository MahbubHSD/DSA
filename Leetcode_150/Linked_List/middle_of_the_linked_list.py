# Leetcode Problem 876: Middle of the Linked List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def middle_node(head):
    """Return the second middle node when the list length is even."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Middle value: {middle_node(head).value}")