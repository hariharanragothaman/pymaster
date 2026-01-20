"""
Depth-First Search of a Tree
1. Quick Logic
2. Getting all the Paths
3. InOrder -- PreOrder -- PostOrder
4. Questions like number of islands in 2D matrices
"""

from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


# General Logic is: What you add in the last stack, is the first you will parse! - Remember Stack

# Pre-Order Traversal
def preorder_traversal(self, root: TreeNode) -> List[int]:
    """
             2
            / \
           1   3
            \
             4

    Root - Left - Right
    """
    result = []
    if root is None:
        return result

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return result


# Post-Order is the just reversing the pre-order
def postorder_traversal(root: TreeNode) -> List[int]:
    result = []
    if root is None:
        return result

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return result[::-1]
