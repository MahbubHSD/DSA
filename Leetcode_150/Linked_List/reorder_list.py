# Leetcode Problem 143: Reorder List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def reorder_list(head):
    """
    Reorder a list as first, last, second, second-last, and so on.

    Parameters:
    head (ListNode): The first list node.

    Returns:
    ListNode: The head of the reordered list.
    """
    values = []
    current = head
    while current:
        values.append(current)
        current = current.next
    left, right = 0, len(values) - 1
    while left < right:
        values[left].next = values[right]
        left += 1
        if left == right:
            break
        values[right].next = values[left]
        right -= 1
    if values:
        values[left].next = None
    return head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorder_list(head)
    values = []
    while head:
        values.append(head.value)
        head = head.next
    print(f"Reordered list: {values}")