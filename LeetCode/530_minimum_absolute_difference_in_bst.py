"""
Solution for 530. Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for BSTs
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x: int value for a node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 56 ms, faster than 100.00% of Python3 online submissions for Minimum Absolute
        Difference in BST.
    Memory Usage: 15.4 MB, less than 5.17% of Python3 online submissions for Minimum Absolute
        Difference in BST.
    """
    def getMinimumDifference(self, root):
        """
        Given a binary search tree with non-negative values, find the minimum absolute difference
        between values of any two nodes.

        Example:

        Input:

           1
            \
             3
            /
           2

        Output:
        1

        Explanation:
        The minimum absolute difference is 1, which is the difference between 2 and 1 (or between
        2 and 3).
        Args:
            root: TreeNode object as a root of the BST

        Returns:
            int: minimum absolute difference between any two nodes in the BST
        """
        # create sorted array
        sorted_array = self.iterative_traversal(root)
        print(sorted_array)

        # initialize min_diff
        min_diff = float('inf')

        # loop thorugh the array and compare two consecutive elements
        for i in range(len(sorted_array) - 1):
            # update current min value
            min_diff = min(min_diff, abs(sorted_array[i] - sorted_array[i + 1]))

        return min_diff

    def iterative_traversal(self, root):
        """
        Iterative approach for in-order traversal
        Args:
            root: TreeNode object as a root of the BST

        Returns:
            int: minimum absolute difference between any two nodes in the BST
        """
        stack = []
        result = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result

    def recursive_traversal(self, root):
        """
        Recursive approach for in-order traversal
        Args:
            root: TreeNode object as a root of the BST

        Returns:
            int: minimum absolute difference between any two nodes in the BST
        """
        if not root:
            return []

        left_subtree = self.recursive_traversal(root.left)
        right_subtree = self.recursive_traversal(root.right)
        return left_subtree + [root.val] + right_subtree
