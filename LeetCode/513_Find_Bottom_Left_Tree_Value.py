"""
Solution for 513. Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Runtime: 52 ms, faster than 87.30% of Python3 online submissions for Find Bottom Left Tree Value.
    Memory Usage: 15.7 MB, less than 8.16% of Python3 online submissions for Find Bottom Left Tree Value.
    """
    # Time: O(n), Space: O(n)
    def simple_approach(self, root):
        """
        Given a binary tree, find the leftmost value in the last row of the tree.

        Example 1:
        Input:

            2
           / \
          1   3

        Output:
        1
        Example 2:
        Input:

                1
               / \
              2   3
             /   / \
            4   5   6
               /
              7

        Output:
        7
        Args:
            root: root node for a binary tree

        Returns:
            int: bottom-left node's value
        """
        if not root:
            return []

        # Initialize a level array
        level = [root]

        # Bottom-left value place holder
        bottom_left = root.val

        # Loop, while level not empty
        while level:
            temp = []

            # Loop for level array
            for node in level:

                # append to temporary array for each left and right if not None
                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

            # Update level array with temporary array
            level = temp

            # Update bottom_left variable with tmep[0]
            if temp:
                bottom_left = temp[0].val

        return bottom_left

    def right_to_left_bfs(self, root):
        """
        Same question as above simple_approach function, but this one is smarter and cleaner

        Args:
            root: root for a binary tree

        Returns:
            int: bottom-left node's value
        """
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val

    def findLeftMostNode(self, root):
        return self.right_to_left_bfs(root)
