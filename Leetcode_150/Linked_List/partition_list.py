# Leetcode Problem 86: Partition List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def partition_list(head, pivot):
    """
    Place nodes below pivot before nodes greater than or equal to pivot.

    Parameters:
    head (ListNode): The list head.
    pivot (int): Partition value.

    Returns:
    ListNode: The partitioned list head.
    """
    smaller = ListNode()
    larger = ListNode()
    small_tail, large_tail = smaller, larger
    while head:
        if head.value < pivot:
            small_tail.next = head
            small_tail = small_tail.next
        else:
            large_tail.next = head
            large_tail = large_tail.next
        head = head.next
    large_tail.next = None
    small_tail.next = larger.next
    return smaller.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
    result = partition_list(head, 3)
    print(f"Partitioned head: {result.value}")