"""
Solution for 971. Flip Binary Tree To Match Preorder Traversal
https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode object
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
    Runtime: 40 ms, faster than 92.31% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
    Memory Usage: 13.9 MB, less than 20.00% of Python3 online submissions for Flip Binary Tree To Match Preorder Traversal.
    """
    def flipMatchVoyage(self, root, voyage):
        """
        Given a binary tree with N nodes, each node has a different value from {1, ..., N}.

        A node in this binary tree can be flipped by swapping the left child and the right child of that node.

        Consider the sequence of N values reported by a preorder traversal starting from the root.  Call such a sequence of N values the voyage of the tree.

        (Recall that a preorder traversal of a node means we report the current node's value, then preorder-traverse the left child, then preorder-traverse the right child.)

        Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

        If we can do so, then return a list of the values of all nodes flipped.  You may return the answer in any order.

        If we cannot do so, then return the list [-1].



        Example 1:



        Input: root = [1,2], voyage = [2,1]
        Output: [-1]
        Example 2:



        Input: root = [1,2,3], voyage = [1,3,2]
        Output: [1]
        Example 3:



        Input: root = [1,2,3], voyage = [1,2,3]
        Output: []


        Note:

        1 <= N <= 100

        Args:
            root: TreeNode object
            voyage: list<int>

        Returns:
            list<int>:
        """
        self.flipped = []
        self.i = 0

        def helper(node):
            if not node:
                return
            if node.val != voyage[self.i]:
                self.flipped = [-1]
                return
            self.i += 1
            if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                self.flipped.append(node.val)
                helper(node.right)
                helper(node.left)
            else:
                helper(node.left)
                helper(node.right)

        helper(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped
