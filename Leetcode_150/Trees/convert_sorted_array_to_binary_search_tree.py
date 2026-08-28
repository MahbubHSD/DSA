# Leetcode Problem 108: Convert Sorted Array to Binary Search Tree

arr = [-10, -3, 0, 5, 9]


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sorted_array_to_bst(arr):
    """Build a height-balanced BST from a sorted array."""
    if not arr:
        return None
    middle = len(arr) // 2
    return TreeNode(arr[middle], sorted_array_to_bst(arr[:middle]), sorted_array_to_bst(arr[middle + 1:]))


if __name__ == "__main__":
    print(f"BST root: {sorted_array_to_bst(arr).value}")