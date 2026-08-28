# Leetcode Problem 234: Palindrome Linked List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def is_palindrome_list(head):
    """
    Determine whether a singly linked list reads the same both ways.

    Parameters:
    head (ListNode): The list head.

    Returns:
    bool: True when the list is a palindrome.
    """
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values == values[::-1]


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    result = is_palindrome_list(head)
    print(f"List is palindrome: {result}")