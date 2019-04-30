"""
Solution for 112. Path Sum
https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a binary-search tree
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for the node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 64 ms, faster than 19.67% of Python3 online submissions for Path Sum.
    Memory Usage: 15.3 MB, less than 5.00% of Python3 online submissions for Path Sum.
    """
    def recursive_approach(self, root, sum):
        """
        Recursive solution
        Args:
            root: Node object for a root node given BST
            sum: sum to look for in the tree

        Returns:
            bool: True if such sum exist in the tree, otherwise False
        """
        if not root:
            return False
        elif not root.left and not root.right and sum == root.val:
            return True
        elif not root.left and not root.right:
            return False
        else:
            return (
                    self.hasPathSum(root.left, sum - root.val) or
                    self.hasPathSum(root.right, sum - root.val)
            )

    """
    Iterative approach
    Time: O(n), Space: O(n)
    """

    def iterative_approach(self, root, sum):
        """
        Iterative solution
        Args:
            root: Node object for a root node given BST
            sum: sum to look for in the tree

        Returns:
            bool: True if such sum exist in the tree, otherwise False
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, curr_path = stack.pop()
            if not curr.left and not curr.right and curr_path == sum:
                return True
            if curr.left:
                stack.append((curr.left, curr_path + curr.left.val))
            if curr.right:
                stack.append((curr.right, curr_path + curr.right.val))
        return False

    def hasPathSum(self, root, sum):
        """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
        adding up all the values along the path equals the given sum.

        Note: A leaf is a node with no children.

        Example:

        Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        Args:
            root: Node object for a root node given BST
            sum: sum to look for in the tree

        Returns:
            bool: True if such sum exist in the tree, otherwise False
        """
        return self.iterative_approach(root, sum)