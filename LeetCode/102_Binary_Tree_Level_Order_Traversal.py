"""
Solution for 102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Runtime: 44 ms, faster than 75.27% of Python3 online submissions for Binary Tree Level Order
        Traversal.
    Memory Usage: 13.3 MB, less than 7.29% of Python3 online submissions for Binary Tree Level
        Order Traversal.
    """
    def levelOrder(self, root):
        """
        Given a binary tree, return the level order traversal of its nodes' values.
        (ie, from left to right, level by level).

        For example:
        Given binary tree [3,9,20,null,null,15,7],
            3
           / \
          9  20
            /  \
           15   7
        return its level order traversal as:
        [
          [3],
          [9,20],
          [15,7]
        ]

        Args:
            root: root node for a binary tree

        Returns:
            list<list<int>>: two dimensional array containing level-order nodes
        """
        # Check if root is None, return an empty array if so
        if not root:
            return []

        # Initialize answer, and level arrays
        ans, level = [], [root]

        # Loop while level is not empty
        while level:
            # Append everything in the level
            ans.append([node.val for node in level])
            temp = []

            # Get next level
            for node in level:
                temp.extend([node.left, node.right])

            # Assign level variable if leaf not empty
            level = [leaf for leaf in temp if leaf]

        return ans
