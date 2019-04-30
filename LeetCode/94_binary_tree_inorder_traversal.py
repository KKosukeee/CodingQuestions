"""
Solution for 94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a linked-list
    """
    def __init__(self, x):
        """
        Initialization methodc
        Args:
            x: integer value for the node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 48 ms, faster than 17.92% of Python3 online submissions for Binary Tree Inorder
        Traversal.
    Memory Usage: 13.4 MB, less than 5.64% of Python3 online submissions for Binary Tree Inorder
        Traversal.
    """
    def inorderTraversal(self, root):
        """
        Given a binary tree, return the inorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,3,2]
        Args:
            root: Node object for a root node

        Returns:
            list<Node>: containing Node object in-order order.
        """
        # base cases
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]
        # recursive cases
        else:
            left_nodes = self.inorderTraversal(root.left) + [root.val]
            merged = left_nodes + self.inorderTraversal(root.right)
            return merged
