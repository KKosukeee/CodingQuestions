"""
Solution for 114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for a BT
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x: int value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 40 ms, faster than 95.01% of Python3 online submissions for Flatten Binary Tree to
        Linked List.
    Memory Usage: 13.4 MB, less than 28.73% of Python3 online submissions for Flatten Binary Tree
        to Linked List.
    """
    def flatten(self, root):
        """
        Given a binary tree, flatten it to a linked list in-place.

        For example, given the following tree:

            1
           / \
          2   5
         / \   \
        3   4   6
        The flattened tree should look like:

        1
         \
          2
           \
            3
             \
              4
               \
                5
                 \
                  6
        Args:
            root: TreeNode as the head of the BT

        Returns:

        """

        def in_order(current):
            """
            This traverses the tree in in-order manner
            Args:
                current: TreeNode object

            Returns:
                tuple<TreeNode>: as the head and the trail of sub BT
            """
            if not current:
                return None, None

            left_flatten, left_tail = in_order(current.left)
            right_flatten, right_tail = in_order(current.right)

            if left_flatten:
                left_tail.right = right_flatten
                current.right = left_flatten
            else:
                current.right = right_flatten

            current.left = None
            if right_tail:
                return current, right_tail
            elif left_tail:
                return current, left_tail

            return current, current

        in_order(root)
