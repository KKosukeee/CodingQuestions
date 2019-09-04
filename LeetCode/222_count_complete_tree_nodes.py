"""
Solution for 222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/
"""
# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode class
    """
    def __init__(self, x):
        """
        Initialization method

        Args:
            x(int):
        """
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    """
    Runtime: 84 ms, faster than 83.52% of Python3 online submissions for Count Complete Tree Nodes.
    Memory Usage: 21.3 MB, less than 6.90% of Python3 online submissions for Count Complete Tree Nodes.
    """
    def sub_optimal(self, root: TreeNode) -> int:
        """
        Sub-optimal solution using BFS. This runs in O(N)

        Args:
            root(TreeNode):

        Returns:
            int:

        """
        if not root:
            return 0
        count = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return count

    def optimal(self, root: TreeNode) -> int:
        """
        The optimal solution which runs in O(log(N)**2)

        Args:
            root(TreeNode):

        Returns:
            int:

        """
        if not root:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        if left_depth == right_depth:
            return 2 ** left_depth + self.countNodes(root.right)
        else:
            return 2 ** right_depth + self.countNodes(root.left)

    def get_depth(self, node):
        """
        This methods gets depth of a BT

        Args:
            node(TreeNode):

        Returns:
            int:

        """
        if not node:
            return 0
        return self.get_depth(node.left) + 1

    def countNodes(self, root: TreeNode) -> int:
        """
        Given a complete binary tree, count the number of nodes.

        Note:

        Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

        Example:

        Input:
            1
           / \
          2   3
         / \  /
        4  5 6

        Output: 6

        Args:
            root(TreeNode):

        Returns:
            int:

        """
        return self.optimal(root)
