"""
Solution for 872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
    """
    def __init__(self, x):
        """
        Initialization method for a BT
        Args:
            x: int value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 36 ms, faster than 95.53% of Python3 online submissions for Leaf-Similar Trees.
    Memory Usage: 13.1 MB, less than 66.57% of Python3 online submissions for Leaf-Similar Trees.
    """
    def leafSimilar(self, root1, root2):
        """
        Consider all the leaves of a binary tree.  From left to right order, the values of those
        leaves form a leaf value sequence.

        For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

        Two binary trees are considered leaf-similar if their leaf value sequence is the same.

        Return true if and only if the two given trees with head nodes root1 and root2 are
        leaf-similar.
        Args:
            root1: TreeNode object as the root node for a BT
            root2: TreeNode object as the root node for a BT

        Returns:
            bool: True if they are the similar by definition, False otherwise
        """
        leaves_1, leaves_2 = [], []

        def dfs(root, array):
            if not root:
                return
            elif self.is_leaf(root):
                array.append(root.val)
            else:
                dfs(root.left, array)
                dfs(root.right, array)

        dfs(root1, leaves_1)
        dfs(root2, leaves_2)

        return leaves_1 == leaves_2

    def is_leaf(self, root):
        """
        This method determine if the root is a leaf node or not
        Args:
            root: TreeNode object to determine if the root is a leaf or not

        Returns:
            bool: True if the root is a leaf node, False otherwise
        """
        return not root.left and not root.right
