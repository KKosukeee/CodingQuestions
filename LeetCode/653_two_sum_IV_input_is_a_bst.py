"""
Solution for 653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode
    """
    def __init__(self, x):
        """
        Initialization
        Args:
            x(int):
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 84 ms, faster than 80.86% of Python3 online submissions for Two Sum IV - Input is a BST.
    Memory Usage: 16.4 MB, less than 5.88% of Python3 online submissions for Two Sum IV - Input is a BST.
    """
    def findTarget(self, root, k):
        """
        Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

        Example 1:

        Input:
            5
           / \
          3   6
         / \   \
        2   4   7

        Target = 9

        Output: True


        Example 2:

        Input:
            5
           / \
          3   6
         / \   \
        2   4   7

        Target = 28

        Output: False
        Args:
            root(TreeNode):
            k(int):

        Returns:
            bool:
        """
        comp = set()

        def dfs(node):
            if not node:
                return False
            if node.val in comp:
                return True
            comp.add(k - node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
