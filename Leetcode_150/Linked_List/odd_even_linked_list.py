# Leetcode Problem 328: Odd Even Linked List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def odd_even_list(head):
    """Group odd-positioned nodes before even-positioned nodes in place."""
    if not head:
        return None
    odd, even = head, head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(f"Odd-even head: {odd_even_list(head).value}")