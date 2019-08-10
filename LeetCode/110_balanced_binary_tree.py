"""
Solution for 110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode object
    """
    def __init__(self, x):
        """
        Init
        Args:
            x: int value
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 60 ms, faster than 68.36% of Python3 online submissions for Balanced Binary Tree.
    Memory Usage: 19.7 MB, less than 5.72% of Python3 online submissions for Balanced Binary Tree.
    """
    def isBalanced(self, root):
        """
        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:

        a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

        Example 1:

        Given the following tree [3,9,20,null,null,15,7]:

            3
           / \
          9  20
            /  \
           15   7
        Return true.

        Example 2:

        Given the following tree [1,2,2,3,3,null,null,4,4]:

               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        Return false.
        Args:
            root: TreeNode object

        Returns:
            bool: True or False
        """
        def helper(node):
            if not node:
                return True, 0
            lb, ld = helper(node.left)
            rb, rd = helper(node.right)
            return lb and rb and abs(ld - rd) <= 1, max(ld, rd) + 1
        boolean, _ = helper(root)
        return boolean
