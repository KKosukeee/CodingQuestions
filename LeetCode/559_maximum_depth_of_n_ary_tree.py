"""
Solution for 559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""
# Definition for a Node.
class Node:
    """
    Node object
    """
    def __init__(self, val, children):
        """
        Initialization method
        Args:
            val(int):
            children(list[Node]):
        """
        self.val = val
        self.children = children

from collections import deque
class Solution:
    """
    Runtime: 628 ms, faster than 96.80% of Python3 online submissions for Maximum Depth of N-ary Tree.
    Memory Usage: 95.2 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.
    """
    def maxDepth(self, root):
        """
        Given a n-ary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        For example, given a 3-ary tree:






        We should return its max depth, which is 3.



        Note:

        The depth of the tree is at most 1000.
        The total number of nodes is at most 5000.
        Args:
            root(Node):

        Returns:
            int:
        """
        if not root:
            return 0
        level = 0
        queue = deque([root])
        while queue:
            temp = deque([])
            while queue:
                node = queue.popleft()
                temp.extend(node.children)
            queue = temp
            level += 1
        return level
