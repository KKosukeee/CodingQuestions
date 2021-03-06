"""
Solution for 617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
"""
# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 80 ms, faster than 94.94% of Python3 online submissions for Merge Two Binary Trees.
    Memory Usage: 14.2 MB, less than 17.32% of Python3 online submissions for Merge Two Binary Trees.
    """
    def mergeTrees(self, t1, t2):
        """
        Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

        You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

        Example 1:

        Input:
            Tree 1                     Tree 2
                  1                         2
                 / \                       / \
                3   2                     1   3
               /                           \   \
              5                             4   7
        Output:
        Merged tree:
                 3
                / \
               4   5
              / \   \
             5   4   7
        Args:
            t1: TreeNode object
            t2: TreeNode object

        Returns:
            TreeNode: after the merge
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
