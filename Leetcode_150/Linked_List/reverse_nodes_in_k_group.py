# Leetcode Problem 25: Reverse Nodes in k-Group


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def reverse_k_group(head, k):
    """
    Reverse list nodes in groups of k, leaving a short final group unchanged.

    Parameters:
    head (ListNode): The list head.
    k (int): Group size.

    Returns:
    ListNode: The transformed list head.
    """
    dummy = ListNode(next_node=head)
    group_previous = dummy
    while True:
        group_end = group_previous
        for _ in range(k):
            group_end = group_end.next
            if not group_end:
                return dummy.next
        group_start = group_previous.next
        next_group = group_end.next
        previous = next_group
        current = group_start
        while current is not next_group:
            following = current.next
            current.next = previous
            previous = current
            current = following
        group_previous.next = group_end
        group_previous = group_start


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = reverse_k_group(head, 2)
    print(f"New head value: {result.value}")