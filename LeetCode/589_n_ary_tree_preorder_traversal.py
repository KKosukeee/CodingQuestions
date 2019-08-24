"""
Solution for 589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
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

class Solution:
    """
    Runtime: 656 ms, faster than 71.70% of Python3 online submissions for N-ary Tree Preorder Traversal.
    Memory Usage: 95.2 MB, less than 13.64% of Python3 online submissions for N-ary Tree Preorder Traversal.
    """
    def preorder(self, root):
        """
        Given an n-ary tree, return the preorder traversal of its nodes' values.

        For example, given a 3-ary tree:







        Return its preorder traversal as: [1,3,5,6,2,4].



        Note:

        Recursive solution is trivial, could you do it iteratively?
        Args:
            root(Node):

        Returns:
            list[int]:
        """
        if not root:
            return []
        nodes, stack = [], [root]
        while stack:
            node = stack.pop()
            nodes.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return nodes
