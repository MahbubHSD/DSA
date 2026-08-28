# Leetcode Problem 237: Delete Node in a Linked List


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def delete_node(node):
    """Delete a node when only that node, not the head, is provided."""
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    node = ListNode(4, ListNode(5))
    delete_node(node)
    print(f"Updated node: {node.value}")