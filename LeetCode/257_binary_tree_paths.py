"""
Solution for 257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
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
            x: int value as the value of the node
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 40 ms, faster than 89.10% of Python3 online submissions for Binary Tree Paths.
    Memory Usage: 12.9 MB, less than 89.69% of Python3 online submissions for Binary Tree Paths.
    """
    def binaryTreePaths(self, root):
        """
        Given a binary tree, return all root-to-leaf paths.

        Note: A leaf is a node with no children.

        Example:

        Input:

           1
         /   \
        2     3
         \
          5

        Output: ["1->2->5", "1->3"]

        Explanation: All root-to-leaf paths are: 1->2->5, 1->3
        Args:
            root: TreeNode object as a root node of a BT

        Returns:
            list<str>: where for each element is the path from the root to the leaves
        """
        if not root:
            return []

        result = []
        self.dfs(root, '', result)
        return result

    def dfs(self, root, comb, result):
        if not root:
            return
        elif self.is_leaf(root):
            result.append(comb + str(root.val))
            return

        self.dfs(root.left, comb + '{}->'.format(root.val), result)
        self.dfs(root.right, comb + '{}->'.format(root.val), result)

    def is_leaf(self, root):
        return not root.left and not root.right
