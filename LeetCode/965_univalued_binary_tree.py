"""
Solution for 965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for BTs
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x: integer value of a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 32 ms, faster than 99.52% of Python3 online submissions for Univalued Binary Tree.
    Memory Usage: 13.1 MB, less than 54.32% of Python3 online submissions for Univalued Binary Tree.
    """
    def bfs(self, root):
        """
        Solves the problem with Breadth First Search
        Args:
            root: TreeNode object for a BT

        Returns:
            bool: representing if the BT is uni-val or not
        """
        if not root:
            return False

        # Initialize a variable with root's value
        value = root.val

        # Create level array to do the BFS
        level = deque([root])

        # Loop, while the level array contains something
        while level:

            # Create a temporary array to update level array
            temp = []

            # Loop while level array contains something
            while level:
                # Pop an element from level queue
                node = level.popleft()

                # Compare the value, and return False if they differ
                if node.val != value:
                    return False

                # Append node's left and right node
                if node.left:
                    temp.append(node.left)

                if node.right:
                    temp.append(node.right)

            # Update level array
            level = deque(temp)

        # Return True
        return True

    def dfs(self, root):
        """
        Solves the problem with Depth First Search
        Args:
            root: TreeNode object for a BT

        Returns:
            bool: representing if the BT is uni-val or not
        """
        if not root:
            return True

        # Check if root value is the same as its left node
        left_unival = (not root.left or root.val == root.left.val and self.dfs(root.left))

        # Check if root value is the same as its right node
        right_unival = (not root.right or root.val == root.right.val and self.dfs(root.right))

        return left_unival and right_unival

    def isUnivalTree(self, root):
        """
        A binary tree is univalued if every node in the tree has the same value.

        Return true if and only if the given tree is univalued.



        Example 1:


        Input: [1,1,1,1,1,null,1]
        Output: true
        Example 2:


        Input: [2,2,2,5,2]
        Output: false
        Args:
            root: TreeNode object for a BT

        Returns:
            bool: representing if the BT is uni-val or not
        """
        return self.dfs(root)
