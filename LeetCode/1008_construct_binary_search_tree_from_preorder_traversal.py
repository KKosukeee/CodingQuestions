"""
Solution for 1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node objecct for a BT tree
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value for the node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 28 ms, faster than 99.83% of Python3 online submissions for Construct Binary Search
        Tree from Preorder Traversal.
    Memory Usage: 13 MB, less than 90.64% of Python3 online submissions for Construct Binary
        Search Tree from Preorder Traversal.
    """
    def bstFromPreorder(self, preorder):
        """
        Return the root node of a binary search tree that matches the given preorder traversal.

        (Recall that a binary search tree is a binary tree where for every node, any descendant of
        node.left has a value < node.val, and any descendant of node.right has a value > node.val.
        Also recall that a preorder traversal displays the value of the node first, then traverses
        node.left, then traverses node.right.)



        Example 1:

        Input: [8,5,1,7,10,12]
        Output: [8,5,10,1,7,null,12]

        Args:
            preorder: list of integers as seen by the pre-order traversal

        Returns:
            TreeNode: as the root of the BT tree
        """
        if not preorder:
            return []

        root = TreeNode(preorder[0])
        stack = [root]

        for num in preorder[1:]:
            if stack and stack[-1].val > num:
                stack[-1].left = TreeNode(num)
                stack.append(stack[-1].left)
            elif stack and stack[-1].val < num:
                while stack and stack[-1].val < num:
                    popped = stack.pop()

                popped.right = TreeNode(num)
                stack.append(popped.right)

        return root
