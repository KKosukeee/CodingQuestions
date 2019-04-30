"""
Solution for 100. Same Tree
https://leetcode.com/problems/same-tree/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    """
    A node in a BST
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x: integer value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 36 ms, faster than 83.16% of Python3 online submissions for Same Tree.
    Memory Usage: 13.2 MB, less than 5.74% of Python3 online submissions for Same Tree
    """
    def isSameTree(self, p, q):
        """
        Given two binary trees, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical and the
        nodes have the same value.

        Example 1:

        Input:     1         1
                  / \       / \
                 2   3     2   3

                [1,2,3],   [1,2,3]

        Output: true
        Example 2:

        Input:     1         1
                  /           \
                 2             2

                [1,2],     [1,null,2]

        Output: false
        Example 3:

        Input:     1         1
                  / \       / \
                 2   1     1   2

                [1,2,1],   [1,1,2]

        Output: false
        Args:
            p: root node object to check whether both BSTs are the same
            q: root node object to check whether both BSTs are the same

        Returns:
            bool: True if they are the same BSTs, otherwise False
        """
        # Initialize two queues for each tree with root nodes
        q1, q2 = deque([p]), deque([q])

        # Loop while q1 and q2 len(q1) == len(q2)
        while (q1 and q2) and (len(q1) == len(q2)):
            p1 = q1.popleft()  # -> None
            p2 = q2.popleft()  # -> None

            # Check for left and right child for each tree
            if (p1 and p2) and (p1.val == p2.val):
                # If the values are the same, put them in q1, q2
                q1.extend([p1.left, p1.right])
                q2.extend([p2.left, p2.right])
            elif (not p1 and not p2):
                continue
            else:
                # If the values are not the same, return False
                return False

        # Return True
        return True
