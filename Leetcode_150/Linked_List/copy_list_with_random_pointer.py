# Leetcode Problem 138: Copy List with Random Pointer


class Node:
    def __init__(self, value=0, next_node=None, random=None):
        self.value = value
        self.next = next_node
        self.random = random


def copy_random_list(head):
    """
    Deep-copy a linked list with next and random pointers.

    Parameters:
    head (Node): The original list head.

    Returns:
    Node: The copied list head.
    """
    copies = {}
    current = head
    while current:
        copies[current] = Node(current.value)
        current = current.next
    current = head
    while current:
        copies[current].next = copies.get(current.next)
        copies[current].random = copies.get(current.random)
        current = current.next
    return copies.get(head)


if __name__ == "__main__":
    node = Node(7)
    result = copy_random_list(node)
    print(f"Copied node value: {result.value}")