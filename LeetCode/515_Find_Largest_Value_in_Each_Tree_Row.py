"""
Solution for 515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Runtime: 56 ms, faster than 85.52% of Python3 online submissions for Find Largest Value in
        Each Tree Row.
    Memory Usage: 15.6 MB, less than 9.52% of Python3 online submissions for Find Largest Value in
        Each Tree Row.
    """
    def largestValues(self, root):
        """
        You need to find the largest value in each row of a binary tree.

        Example:
        Input:

                  1
                 / \
                3   2
               / \   \
              5   3   9

        Output: [1, 3, 9]

        Args:
            root: root node for a binary tree

        Returns:
            list<int>: list of integers for each level's max val
        """
        if not root:
            return []

        # Initialize an array which holds all nodes in the same level
        level = [root]

        # Initialize result array
        result = [root.val]

        # Loop, while level array is not empty
        while level:

            # Initialize max_val with None
            max_val = -float('inf')

            # Initialize temp array which holds all nodes in the level
            temp = []

            # Loop through level array
            for node in level:

                # Check left and right child are not None, and append to the temp array
                if node.left:
                    temp.append(node.left)
                    max_val = max(max_val, node.left.val)

                if node.right:
                    temp.append(node.right)
                    max_val = max(max_val, node.right.val)

            # Append max_val to the result array
            if max_val != -float('inf'):
                result.append(max_val)

            level = temp

        # Return the result array
        return result
