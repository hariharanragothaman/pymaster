"""
Breadth-First Search - Implemented using queues
This can be implemented for both Trees / Graphs
Here, we will use Trees as examples.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def level_order(self, root):
        traverse = []
        level = 0

        if not root:
            return traverse

        # Put the entire tree into the Queue
        q = deque([root])

        while q:
            traverse.append([])
            for i in range(len(q)):
                node = q.popleft()
                traverse[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return traverse
