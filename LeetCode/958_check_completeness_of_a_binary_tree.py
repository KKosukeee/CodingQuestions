"""
Solution for 958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    """
    TreeNode object
    """
    def __init__(self, x):
        """
        Initialization method
        Args:
            x:(int)
        """
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    """
    Runtime: 36 ms, faster than 98.44% of Python3 online submissions for Check Completeness of a Binary Tree.
    Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Check Completeness of a Binary Tree.
    """
    def isCompleteTree(self, root):
        """
        Given a binary tree, determine if it is a complete binary tree.

        Definition of a complete binary tree from Wikipedia:
        In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.



        Example 1:



        Input: [1,2,3,4,5,6]
        Output: true
        Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
        Example 2:



        Input: [1,2,3,4,5,null,7]
        Output: false
        Explanation: The node with value 7 isn't as far left as possible.

        Note:

        The tree will have between 1 and 100 nodes.
        Args:
            root(TreeNode):

        Returns:
            bool:
        """
        if not root:
            return True
        queue = deque([root])
        level = 0
        while queue:
            temp = deque([])
            seen_none = False
            count = len(queue)
            while queue:
                node = queue.popleft()
                if node.left:
                    if seen_none:
                        return False
                    temp.append(node.left)
                else:
                    seen_none = True
                if node.right:
                    if seen_none:
                        return False
                    temp.append(node.right)
                else:
                    seen_none = True
            if temp and count != 2 ** level:
                return False
            level += 1
            queue = temp
        return True
