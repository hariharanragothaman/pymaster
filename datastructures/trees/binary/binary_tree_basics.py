"""
Binary Tree - Fundamentals
"""

from collections import deque

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

    def print_level_order(self, node):
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

    def print_postorder(self, root):
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

    def postorder_recursive(self, root, result=None):
        if root is None:
            return []
        if result is None:
            result = []
        self.postorder_recursive(root.left, result)
        self.postorder_recursive(root.right, result)
        result.append(root.data)
        return result


if __name__ == "__main__":
    arr = [3, 9, 20, None, None, 15, 7]
    print("The initial array is:", arr)

    node_map = {}
    for i in range(len(arr)):
        node_map[i] = Node(arr[i])
    print("The node map is:", node_map)

    bt = BinaryTree(arr)
    rt = bt.create_tree(node_map)
    print("The root of the tree is:", rt.data)

    level_order = bt.print_level_order(rt)
    print(*level_order)

    post_order = bt.print_postorder(rt)
    print(*post_order)
