"""
Common recipes in Trees
"""

from typing import Iterator

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def inorder(node: TreeNode) -> Iterator[int]:
    stack = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        yield node.val
        node = node.right