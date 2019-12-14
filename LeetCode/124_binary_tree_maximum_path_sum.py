"""
Solution for 124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  """
  Runtime: 88 ms, faster than 90.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
  Memory Usage: 20.2 MB, less than 100.00% of Python3 online submissions for Binary Tree Maximum Path Sum.
  """
  def maxPathSum(self, root: TreeNode) -> int:
    """
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

    Example 1:

    Input: [1,2,3]

           1
          / \
         2   3

    Output: 6
    Example 2:

    Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    Output: 42

    Args:
      root:

    Returns:

    """
    self.max_sum = float('-inf')
    def rec(node):
      if not node:
        return 0
      l = max(rec(node.left), 0)
      r = max(rec(node.right), 0)
      c = node.val + l + r
      self.max_sum = max(self.max_sum, c)
      return node.val + max(l, r)
    rec(root)
    return self.max_sum