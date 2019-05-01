"""
Solution for 144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode(object):
    """
    Node object for BST
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: integer value for a Node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    Runtime: 20 ms, faster than 79.06% of Python online submissions for Binary Tree Preorder
        Traversal.
    Memory Usage: 11.7 MB, less than 5.08% of Python online submissions for Binary Tree Preorder
        Traversal.
    """
    def recursive_approach(self, root):
        """
        Recursive approach
        Args:
            root: root TreeNode object for a BST

        Returns:
            list<int>: containing all values in pre-order traversal
        """
        if not root:
            return []

        def recursion(root, seen):
            # if the root is None, then it's a base case
            if not root:
                return

            # otherwise it's a recursive case
            else:

                # append to seen array
                seen.append(root.val)

                # call for left node first
                recursion(root.left, seen)

                # call for right node then
                recursion(root.right, seen)

        pre_order = []
        recursion(root, pre_order)
        return pre_order

    def iterative_approach(self, root):
        """
        Iterative approach
        Args:
            root: root TreeNode object for a BST

        Returns:
            list<int>: containing all values in pre-order traversal
        """
        if not root:
            return []

        # initialize a stack with root
        stack = [root]

        # initialize result array with values
        result = []

        # loop while stack is not empty
        while stack:

            # pop an element from the stack
            node = stack.pop()

            # append RIGHT node first
            if node.right:
                stack.append(node.right)

            # append LEFT node then
            if node.left:
                stack.append(node.left)

            # append to the result array
            result.append(node.val)

        # return the result array
        return result

    def preorderTraversal(self, root):
        """
        Given a binary tree, return the preorder traversal of its nodes' values.

        Example:

        Input: [1,null,2,3]
           1
            \
             2
            /
           3

        Output: [1,2,3]
        Args:
            root:

        Returns:

        """
        return self.iterative_approach(root)
