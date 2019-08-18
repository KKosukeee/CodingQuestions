"""
Solution for 700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
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
    Runtime: 76 ms, faster than 97.48% of Python3 online submissions for Search in a Binary Search Tree.
    Memory Usage: 15.8 MB, less than 9.09% of Python3 online submissions for Search in a Binary Search Tree.
    """
    def searchBST(self, root, val):
        """
        Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

        For example,

        Given the tree:
                4
               / \
              2   7
             / \
            1   3

        And the value to search: 2
        You should return this subtree:

              2
             / \
            1   3
        In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

        Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
        Args:
            root(TreeNode):
            val(int):

        Returns:
            TreeNode:
        """
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else:
                node = node.right
        return None
