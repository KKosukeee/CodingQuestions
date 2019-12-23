"""
Solution for 173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BST
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for a Node
        """
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    """
    Runtime: 108 ms, faster than 23.72% of Python3 online submissions for Binary Search Tree
        Iterator.
    Memory Usage: 19.5 MB, less than 100.00% of Python3 online submissions for Binary Search Tree
        Iterator.
    """
    def __init__(self, root):
        """
        Initialization method
        Args:
            root: TreeNode as a root for the BST
        """
        # initialize a queue
        self.queue = deque()

        # do in-order traversal
        self.in_order_traversal(root)

        self.stack = []
        self.left_most(root)

    def in_order_traversal(self, root):
        """
        does the in-order traversal and append to the queue
        Args:
            root: TreeNode object for a BST

        Returns:

        """
        # if root is a leaf node, then append to the queue
        if not root:
            return
        elif not root.left and not root.right:
            self.queue.append(root.val)
        else:
            # recursive call for left child
            self.in_order_traversal(root.left)

            # append root node to the queue
            self.queue.append(root.val)

            # recursive call for right child
            self.in_order_traversal(root.right)

    def next(self):
        """
        get minimum element from the tree
        Returns:
            int: minimum number in current tree
        """
        # pop an element with popleft operation
        return self.space_effient_next()

    def brute_force_next(self):
        """
        A brute force solution that runs in O(1) time and O(N) space

        Returns:

        """
        return self.queue.popleft()

    def space_effient_next(self):
        """
        A space efficient solution that runs in O(H) in time and O(H) in space

        Returns:

        """

    def hasNext(self):
        """
        determine if the tree has a node in it or not
        Returns:
            bool: True if the tree is not empty, False otherwise
        """
        # check if the queue is empty or not
        return self.space_efficient_hasNext()

    def brute_force_hasNext(self):
        """
        A brute force solution that runs in O(1) in time and O(N) in space

        Returns:

        """
        return len(self.queue) > 0

    def space_efficient_hasNext(self):
        """
        A space efficient solution that runs in O(H) in time and O(H) in space

        Returns:

        """

    def left_most(self, node):
        while node:
            self.stack.append(node)
            node = node.left