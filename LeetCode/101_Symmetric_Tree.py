"""
A solution for 101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    A solution class
    """
    def isSymmetric(self, root):
        """
        Checks if the tree is symmetric or not

        Args:
            root: root node to start with

        Returns:
            bool: indicating if the tree is a symmetric or not
        """
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left, right):
        """
        Helper function to call recursively

        Args:
            left: left node for a parent node
            right: right node for a parent node

        Returns:
            bool: whether the subtree is symmetric or not
        """
        if not left and not right:
            return True
        elif not left or not right:
            return False
        else:
            if left.val == right.val:
                in_pair = self.is_mirror(left.right, right.left)
                out_pair = self.is_mirror(left.left, right.right)
                return in_pair and out_pair
            else:
                return False


"""
recursive approach
Time: O(n), Space: O(n)
1. create a function with two node as arguments
2. if both of them are None, then return True - it's a base case
3. if either one of them is None, then return  False - it's another base case
4. otherwise compare both values, if they are the same, call recursively
5. if not the same, then it's not a mirror tree
6. check for an inner pair and an outer pair
7. AND them 
"""
