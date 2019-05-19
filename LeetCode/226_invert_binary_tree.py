"""
Solution for 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
    """
    def __init__(self, x):
        """
        Initialization method for a Node object
        Args:
            x: integer value of a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 36 ms, faster than 86.59% of Python3 online submissions for Invert Binary Tree.
    Memory Usage: 13.1 MB, less than 51.67% of Python3 online submissions for Invert Binary Tree.
    """
    def invertTree(self, root):
        """
        Invert a binary tree.

        Example:

        Input:

             4
           /   \
          2     7
         / \   / \
        1   3 6   9
        Output:

             4
           /   \
          7     2
         / \   / \
        9   6 3   1
        Args:
            root: TreeNode object as the root of a BT

        Returns:
            TreeNode: as the root of inverted BT
        """
        return self.iterative_approach(root)

    def iterative_approach(self, root):
        """
        Iterative solution to this problem
        Args:
            root: TreeNode object as the root of a BT

        Returns:
            TreeNode: as the root of inverted BT
        """
        if not root:
            return []

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root

    def recursive_approach(self, root):
        """
        Recursive solution for this problem
        Args:
            root: TreeNode object as the root of a BT

        Returns:
            TreeNode: as the root of inverted BT
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.recursive_approach(root.left)
        self.recursive_approach(root.right)
        return root
