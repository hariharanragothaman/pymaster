# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root, ]
        parent_map = {root: None}

        while stack:
            node = stack.pop()
            if node.left:
                parent_map[node.left] = node
                stack.append(node.left)
            if node.right:
                parent_map[node.right] = node
                stack.append(node.right)

        if p not in parent_map or q not in parent_map:
            return None

        ancestors = set()
        while p :
            ancestors.add(p)
            p = parent_map[p]

        while q not in ancestors:
            q = parent_map[q]
        return q