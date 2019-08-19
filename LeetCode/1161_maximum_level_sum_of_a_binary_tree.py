"""
Solution for 1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
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
            x(int):
        """
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    """
    Runtime: 328 ms, faster than 67.43% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    Memory Usage: 18.5 MB, less than 100.00% of Python3 online submissions for Maximum Level Sum of a Binary Tree.
    """
    def maxLevelSum(self, root):
        """
        Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

        Return the smallest level X such that the sum of all the values of nodes at level X is maximal.



        Example 1:



        Input: [1,7,0,7,-8,null,null]
        Output: 2
        Explanation:
        Level 1 sum = 1.
        Level 2 sum = 7 + 0 = 7.
        Level 3 sum = 7 + -8 = -1.
        So we return the level with the maximum sum which is level 2.


        Note:

        The number of nodes in the given tree is between 1 and 10^4.
        -10^5 <= node.val <= 10^5
        Args:
            root(TreeNode):

        Returns:
            int:
        """
        if not root:
            return 0
        queue = deque([(root, 1)])
        global_sum = root.val
        global_level = 1
        while queue:
            temp = deque([])
            local_sum = 0
            while queue:
                node, level = queue.popleft()
                if node.left:
                    temp.append((node.left, level+1))
                if node.right:
                    temp.append((node.right, level+1))
                local_sum += node.val
            if local_sum > global_sum:
                global_sum = local_sum
                global_level = level
            queue = temp
        return global_level
