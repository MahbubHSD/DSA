# Leetcode Problem 61: Rotate List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def rotate_list(head, k):
    """
    Rotate a linked list to the right by k positions.

    Parameters:
    head (ListNode): The list head.
    k (int): Number of right rotations.

    Returns:
    ListNode: The rotated list head.
    """
    if not head or not head.next or k == 0:
        return head
    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1
    k %= length
    if k == 0:
        return head
    tail.next = head
    steps = length - k
    for _ in range(steps):
        tail = tail.next
    new_head = tail.next
    tail.next = None
    return new_head


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = rotate_list(head, 2)
    print(f"Rotated head value: {result.value}")