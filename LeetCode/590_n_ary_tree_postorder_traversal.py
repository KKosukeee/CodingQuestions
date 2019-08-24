"""
Solution for 590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
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
            children(Node):
        """
        self.val = val
        self.children = children

from collections import deque

class Solution:
    """
    Runtime: 680 ms, faster than 23.04% of Python3 online submissions for N-ary Tree Postorder Traversal.
    Memory Usage: 95.3 MB, less than 7.14% of Python3 online submissions for N-ary Tree Postorder Traversal.
    """
    def postorder(self, root):
        """
        Given an n-ary tree, return the postorder traversal of its nodes' values.

        For example, given a 3-ary tree:







        Return its postorder traversal as: [5,6,3,2,4,1].


        Note:

        Recursive solution is trivial, could you do it iteratively?
        Args:
            root(Node):

        Returns:
            list[int]:

        """
        if not root:
            return []
        nodes, stack = deque([]), [root]
        while stack:
            node = stack.pop()
            nodes.appendleft(node.val)
            for child in node.children:
                stack.append(child)
        return nodes
