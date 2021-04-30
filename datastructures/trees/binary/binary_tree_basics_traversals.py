"""
Binary Tree - Fundamentals
"""

from collections import deque
from typing import List

"""
General things to remember

Parent(r) = (r−1)/2⌋ if r≠0
Left child(r) = 2r+1 if 2r+1<n
Right child(r) = 2r+2 if 2r+2<n
Left sibling(r) = r−1 if r is even and r≠0
Right sibling(r) =r+1 if r is odd and r+1<n.

"""

""" Node representation of Tree Node"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BinaryTree:
    def __init__(self, array):
        self.arr = array
        self.root = None

    def create_tree(self, hmap):
        """
        Function that builds the tree
        Returns:
        """
        n = len(arr)
        self.root = hmap[0]

        # This is just to assign left and right children
        i = 0
        while i < n:
            node = hmap[i]

            if 0 < (2 * i + 1) < n:
                if arr[2 * i + 1]:
                    node.left = hmap[2 * i + 1]
            else:
                node.left = None

            if 0 < (2 * i + 2) < n:
                if arr[2 * i + 2]:
                    node.right = hmap[2 * i + 2]
            else:
                node.right = None
            i += 1

        return self.root

    def get_level_order(self, node) -> List[int]:
        """
        This is classic BFS template in Trees
        Args:
            node:
        Returns:
        """
        traverse = []
        level = 0

        if not node:
            return traverse

        # Put the entire tree into the Queue
        q = deque([node])

        while q:
            traverse.append([])
            for i in range(len(q)):
                node = q.popleft()
                traverse[level].append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return traverse

    def get_postorder(self, root):
        """
        Post-order-traversal - heavily useful when traversing from the bottom
        Time Complexity: O(n)
        Args:
            root:

        Returns:

        """
        res_temp = []
        post_order = []

        if not root:
            return post_order

        stack = [root]

        while stack:
            root = stack.pop()
            res_temp.append(root.data)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        while res_temp:
            post_order.append(res_temp.pop())

        return post_order

    def postorder_recursive(self, root, result=None) -> List[int]:
        if root is None:
            return []
        if result is None:
            result = []
        self.postorder_recursive(root.left, result)
        self.postorder_recursive(root.right, result)
        result.append(root.data)
        return result

    def get_inorder(self, node) -> List[int]:
        inorder = []
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            inorder.append(node.data)
            node = node.right
        return inorder

    def get_preorder(self, root):
        result = []

        if root is None:
            return result

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.data)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result

    def maximum_depth(self, root):
        _levels = self.get_level_order(root)
        return len(_levels)


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4, 4, 3]
    print("The initial array is:", arr)

    node_map = {}
    for i in range(len(arr)):
        node_map[i] = Node(arr[i])
    print("The node map is:", node_map)

    bt = BinaryTree(arr)
    rt = bt.create_tree(node_map)
    print("The root of the tree is:", rt.data)

    # Level Order traversal
    levelorder = bt.get_level_order(rt)
    print(*levelorder)

    # Post Order traversal
    postorder = bt.get_postorder(rt)
    print(*postorder)

    # In order traversal
    inorder = bt.get_inorder(rt)
    print(*inorder)

    # Preorder traversal
    preorder = bt.get_preorder(rt)
    print(*preorder)

    # Get Maximum depth
    depth = bt.maximum_depth(rt)
    print("The maximum_depth is: ", depth)
