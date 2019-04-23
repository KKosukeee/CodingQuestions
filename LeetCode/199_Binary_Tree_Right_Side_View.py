"""
Solution for 199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Runtime: 40 ms, faster than 94.40% of Python3 online submissions for Binary Tree Right Side
        View.
    Memory Usage: 13.3 MB, less than 5.13% of Python3 online submissions for Binary Tree Right Side
        View.
    """

    # Time: O(n), Space: O(n)
    def rightSideView(self, root):
        """
        Given a binary tree, imagine yourself standing on the right side of it, return the values
        of the nodes you can see ordered from top to bottom.

        Example:

        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---

        Args:
            root: root node for a binary tree to begin with

        Returns:
            list<int>: an array contains all values that are seen from right side
        """
        # If root is None, then return an empty array
        if not root:
            return []

        # Initialize a result array
        result = []

        # Initialize a array which holds all nodes at a given level
        level = [root]

        # Loop while level array isn't empty
        while level:

            # Create a temporary level place holder
            temp = []

            # Assign right_most_node which will be the right most node at the end
            right_most_node = None

            # Loop for all nodes in level array
            for node in level:

                # Append it's left then it's right node
                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

                # Update right_most_node
                right_most_node = node

            # Append right_most_node to result array
            if right_most_node:
                result.append(right_most_node.val)

            level = temp

        # return the result array
        return result
