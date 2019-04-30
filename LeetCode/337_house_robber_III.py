"""
Solution for 337. House Robber III
https://leetcode.com/problems/house-robber-iii/
"""

# Definition for a binary tree node.
class TreeNode:
    """
    Node object for binary tree
    """
    def __init__(self, x):
        """
        Initialization method for a node
        Args:
            x:
        """
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Runtime: 68 ms, faster than 31.24% of Python3 online submissions for House Robber III.
    Memory Usage: 16.5 MB, less than 5.09% of Python3 online submissions for House Robber III.
    """
    def rob(self, root, dp={}):
        """
        The thief has found himself a new place for his thievery again. There is only one entrance
        to this area, called the "root." Besides the root, each house has one and only one parent
        house. After a tour, the smart thief realized that "all houses in this place forms a binary
        tree". It will automatically contact the police if two directly-linked houses were broken
        into on the same night.

        Determine the maximum amount of money the thief can rob tonight without alerting the police.

        Example 1:

        Input: [3,2,3,null,3,null,1]

             3
            / \
           2   3
            \   \
             3   1

        Output: 7
        Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
        Example 2:

        Input: [3,4,5,1,3,null,1]

             3
            / \
           4   5
          / \   \
         1   3   1

        Output: 9
        Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
        Args:
            root:
            dp:

        Returns:

        """
        # base case
        if not root:
            return 0
        if root in dp:
            return dp[root]
        # recursive case
        v1 = self.rob(root.left) + self.rob(root.right)
        v2 = root.val

        if root.left:
            v2 += self.rob(root.left.left)
            v2 += self.rob(root.left.right)

        if root.right:
            v2 += self.rob(root.right.left)
            v2 += self.rob(root.right.right)

        dp[root] = max(v1, v2)
        return max(v1, v2)
