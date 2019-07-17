"""
Solution for 429. N-ary Tree Level Order Traversal
"""

from collections import deque

# Definition for a Node.
class Node:
    """
    Node object
    """
    def __init__(self, val, children):
        """
        Initialization
        Args:
            val: int
            children: list<Node>
        """
        self.val = val
        self.children = children

class Solution:
    """
    Runtime: 96 ms, faster than 84.42% of Python3 online submissions for N-ary Tree Level Order Traversal.
    Memory Usage: 17.6 MB, less than 73.03% of Python3 online submissions for N-ary Tree Level Order Traversal.
    """
    def levelOrder(self, root):
        """
        Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

        For example, given a 3-ary tree:







        We should return its level order traversal:

        [
             [1],
             [3,2,4],
             [5,6]
        ]
        Args:
            root: Node object

        Returns:
            list<list<int>>: values in level
        """
        if not root:
            return []

        result = [[root.val]]
        level = deque([root])

        while level:
            tmp_nodes = deque()
            tmp_values = []

            while level:
                node = level.popleft()

                for child in node.children:
                    tmp_nodes.append(child)
                    tmp_values.append(child.val)

            level = tmp_nodes
            if tmp_values:
                result.append(tmp_values)

        return result
