"""
Solution for 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 52 ms, faster than 74.86% of Python3 online submissions for Validate Binary Search Tree.
    Memory Usage: 17.1 MB, less than 5.13% of Python3 online submissions for Validate Binary Search Tree.
    """
    def isValidBST(self, root):
        """
        Given a binary tree, determine if it is a valid binary search tree (BST).

        Assume a BST is defined as follows:

        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.


        Example 1:

            2
           / \
          1   3

        Input: [2,1,3]
        Output: true
        Example 2:

            5
           / \
          1   4
             / \
            3   6

        Input: [5,1,4,null,null,3,6]
        Output: false
        Explanation: The root node's value is 5 but its right child's value is 4.
        Args:
            root: TreeNode object as a root

        Returns:
            bool: whether the given tree is a BST or not
        """
        values = [-float('inf')]

        def dfs(node):
            if not node:
                return True

            left_valid = dfs(node.left)
            root_valid = values[0] < node.val
            values[0] = node.val
            right_valid = dfs(node.right)
            return left_valid and root_valid and right_valid

        return dfs(root)
